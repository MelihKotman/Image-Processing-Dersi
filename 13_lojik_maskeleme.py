import cv2
import numpy as np

img = cv2.imread('images/lena.jpg')
y, x = img.shape[:2]

# Siyahlık (0) dolu ayni boyutta bir maske üret
mask = np.zeros((y, x), dtype=np.uint8)

# Maske ortasına BEYAZ bir daire çiz (cv2.circle)
cv2.circle(mask, (x//2, y//2), 150, 255, -1)

# AND işlemi (Resmin sadece maske altındaki kısmını tutar)
sonuc = cv2.bitwise_and(img, img, mask=mask)

# Renkleri/Parlaklıkları tersleme (Negative image)
negatif = cv2.bitwise_not(img)

cv2.imshow("AND Islemi", sonuc)
cv2.waitKey(0)

cv2.imshow("Negatif Islemi", negatif)
cv2.waitKey(0)

cv2.destroyAllWindows()