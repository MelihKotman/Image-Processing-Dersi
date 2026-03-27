import cv2

img1 = cv2.imread('images/landscape.png')
img2 = cv2.imread('images/landscape2.png')


# Doygunluklu (Saturated) Toplama [Maksimum 255 ile sınırlar]
toplam = cv2.add(img1, img2)

# Ağırlıklı Toplama / Blending (Alpha: 0.7, Beta: 0.3)
karisim1 = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

# Ağırlıklı Toplama / Blending (Alpha: 0.2, Beta: 0.8)
karisim2 = cv2.addWeighted(img1, 0.2, img2, 0.8, 0)


cv2.imshow("Doygunluklu toplama", toplam)
cv2.waitKey(0)

cv2.imshow("Agirlikli toplama (img1 agirlikli)",karisim1)
cv2.waitKey(0)

cv2.imshow("Agirlikli toplama (img2 agirlikli)",karisim2)
cv2.waitKey(0)

cv2.destroyAllWindows()