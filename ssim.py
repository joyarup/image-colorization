import math
import numpy as np
from skimage.metrics import structural_similarity as ssim

def PSNR(x, y):
    mse = np.mean((x - y) ** 2)
    max = 255
    psnr = 20 * math.log10(max / math.sqrt(mse))
    return psnr

first = np.array([[1, 4, 5,1, 4, 5,1], [5, 8, 9,1, 4, 5,1], [1,2,3,1, 4, 5,1], [1,2,3,1, 4, 5,1], [1,2,3,1, 4, 5,1], [1,2,3,1, 4, 5,1], [1,2,3,1, 4, 5,1]])
second = np.array([[2, 3, 4,2,3,4,5], [5,4,2,3,4,5,1], [1,2,3,2,3,4,5], [1,2,3,1, 4, 5,1], [1,2,3,1, 4, 5,1], [1,2,3,1, 4, 5,1], [1,2,3,1, 4, 5,1]])
psnr = PSNR(first, second)
print(psnr)
s = ssim(first, second)
print(s)
