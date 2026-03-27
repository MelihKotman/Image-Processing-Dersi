import cv2
import numpy as np

# 1.Kendi beğendiğiniz manzara/araba vb. bir fotoğrafı okuyunuz.
car_img = cv2.imread('image/mercedes_mclaren_slr.png')

# 2. Fotoğrafın tam merkezine `cv2.circle()`ile daire şeklinde siyah/beyaz bir maske yaratın (Merkez Objelik).

# - Görüntünün boyutunu al
rows, cols = car_img.shape[:2]

# - Görüntüyle aynı boyutta, tek kanallı ve tamamen siyah (0) bir matris oluşturuyoruz.
maske = np.zeros((rows, cols), dtype = np.uint8)

# - Merkeze beyaz (255) renkte, içi dolu (-1) bir daire çiziyoruz.
center_coor = (cols // 2, rows // 2)
rad = int(min(rows, cols) * 0.4)
cv2.circle(maske, center_coor, rad, 255, -1)

# 3. `cv2.bitwise_and` ile fotoğrafınızın sadece köşelerini kapatıp bir odak (vignette/mask) yaratınız.

# - Maskede siyah (0) olan köşeler orijinal görüntüyü de yutacak.
masked_img = cv2.bitwise_and(car_img, car_img, mask = maske)

# 4. `cv2.getRotationMatrix2D` kullanarak resmi saat yönünde hafifçe eğin (örneğin 15 derece). Interpolasyon yöntemini `cv2.INTER_LINEAR` ayarlayın.

# - Not: OpenCV'de pozitif açılar saatin tersi yönündedir! Bu yüzden saat yönü için -15 vermeliyiz.
M_rot = cv2.getRotationMatrix2D(center_coor, -15, 1.0)

# - Interpolasyon yöntemini cv2.INTER_LINEAR ayarlayarak döndürme işlemini (warpAffine) uygulayalım.
final_img = cv2.warpAffine(masked_img, M_rot, (cols, rows), flags = cv2.INTER_LINEAR)

# 5. Elde ettiğiniz matrisi (ve işlem adımlarını) ekranda gösterin.
cv2.imshow('1. Orijinal Goruntu', car_img)
cv2.imshow('2. Siyah-Beyaz Maske', maske)
cv2.imshow('3. Maskelenmis (Odak) Goruntu', masked_img)
cv2.imshow('4. Maskeli ve Dondurulmus (Sonuc)', final_img)

cv2.waitKey(0)
cv2.destroyAllWindows()