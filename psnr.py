import math
import numpy as np


def PSNR(x, y):
    mse = np.mean((x - y) ** 2)
    max = 255
    psnr = 20 * math.log10(max / math.sqrt(mse))
    return psnr

first = np.array([[1, 4, 5], [5, 8, 9], [1,2,3]])
second = np.array([[2, 3, 4], [5, 4, 3], [1,2,3]])
psnr = PSNR(first, second)
print(psnr)
