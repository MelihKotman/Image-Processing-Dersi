import cv2
import numpy as np

img = cv2.imread('images/lena.jpg')
rows, cols = img.shape[:2]

# 1. ÖTELEME MATRİSİ: Sağa 100 piksel, Aşağı 50 piksel kaydır
M = np.float32([[1, 0, 100], [0, 1, 50]])
# cv2.warpAffine tüm affine fonskiyonlarını çalıştırır.
otelenmis = cv2.warpAffine(img, M, (cols, rows))

# 2. DÖNDÜRME (ROTATION) MATRİSİ:
# Merkeze göre, 45 derece döndür, Ölçek 1.0 olsun
M_dondurme = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1.0)
dondurulmus = cv2.warpAffine(img, M_dondurme, (cols, rows))

cv2.imshow("Oteleme Matrisi", otelenmis)
cv2.waitKey(0)

cv2.imshow("Dondurme Matrisi", dondurulmus)
cv2.waitKey(0)

cv2.destroyAllWindows()