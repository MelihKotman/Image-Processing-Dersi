# Altın Kural: OpenCV görüntüleri BGR okur, Matplotlib ise RGB gösterir. Bu yüzden Matplotlib'e vermeden önce ´cv2.cvtColor(img, cv2.COLOR_BGR'RGB)´ dönüşümü şarttır!
# cv2.IMREAD_COLOR -> 1 -> Renkli (BGR), alfa kanalı yok (Varsayılan)
# cv2.IMREAD_GRAYSCALE -> 0 -> Gri tonlama, tek kanal
# cv2.IMREAD_UNCHANGED -> -1 -> Orijinal (alfa kanalı dahil)

import cv2
from matplotlib import pyplot as plt

# Görüntü Oku ve Dönüştür
img = cv2.imread('images/lena.jpg')
gray = cv2.imread('images/lena.jpg', cv2.IMREAD_GRAYSCALE)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 1 satır, 3 sütundan oluşan bir figür (pencere) oluşturalım.
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 1. Grafik: Renkli Orijinal GÖrüntü (RGB'ye çevrilmiş)
axes[0].imshow(rgb)
axes[0].set_title('Renkli (RGB)')
axes[0].axis('off')

# 2. Grafik: Gri Tonlama
# Matplotlib tek kanallı renklendirir bunu engellemek için cmap = 'gray' demeliyiz!
axes[1].imshow(gray, cmap='gray')
axes[1].set_title('Gri Tonlama')
axes[1].axis('off')

# 3. Grafik: Görüntünün Histogramı (Piksel yoğunluklarının dağılımı)
# ravel() matrisi tek boyutlu diziye düzleştirir. 256 adet (0-255 arası) sütun çizeriz.
axes[2].hist(gray.ravel(), 256, [0, 256])
axes[2].set_title('Histogram')

# Grafikleri ekrana düzgün yerleştirip göster
plt.tight_layout()
plt.show()