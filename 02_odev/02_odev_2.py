import cv2
import numpy as np

# Yan veya hafif eğik çekilmiş vesikalık/portre fotoğrafını oku
img_profile = cv2.imread('image/yan_profil.jpeg')

rows, cols = img_profile.shape[:2]
center = (cols // 2, rows // 2)

# Fotoğrafı düzeltmek için gereken açıyı belirleyelim.
# Genel olarak deneme yanılma yöntemi veya bazı algoritmalarla belirlenebilirmiş.
angle = -14

# Döndürme matrisini oluşturalım.
rot_mat = cv2.getRotationMatrix2D(center, angle, 1.0)

# Görüntüyü döndürerek düzelt.
# Interpolasyonu siyah köşeler oluşmasın ve daha pürüzsüz olsun diye al
corrected_face = cv2.warpAffine(img_profile, rot_mat, (cols, rows), flags = cv2.INTER_LINEAR)

cv2.imshow("Egik Profil", img_profile)
cv2.waitKey(0)

cv2.imshow("Hizalanmis Yuz", corrected_face)
cv2.waitKey(0)

cv2.destroyAllWindows()