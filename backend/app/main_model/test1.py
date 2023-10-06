import torch
from torch import nn
from torchvision.models import resnet50
from facenet_pytorch import MTCNN, InceptionResnetV1
from sklearn.model_selection import train_test_split
from torch.utils.data import Subset
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms
from app.main_model.model2 import CustomModel


mtcnn_model = MTCNN().eval().cpu()  # MTCNN на CPU
resnet_model = InceptionResnetV1(pretrained="vggface2").eval().to("cpu")
model = CustomModel()
model.load_state_dict(
    torch.load(
        r"D:\InnoHack\InnoGlobalHack\backend\app\main_model\data\model_epoch_final.pth", map_location=torch.device("cpu")
    )
)
model.eval()


def get_score(X):
    transform = transforms.Compose([
        transforms.ToPILImage(),
        transforms.Resize((128, 128)),
        transforms.ToTensor(),
    ])

    # Применяем трансформацию к изображению
    X = transform(X)
    X = torch.tensor(X).unsqueeze(0).float()
    # with torch.no_grad():
    #     outputs = model(X, mtcnn_model, resnet_model)
    #     _, predicted = torch.max(outputs.data, 1)

    with torch.no_grad():
        outputs = model(X, mtcnn_model, resnet_model)
        # Получаем вероятности с помощью softmax
        probabilities = torch.nn.functional.softmax(outputs.data, dim=1)
        print(probabilities)
        # Если вероятность класса 0 меньше 0.8, присваиваем класс 1
        predicted = (probabilities[:, 1] > 0.976).long()
        print(probabilities[:, 1])
        print(predicted)

    return 0 if predicted else 1
