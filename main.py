# -*- coding: utf-8 -*-
"""
前置:輸入圖片
noise_adder = Noise.ImageNoise(picture)

七種加噪功能
noise_adder.SaltedPepper(P, Noise_max = 1, Noise_min = 0)
noise_adder.LaplacianNoise(mu = 0, sigma = 0.1)
noise_adder.ContinuousOcclusion(BlockSize, PosX):
noise_adder.GlitchNoise(P, orientation='vertical', param_nam='hetero'):
noise_adder.GaussianNoise(mu = 0, sigma = 0.1)
noise_adder.PoissonNoise(plambda)
noise_adder.SpeckleNoise()

"""

import matplotlib.pyplot as plt
import Noise
from scipy.sparse import csr_matrix, csc_matrix, coo_matrix
import cv2


# 讀圖，顏色正確被顯示
cifar10 = cv2.imread('cifar10.jpg')
cifar10 = cv2.cvtColor(cifar10, cv2.COLOR_BGR2RGB)
Lenna = cv2.imread('lena_std.tif')
Lenna = cv2.cvtColor(Lenna, cv2.COLOR_BGR2RGB)


# 彩色圖片
noise_adder = Noise.ImageNoise(cifar10/255)
Y1          = noise_adder.SaltedPepper(20)
plt.axis('off')
plt.imshow(Y1)
plt.show()

# 灰階圖片
# Lenna_gray  = cv2.cvtColor(Lenna, cv2.COLOR_RGB2GRAY)
# noise_adder = Noise.ImageNoise(Lenna_gray/255)
# Y2          = noise_adder.SaltedPepper(20)
# plt.axis('off')
# plt.imshow(Y2, cmap='gray')
# plt.show()

# 稀疏矩陣
# Lenna_gray  = cv2.cvtColor(Lenna, cv2.COLOR_RGB2GRAY)
# sparse      = csr_matrix(Lenna_gray)
# noise_adder = Noise.ImageNoise(sparse)
# Y3_sparse   = noise_adder.SaltedPepper(20)
# Y3          = Y3_sparse.toarray()
# plt.axis('off')
# plt.imshow(Y3, cmap='gray')
# plt.show()



