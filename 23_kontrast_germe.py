import cv2
import numpy as np

img = cv2.imread('images/puslu.png', 0)

cv2.imshow("Puslu hava", img)
cv2.waitKey(0)

# Min ve Max tonları bul ($r_{min}$, $r_{max}$)
min_val = np.min(img)
max_val = np.max(img)

# Formül: (r - min) / (max - min) * 255
katsayi = 255.0 / (max_val - min_val)
stretched = (img - min_val) * katsayi

# Sonucu tam sayı 8-bit renk formatına çevir
stretched = np.uint8(stretched)

cv2.imshow("Islemden gecmis puslu", stretched)
cv2.waitKey(0)

cv2.destroyAllWindows()