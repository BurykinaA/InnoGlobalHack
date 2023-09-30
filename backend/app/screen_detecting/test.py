import os
import cv2
import numpy as np
import warnings
import time

from src.anti_spoof_predict import AntiSpoofPredict
from src.generate_patches import CropImage
from src.utility import parse_model_name
warnings.filterwarnings('ignore')


SAMPLE_IMAGE_PATH = "./images/sample/"


# ?????APK??????????3:4,????????????????3:4
def check_image(image):
    height, width, channel = image.shape
    if width/height != 3/4:
        print("Image is not appropriate!!!\nHeight/Width should be 4/3.")
        return False
    else:
        return True


def test(image_name, model_dir, device_id):
    model_test = AntiSpoofPredict(device_id)
    image_cropper = CropImage()
    image = cv2.imread(SAMPLE_IMAGE_PATH + image_name)
    result = check_image(image)
    if result is False:
        height, width, channel = image.shape
        new_width = int(height * (3/4))
        start_x = int((width - new_width) / 2)
        image = image[:, start_x:start_x+new_width]
        cv2.imwrite(SAMPLE_IMAGE_PATH + 'crop.jpg', image)
    image_bbox = model_test.get_bbox(image)
    prediction = np.zeros((1, 3))
    test_speed = 0
    # sum the prediction from single model's result
    for model_name in os.listdir(model_dir):
        h_input, w_input, model_type, scale = parse_model_name(model_name)
        param = {
            "org_img": image,
            "bbox": image_bbox,
            "scale": scale,
            "out_w": w_input,
            "out_h": h_input,
            "crop": True,
        }
        if scale is None:
            param["crop"] = False
        img = image_cropper.crop(**param)
        start = time.time()
        print(model_name)
        prediction += model_test.predict(img, os.path.join(model_dir, model_name))
        test_speed += time.time()-start

    # draw result of prediction
    label = np.argmax(prediction)
    return label
    # value = prediction[0][label]/2
    # if label == 1:
    #     print("Image '{}' is Real Face. Score: {:.2f}.".format(image_name, value))
    #     result_text = "RealFace Score: {:.2f}".format(value)
    #     color = (255, 0, 0)
    # else:
    #     print("Image '{}' is Fake Face. Score: {:.2f}.".format(image_name, value))
    #     result_text = "FakeFace Score: {:.2f}".format(value)
    #     color = (0, 0, 255)
    # print("Prediction cost {:.2f} s".format(test_speed))
    # cv2.rectangle(
    #     image,
    #     (image_bbox[0], image_bbox[1]),
    #     (image_bbox[0] + image_bbox[2], image_bbox[1] + image_bbox[3]),
    #     color, 2)
    # cv2.putText(
    #     image,
    #     result_text,
    #     (image_bbox[0], image_bbox[1] - 5),
    #     cv2.FONT_HERSHEY_COMPLEX, 0.5*image.shape[0]/1024, color)

    # format_ = os.path.splitext(image_name)[-1]
    # result_image_name = image_name.replace(format_, "_result" + format_)
    # cv2.imwrite(SAMPLE_IMAGE_PATH + result_image_name, image)


def get_sreenshot(img):
    """
    1 - real
    0 - fake
    """
    return test(img, 'resources/anti_spoof_models', 0)
