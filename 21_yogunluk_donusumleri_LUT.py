import cv2
import numpy as np

img = cv2.imread('images/karanlik_oda.png')

cv2.imshow("Goruntu", img)
cv2.waitKey(0)

# 1. Image Negative
negatif = 255 - img

cv2.imshow("Gorselin negatifi", negatif)
cv2.waitKey(0)

# 2. Logarithmic Transform (Normalizasyon Taktikli)
c = 255 / np.log(1 + np.max(img))
log_img = c * (np.log(img.astype(np.float64) + 1))
log_img = np.array(log_img, dtype=np.uint8)

cv2.imshow("Gorselin logaritmik transformesi", log_img)
cv2.waitKey(0)

# 3. Gamma Transform: Lookup Table (LUT) Hızlandırıcısı PÜF NOKTASI!
gamma = 0.4 # Pikseller açılır/aydınlanır
# Her bir milyon piksel için kuvvet işlemi yapmak GPU/CPU düşmanıdır!
# LUT: Her seferinde hesaplamak yerine önce bir tablo yaratıp sonra saniyede eşleştirir:
lookUpTable = np.array([((i / 255.0) ** gamma) * 255
                        for i in np.arange(0, 256)]).astype("uint8")
gamma_img = cv2.LUT(img, lookUpTable)

cv2.imshow("Gama Transformu (LUT)", gamma_img)
cv2.waitKey(0)

cv2.destroyAllWindows(0)

