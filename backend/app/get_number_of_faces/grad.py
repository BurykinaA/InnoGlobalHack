import numpy as np
from scipy import ndimage


def check_gradient(image, threshold):
    # Вычисляем градиент изображения
    gradient = np.sqrt(
        ndimage.sobel(image, axis=0) ** 2 + ndimage.sobel(image, axis=1) ** 2
    )

    # Проверяем, превышает ли максимальное значение градиента порог
    if np.max(gradient) > threshold:
        return True
    else:
        return False
