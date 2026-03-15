# Matriste (NumPy Array) Slicing Operasyonu
# roi = img[y1:y2, x1:x2]
import cv2

img = cv2.imread('images/lena.jpg')

# Satırlarda (Y Ekseni) 50'den 200'e
# Sütunlarda (X Ekseni) 100'den 300'e kadar olan dikdörtgeni kes!
roi = img[50:200, 100:300]

cv2.imshow('Ilgi Alanı (ROI)', roi)
cv2.waitKey(1500)

# Aynı boyutta başka bir bölgeye yapıştırabiliriz
img[0:150, 0:200] = roi

cv2.imshow('Guncellenmis Goruntu', img)
cv2.waitKey(3000)
cv2.destroyAllWindows()