import cv2, numpy as np
from matplotlib import pyplot as plt

# 1. Gürültülü bir fotoğraf edinin veya yapay gürültü ekleyeniz.
img = cv2.imread('image/lena.jpg', 0)
noisy = img.copy()
prob = 0.05
noisy[np.random.random(img.shape) < prob] = 255
noisy[np.random.random(img.shape) < prob] = 0

# 2. Kutu, Gauss, Medyan ve Bilateral filtreleri kullanarak gürültüyü azaltın.
kutu   = cv2.blur(noisy, (5, 5))
gauss  = cv2.GaussianBlur(noisy, (5, 5), 0)
medyan = cv2.medianBlur(noisy, 5)
bilat  = cv2.bilateralFilter(noisy, 9, 75, 75)

titles = ['Gürültülü','Kutu','Gauss','Medyan','Bilateral']
images = [noisy, kutu, gauss, medyan, bilat]
fig, axes = plt.subplots(1,5, figsize=(24, 4))
for ax,im,t in zip(axes,images,titles):
    ax.imshow(im, cmap='gray'); ax.set_title(t); ax.axis('off')
plt.tight_layout(); plt.show()

# 3. Sobel ve Laplacian kenar haritalarını karşılaştırınız.
laplacian = cv2.Laplacian(noisy, cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))

sobelx = cv2.Sobel(noisy, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(sobelx, cv2.CV_64F, 0, 1, ksize=3)
sobel_mag = cv2.magnitude(sobelx, sobely)

titles = ['Laplacian','Sobel']
images = [laplacian, sobely]
fig, axes = plt.subplots(1,2, figsize=(10,5))
for ax,im,t in zip(axes,images,titles):
    ax.imshow(im, cmap='gray'); ax.set_title(t); ax.axis('off')
plt.tight_layout(); plt.show()

# 4. "Hangi filtre gürültüyü daha iyi azaltıyor?" sorusunu cevaplayınız.
"""
Medyan filtresi içlerinde en iyi sonucu verdi. Kutu ve Gauss filtreleri gürültüyü azaltırken aynı zamanda görüntüyü de bulanıklaştırdı. Bilateral filtre ise gürültüyü azaltırken kenarları korumaya çalıştı ancak medyan kadar etkili olmadı.

Laplacian kenar haritası, gürültülü görüntüde çok fazla gürültü içerirken, Sobel kenar haritası daha temiz ve belirgin kenarlar gösterdi. Bu da Sobel filtresinin gürültülü görüntülerde daha iyi performans gösterdiğini gösteriyor.
"""