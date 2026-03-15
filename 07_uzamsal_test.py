# INTER_NEAREST metodu, komşu pikselleri yapay zeka/yumuşatma ile doldurmasını engeller. Tam olarak pikselleşmeyi (bloklaşmayı) verir.

import cv2
import numpy as np
import time

# Farklı IMREAD modlarında boyutlar değişir!

# 1. Renkli (3 Kanal - M x N x 3 matris)
img_color = cv2.imread('images/lena.jpg', cv2.IMREAD_COLOR)

# 2. Gri Tonlama (Tek Kanal - M x N matris)
img_gray = cv2.imread('images/lena.jpg', cv2.IMREAD_GRAYSCALE)

# Uzamsal çözünürlük etkisi (Alt Örnekleme / Downsampling)

# 1- 0.125 Ölçek
# Çözünürlüğü bilerek küçült (örnekleme sıklığını düşürür)
kucuk = cv2.resize(img_gray, None, fx= 0.125, fy= 0.125,
                       interpolation=cv2.INTER_NEAREST)
    
# Aynı görsel boyutta görmek için tekrar yapay olarak büyüt (pikselleşmeyi gösterir)
buyuk = cv2.resize(kucuk, img_gray.shape[::-1],
                       interpolation= cv2.INTER_NEAREST)
    
cv2.imshow('Olcek 0.125', buyuk)
cv2.waitKey()

# 2- 0.25 Ölçek
# Çözünürlüğü bilerek küçült (örnekleme sıklığını düşürür)
kucuk = cv2.resize(img_gray, None, fx= 0.25, fy= 0.25,
                       interpolation=cv2.INTER_NEAREST)
    
# Aynı görsel boyutta görmek için tekrar yapay olarak büyüt (pikselleşmeyi gösterir)
buyuk = cv2.resize(kucuk, img_gray.shape[::-1],
                       interpolation= cv2.INTER_NEAREST)

cv2.imshow('Olcek 0.25', buyuk)
cv2.waitKey()

# 3- 0.5 Ölçek
# Çözünürlüğü bilerek küçült (örnekleme sıklığını düşürür)
kucuk = cv2.resize(img_gray, None, fx= 0.5, fy= 0.5,
                       interpolation=cv2.INTER_NEAREST)
    
# Aynı görsel boyutta görmek için tekrar yapay olarak büyüt (pikselleşmeyi gösterir)
buyuk = cv2.resize(kucuk, img_gray.shape[::-1],
                       interpolation= cv2.INTER_NEAREST)
    
cv2.imshow('Olcek 0.5', buyuk)
cv2.waitKey()

# 4- 1 Ölçek
# Çözünürlüğü bilerek küçült (örnekleme sıklığını düşürür)
kucuk = cv2.resize(img_gray, None, fx= 1, fy= 1,
                       interpolation=cv2.INTER_NEAREST)
    
# Aynı görsel boyutta görmek için tekrar yapay olarak büyüt (pikselleşmeyi gösterir)
buyuk = cv2.resize(kucuk, img_gray.shape[::-1],
                       interpolation= cv2.INTER_NEAREST)
    
cv2.imshow('Olcek 1', buyuk)
cv2.waitKey()
