import numpy as np
import torch
import matplotlib.pyplot as plt

anti_spoofing_data = np.load("/content/drive/MyDrive/new_images/valid.npz")
X, y = anti_spoofing_data["arr_0"], anti_spoofing_data["arr_1"]


class celebaDataset_valid(torch.utils.data.Dataset):
    def __init__(
        self,
        X,
        y,
        transform=None,
        crop_face=None,
        map_transform=None,
    ):
        self.X = X
        self.y = y
        self.transform = transform
        self.crop_face = crop_face
        self.map_transform = map_transform

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return torch.tensor(X[idx, :]).permute(2, 0, 1), torch.tensor(
            0 if y[idx] == 0 else 1
        )

    def show_img(self, idx):
        # print(X[idx,:].shape)
        plt.imshow(X[idx, :].transpose((0, 1, 2)))
        plt.show()
