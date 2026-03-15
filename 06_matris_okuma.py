import cv2
import numpy as np

# Farklı IMREAD modlarında boyutlar değişir!

# 1. Renkli (3 Kanal - M x N x 3 matris)
img_color = cv2.imread('images/lena.jpg', cv2.IMREAD_COLOR)

# 2. Gri Tonlama (Tek Kanal - M x N matris)
img_gray = cv2.imread('images/lena.jpg', cv2.IMREAD_GRAYSCALE)

print(f"Renkli Boyut: {img_color.shape}") # (512, 512, 3)
print(f"Gri Boyut: {img_gray.shape}") # (512, 512)
print(f"Veri Tipi: {img_gray.dtype}") # uint8