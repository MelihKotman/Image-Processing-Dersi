import numpy as np
import cv2

# Fotoğrafı gri tonlama çevirin ve gösterin.
img = cv2.imread('01_odev/image/Vesikalik.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('Portre: ', img)
cv2.waitKey(0)

# Fotoğrafın matris boyutları analiz ettirip ekrana yazdırın.
print(f"Matris Boyutları: {img.shape}")

# Sadece yüzünüzü kapsayan bölgeyi (ROI slicing) keserek ayrı pencerede gösterin.
roi = img[160:360, 160:360]

cv2.imshow('ROI: ', roi)
cv2.waitKey(0)

# Kesilen yüz bölgesini, NumPy matris matematiği kullanarak 2-bit (4 renk) olacak şekilde yuvarlama faktörüyle nicemleyip (quantization) "False Contouring/Posterization" hatasını üretin.
seviye = 2 ** 2

faktor = 256 // seviye

nicemli = (roi // faktor) * faktor

cv2.imshow(f'2 bit (4 renk)', nicemli)
cv2.waitKey()

cv2.destroyAllWindows()