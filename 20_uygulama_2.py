import cv2
import numpy as np
from matplotlib import pyplot as plt

# 1. Numpy ile tamamen rastgele sayı (noise/gürültü) içeren 300x300 iki farklı matris tanımlayalım
# dtype=np.uint8 olması çok önemlidir, çünkü görüntü pikselleri 0-255 arası tam sayılardır.
img1_noise = np.random.randint(0, 256, (300, 300), dtype=np.uint8)
img2_noise = np.random.randint(0, 256, (300, 300), dtype=np.uint8)

# 2. Bu iki rastgele matrisi OpenCV formülü ile birbirinden çıkaralım (Mutlak Fark)
# cv2.absdiff, negatif değerleri önler ve değişimin şiddetini gösterir.
fark_matrisi = cv2.absdiff(img1_noise, img2_noise) #

# 3. Farkları ekrana matplotlib ile yazdıralım (Slayt 21'deki pratikten faydalanarak)
fig, axes = plt.subplots(1, 3, figsize=(17, 5))

axes[0].imshow(img1_noise, cmap='gray')
axes[0].set_title('Zaman 1 (Rastgele Matris)')
axes[0].axis('off')

axes[1].imshow(img2_noise, cmap='gray')
axes[1].set_title('Zaman 2 (Rastgele Matris)')
axes[1].axis('off')

axes[2].imshow(fark_matrisi, cmap='gray')
axes[2].set_title('Mutlak Fark (absdiff)')
axes[2].axis('off')

plt.tight_layout()
plt.show()