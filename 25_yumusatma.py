import cv2
import numpy as np

img = cv2.imread("images/gurultulu_lena.png")

# 1. Kutu (Ortalama) Filtre
kutu = cv2.blur(img , (7, 7))
# 2. Gauss Filtre
gauss = cv2.GaussianBlur(img , (7, 7) , 0)
# 3. Medyan Filtre
medyan = cv2.medianBlur(img , 7) # ksize tek sayı!
# 4. Bilateral Filtre (Kenar koruyucu)
bilateral = cv2.bilateralFilter(img , 9, 75 , 75)
# 5. Özel kernel ile filtreleme
kernel = np.ones((7, 7) , np.float32) / 49
ozel = cv2.filter2D(img , -1 , kernel)

cv2.imshow("orijinal" , img)
cv2.waitKey(0)
cv2.imshow("kutu" , kutu)
cv2.waitKey(0)
cv2.imshow("gauss" , gauss)
cv2.waitKey(0)
cv2.imshow("medyan" , medyan)
cv2.waitKey(0)
cv2.imshow("bilateral" , bilateral)
cv2.waitKey(0)
cv2.imshow("ozel" , ozel)
cv2.waitKey(0)
cv2.destroyAllWindows()