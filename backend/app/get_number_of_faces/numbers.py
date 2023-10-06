import torch
from PIL import Image

# import facenet_pytorch
import yaml
from PIL import Image
from facenet_pytorch import MTCNN, InceptionResnetV1
import torch
import numpy as np
from PIL import Image, ImageDraw
from IPython import display
import matplotlib.pyplot as plt
from torchvision import transforms

# # Создаем экземпляр MTCNN
mtcnn = MTCNN(
    margin=0,
    thresholds=[0.4, 0.4, 0.4],
    keep_all=True,
    post_process=False,
    device="cpu",
)


def get_numbers(img):
    image = Image.open(img)  # plt.imread()
    boxes, _ = mtcnn.detect(image)

    # Проверка, найдено ли хотя бы одно лицо
    if boxes is not None:
        face_area = sum([(x2 - x1) * (y2 - y1) for x1, y1, x2, y2 in boxes])
        image_area = image.size[0] * image.size[1]
        face_ratio = face_area / image_area * 100
    else:
        face_ratio = 0

    return len(boxes) if boxes is not None else 0, face_ratio
