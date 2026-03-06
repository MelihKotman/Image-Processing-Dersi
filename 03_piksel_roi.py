import cv2
import numpy as np

img = cv2.imread('images/lena.jpg')

# A. Piksel Erişimi ve Değiştirme

# (100. satır ve 200. sütun) konumundaki pikselin BGR değerlerini alma

piksel = img[100, 200]
print(f"Piksel (100, 200) BGR değerleri: {piksel}")

# Sadece Mavi (Blue) kanalına erişim (0: Mavi, 1: Yeşil, 2: Kırmızı)
mavi_deger = img[100, 200, 0]

# O pikseli tamamen beyaz (255, 255, 255) yapma
img[100, 200] = [255, 255 ,255]

# B. ROI (Region of Interest - İlgi Bölgesi)
# ROI, görüntünün sadece ilgilendiğimiz bir kısmını (örneğin sadece yüzü) kesip almaktır.
# Kullanımı: img[y_baslangic:y_bitis, x_baslangic:x_bitis]

roi = img[50:200, 100:300] # Görüntüden dikdörtgen bir parça kopardık.

# Kopardığımız bu parçayı, görüntünün sol üst köşesine (0:150, 0:200 aralığına) yapıştıralım.
# Not: Kesilen parça (150x200) ile yapıştırılacak alanın boyutu tam olarak aynı olmalıdır!
img[0:150, 0:200] = roi

# C. Kanalları Ayırma ve Birleştirme
# Görüntüyü B, G ve R oalrak 3 ayrı matrise bölme
b, g, r = cv2.split(img)

# Ayrılan kanalları tekrar tek bir renkli görüntü haline getirme
birlesik_img = cv2.merge([b, g, r])

# Sonucu görelim
cv2.imshow('ROI Isleminden Sonra', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
