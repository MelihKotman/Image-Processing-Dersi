import cv2

# Görüntüyü Okuma
img = cv2.imread('images/lena.jpg')

# Normal Görüntüleme
cv2.imshow('Orijinal boyutu', img)

# Boyutlandırılabilir Pencere ile Görüntüleme
cv2.namedWindow('Buyuk Resim', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Buyuk Resim', 800, 600)
cv2.imshow('Buyuk Resim', img)

# Ekranda kalması için tuşa basılmasını bekle ve sonra pencereyi kapat
cv2.waitKey(0)
cv2.destroyAllWindows()

# Görüntüyü Kaydetme (Farklı formatlar ve kaliteler)
cv2.imwrite('images/lena-copy.png', img) # Standard PNG kaydı

# JPEG için kalite ayarı (0-100 arası, 95 yüksek kalite)
cv2.imwrite('images/lena-copy-high-quality.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 95])

# PNG için sıkıştırma seviyesi (0-9 arası, 9 en çok sıkıştırma)
cv2.imwrite('images/lena-compressed.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 9])

