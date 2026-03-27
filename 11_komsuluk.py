import numpy as np
import cv2
# Örnek 5x5 boyutunda rastgele piksellerden oluşan bir matris
img = np.random.randint(0, 256, (5, 5), dtype=np.uint8)


# Merkezdeki p(x,y) pikselimizi belirleyelim. (Örn: x=2, y=2)
y, x = 2, 2
p = img[y, x]
print(f"Merkez Piksel p({x},{y}) = {p}\n")


# 1. N4(p) - 4'lü Komşuluk Değerleri
n4_top = img[y-1, x]
n4_bottom = img[y+1, x]
n4_left = img[y, x-1]
n4_right = img[y, x+1]
print(f"4-Komşuluk (Üst, Alt, Sol, Sağ): {n4_top}, {n4_bottom}, {n4_left}, {n4_right}")

# 2. ND(p) - Çapraz Komşuluk Değerleri
nd_top_left = img[y-1, x-1]
nd_top_right = img[y-1, x+1]
nd_bottom_left = img[y+1, x-1]
nd_bottom_right = img[y+1, x+1]
print(f"Çapraz Komşuluk (Sol-Üst, Sağ-Üst, Sol-Alt, Sağ-Alt): {nd_top_left}, {nd_top_right}, {nd_bottom_left}, {nd_bottom_right}")

# 3. N8(p) için matris dilimleme (Slicing) - 3x3'lük çekirdek çıkarma
# Bu yöntem çok daha pratiktir!
n8_kernel = img[y-1 : y+2, x-1 : x+2]
print("\n8-Komşuluk (3x3 Kernel Gösterimi):")
print(n8_kernel)