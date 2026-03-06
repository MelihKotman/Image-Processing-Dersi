import cv2
import numpy as np
from matplotlib import pyplot as plt
import urllib.request
import os

# Klasik "Lena" test fotoğrafını klasöre indirelim. (Bir kere yapsan yeter)
#if not os.path.exists('images/lena.jpg'):
#    url = "https://raw.githubusercontent.com/opencv/opencv/master/samples/data/lena.jpg"
#    urllib.request.urlretrieve(url, "images/lena.jpg")
#    print("Lena fotoğrafı (lena.jpg) indirildi!")

# Görüntüyü Okuma
img = cv2.imread('images/lena.jpg') # OpenCV, görüntüyü BGR formatında bir NumPy dizisine olarak okur

# Gri Tonlamaya Dönüştürme
# Görüntü işlemelerinde (özellikle filtreleme ve kenar bulmada) renkler genellikle gereksiz veridir.
gray = cv2.imread('images/lena.jpg', cv2.IMREAD_GRAYSCALE)

# Görüntü Bilgilerini Yazdırma
print(f"Görüntü Boyutu: {img.shape}") # (512, 512, 3)
print(f"Görüntü Tipi: {img.dtype}") # uint8
print(f"Toplam Piksel: {img.size}") # 786432

# BGR'den RGN Dönüşümü (Matplotlib renkleri doğru göstersin diye)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Matplotlib ile Görselleştirme
plt.imshow(img_rgb)
plt.title('İlk Görünüm - RGB')
plt.axis('off') # Ekran çizgisi (x, y koordinatları) gizlenir.
plt.show()

