import torch
import facenet_pytorch
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
mtcnn = MTCNN(margin=20, thresholds=[0.6, 0.6, 0.6], keep_all=True, post_process=False, device='cpu')

def get_numbers(img):
    image = Image.open(img) #plt.imread()
    faces = mtcnn(image)

    return len(faces)

    # if len(faces) > 1:
    #     fig, axes = plt.subplots(1, len(faces))
    #     for face, ax in zip(faces, axes):
    #         ax.imshow(face.permute(1, 2, 0).int().numpy())
    #         ax.axis('off')
    # elif len(faces != 0):
    #     fig, ax = plt.subplots(1, 1)
    #     ax.imshow(faces[0].permute(1, 2, 0).int().numpy())
    #     ax.axis('off')
    # fig.show()

    # Вывод количества найденных лиц
    