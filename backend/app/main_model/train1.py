from torchvision import transforms
from tqdm import tqdm
from facenet_pytorch import MTCNN, InceptionResnetV1
import torch
import matplotlib.pyplot as plt

# Define your transformations
data_transforms = transforms.Compose(
    [
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(20),
        transforms.ColorJitter(brightness=0.1, contrast=0.1, saturation=0.1, hue=0.1),
        # Add any other transformations you want
    ]
)


class celebaDataset(torch.utils.data.Dataset):
    def __init__(
        self,
        X,
        y,
        transform=data_transforms,
        crop_face=None,
        map_transform=None,
    ):
        self.X = X
        mtcnn_model = MTCNN().eval().cpu()
        self.y = y
        self.transform = transform
        self.crop_face = crop_face
        self.map_transform = map_transform

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        img = torch.tensor(X[idx, :]).permute(2, 0, 1)
        if self.transform:
            img = self.transform(img)
        return img, torch.tensor(0 if y[idx] == 0 else 1)

    def show_img(self, idx):
        print(X[idx, :].shape)
        plt.imshow(X[idx, :].transpose((0, 1, 2)))
