import numpy as np
import cv2

# 300x300 siyah (0) matris (tek kanal)
black_image = np.zeros((300, 300), dtype=np.uint8)

# Ortaya beyaz (255) kare çizme
# Y:100-200, X:100-200 arası
black_image[100:200, 100:200] = 255

cv2.imshow('Sonuc', black_image)
cv2.waitKey(0)