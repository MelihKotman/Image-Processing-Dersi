import cv2
import numpy as np

img = cv2.imread('images/masadaki_kagit.png')

cv2.imshow("Goruntu", img)
cv2.waitKey(0)

# Kağıdın köşe noktaları (SolÜst, SağÜst, SolAlt, SağAlt) (Kaynak)
pts1 = np.float32([[51,31],  [877,41], [10,508], [950,508]])

# Düz kağıdın olmasını istediğimiz hedefleri (A4 yapısı, max genişlik)
pts2 = np.float32([[0,0],   [300,0],  [0,300],  [300,300]])

# Perspektif matrisi (M) üretiliyor
M_persp = cv2.getPerspectiveTransform(pts1, pts2)

# Fotoğrafa uygula!
perspektif_duzeltilmis = cv2.warpPerspective(img, M_persp, (300, 300))

cv2.imshow('Tarayici Gorunumu', perspektif_duzeltilmis)
cv2.waitKey(0)

cv2.destroyAllWindows()