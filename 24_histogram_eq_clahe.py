import cv2
from matplotlib import pyplot as plt

img = cv2.imread('images/sisli_gece.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Sisli Gece", gray)
cv2.waitKey(0)

# 1. Histogram İstatistikleri (Matplotlib veya OpenCV)
hist_data = cv2.calcHist([gray], [0], None, [256], [0, 256])
# Kolayı: plt.hist(gray.ravel(), bins=256, range=[0, 256]) 

# 2. Global Histogram Eşitleme (Zararlı olabilir)
global_eq = cv2.equalizeHist(gray)

# 3. CLAHE (Modern Sektör Standardı - Gürültü Koruyucu)
# clipLimit: Tıraşlanacak max frekans. tileGridSize: lokal fayans matris
clahe_obj = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(8, 8))
clahe_img = clahe_obj.apply(gray)

cv2.imshow('CLAHE (Mucize!)', clahe_img)
cv2.waitKey(0)