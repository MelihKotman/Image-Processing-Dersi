import cv2, numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/lena.jpg', 0)
noisy = img.copy()
prob = 0.04
noisy[np.random.random(img.shape) < prob] = 255
noisy[np.random.random(img.shape) < prob] = 0

kutu   = cv2.blur(noisy, (5,5))
gauss  = cv2.GaussianBlur(noisy, (5,5), 0)
medyan = cv2.medianBlur(noisy, 5)
bilat  = cv2.bilateralFilter(noisy, 9, 75, 75)

titles = ['Gürültülü','Kutu','Gauss','Medyan','Bilateral']
images = [noisy, kutu, gauss, medyan, bilat]
fig, axes = plt.subplots(1,5, figsize=(24,4))
for ax,im,t in zip(axes,images,titles):
    ax.imshow(im, cmap='gray'); ax.set_title(t); ax.axis('off')
plt.tight_layout(); plt.show()