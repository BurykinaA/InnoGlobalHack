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

device = "cpu"  # torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# print(device)


class CustomModel(nn.Module):
    def __init__(self):
        super(CustomModel, self).__init__()
        self.conv1 = nn.Conv2d(3, 64, kernel_size=3, stride=2, padding=1)
        self.bn1 = nn.BatchNorm2d(64)
        self.pool1 = nn.MaxPool2d(kernel_size=2)
        self.conv2 = nn.Conv2d(64, 128, kernel_size=3, stride=2, padding=1)
        self.bn2 = nn.BatchNorm2d(128)
        self.pool2 = nn.MaxPool2d(kernel_size=2)
        self.dense = nn.Linear(128 * 8 * 8, 512, bias=False)
        self.bn3 = nn.BatchNorm1d(512)
        self.dropout = nn.Dropout(0.1)

        # Additional linear layers
        self.fc1 = nn.Linear(512 + 512, 256)
        self.bn4 = nn.BatchNorm1d(256)
        self.fc2 = nn.Linear(256, 128)
        self.bn5 = nn.BatchNorm1d(128)

        # Final layer
        self.fc3 = nn.Linear(128, 2)

    def forward(self, x, mtcnn, resnet):
        x = x.to(device)

        # First input
        x1 = self.pool1(F.relu(self.bn1(self.conv1(x))))
        x1 = self.pool2(F.relu(self.bn2(self.conv2(x1))))
        x1 = x1.view(x.size(0), -1)
        x1 = self.dropout(self.bn3(self.dense(x1)))

        # Second input
        x2_list = torch.zeros((x.size(0), 512)).to(device)
        for i in range(x.size(0)):
            img = x[i].permute(1, 2, 0).cpu()  # Перемещение изображения на CPU
            detected_faces = mtcnn(img)
            if detected_faces is not None:
                detected_faces = detected_faces.unsqueeze(0).to(
                    device
                )  # add batch dimension
                resnet.eval()
                detected_faces = resnet(detected_faces)
            else:
                detected_faces = torch.zeros((1, 512)).to(
                    device
                )  # assuming the output of resnet is of shape (batch_size, 512)
            x2_list[i] = detected_faces

        # Merge
        x = torch.cat((x1, x2_list), dim=1)

        # Additional linear layers with activation and batch normalization
        x = F.relu(self.bn4(self.fc1(x)))
        x = F.relu(self.bn5(self.fc2(x)))

        # Classification
        x = self.fc3(x)

        return x
