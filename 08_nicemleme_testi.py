import cv2
import numpy as np

# Farklı IMREAD modlarında boyutlar değişir!

# 1. Renkli (3 Kanal - M x N x 3 matris)
img_color = cv2.imread('images/lena.jpg', cv2.IMREAD_COLOR)

# 2. Gri Tonlama (Tek Kanal - M x N matris)
img_gray = cv2.imread('images/lena.jpg', cv2.IMREAD_GRAYSCALE)

# Bit derinliğini test etme (Nicemleme)
for bit in [8, 4, 2, 1]:

    # Toplam mevcut seviye sayısı
    seviye = 2 ** bit

    # Yuvarlama faktörü
    faktor = 256 // seviye

    # NumPy vektörel matematiği ile yuvarlatıyoruz
    nicemli = (img_gray // faktor) * faktor

    cv2.imshow(f'{seviye} Seviye ({bit}-bit)', nicemli)
    cv2.waitKey()