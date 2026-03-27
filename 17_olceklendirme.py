import cv2

img = cv2.imread('images/lena.jpg')

# 2 kat büyütme (Bilineer interpolasyon)
buyuk = cv2.resize(img, None,
    fx=2, fy=2,
    interpolation=cv2.INTER_LINEAR)

# Yarıya küçültme
kucuk = cv2.resize(img, None,
    fx=0.5, fy=0.5,
    interpolation=cv2.INTER_AREA)

# Belirli boyuta getirme (300x200)
sabit = cv2.resize(img, (300, 200))

cv2.imshow("2 Kat Buyutme", buyuk)
cv2.waitKey(0)

cv2.imshow("Yariya Kucultme", kucuk)
cv2.waitKey(0)

cv2.imshow("Belirli boyuta getirme", sabit)
cv2.waitKey(0)

cv2.destroyAllWindows()