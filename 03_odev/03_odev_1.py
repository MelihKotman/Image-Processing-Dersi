import cv2
import numpy as np
from matplotlib import pyplot as plt

# 1. İnternetten tıbbi bir röntgen (X-Ray) indirin. Görüntü matris boyutunu Numpy ile printleyin.
imgX = cv2.imread("image/x-ray.png", 0)

cv2.imshow("X-Ray", imgX)
cv2.waitKey(0)

print(f"X-Ray'in matris boyutu {imgX.shape}")

# 2. Görüntüye hem standart global `cv2.equalizeHist()` uygulayın, hem de el ile matematiksel Logaritmik Dönüşüm Numpy Matris Operasyonu (s = clog(1 + r)) filtresini kodlayarak uygulayın.

global_eq_imgX = cv2.equalizeHist(imgX)

print(f" Global Histogram Eşitleme Kullanılmış\n{global_eq_imgX}")

c = 255 / np.log(1 + np.max(imgX))
log_img = c * (np.log(imgX.astype(np.float64) + 1))
log_img = np.array(log_img, dtype=np.uint8)

# 3. CLAHE işlemi uygulayınız.

clahe_objX = cv2.createCLAHE(clipLimit = 2.0, tileGridSize=(8, 8))
clahe_imgX = clahe_objX.apply(imgX)

# 4. Matplotlib kütüphanesinin `subplots` alanını kullanarak 1 Satır, 4 Sütunlu bir çıktı (Orijinal, Log, GlobalEQ, CLAHE) elde ediniz.
fig, axes = plt.subplots(1, 4, figsize = (20, 5))

axes[0].imshow(imgX, cmap = 'gray')
axes[0].set_title('1. Orijinal X-Ray')
axes[0].axis('off')

axes[1].imshow(global_eq_imgX, cmap = 'gray')
axes[1].set_title('2. Global Histogram Esitlemeli X-Ray')
axes[1].axis('off')

axes[2].imshow(log_img, cmap = 'gray')
axes[2].set_title('3. Logaritmik Donusum Uygulanmis X-Ray')
axes[2].axis('off')

axes[3].imshow(clahe_imgX, cmap = 'gray')
axes[3].set_title('4. CLAHE X-Ray')
axes[3].axis('off')

plt.tight_layout()
plt.show()
                
cv2.destroyAllWindows()

"""
Notebook Raporu: Algoritma Analizi ve Teorik Altyapı

Logaritmik Dönüşümde siyah arka plana ne oldu? Neden "Yıkandı" (Washed-out)?
Görseline baktığımızda siyah arka planın Logaritmik Dönüşüm (3. Görsel) uygulandığında tamamen yok olduğunu, bembeyaz/açık gri bir sise dönüştüğünü ("washed-out" olduğunu) çok net görüyoruz.

Teorik Altyapısı: Logaritmik formül olan s=c⋅log(1+r) yapısı gereği, karanlık (düşük r) değerlerini çok agresif bir şekilde yukarı (aydınlığa) çeker. X-Ray görüntüsünde devasa bir alan kaplayan simsiyah arka plan (0'a yakın pikseller), logaritma eğrisinin o ilk dik yokuşuna denk geldiği için anında parlatılmıştır. Logaritmik dönüşüm tıbbi görüntülerde her zaman işe yaramaz; bu örnekte kemik detaylarını ortaya çıkarmak yerine tüm resmi bir sis bulutuna boğmuştur.

2. Hangi yöntem daha fazla gürültü (Noise) üretti ve teorisi nedir?
En fazla sert gürültüyü ve kaba (grainy) görünümü Global Histogram Eşitleme (2. Görsel) üretmiştir. Dikkat edersek kemiklerin çevresindeki dokular ve siyah arka planın sınırları çok sert ve kumlu bir yapıya bürünmüş haldedir.

Teorik Altyapısı: Global eşitleme, resmi yaymak için Kümülatif Dağılım Fonksiyonunu (CDF) kullanır. Bu X-Ray görüntüsünde siyah/koyu gri piksellerin sayısı (frekansı) devasa boyutlardadır. Histogramda bu kadar büyük bir yığılma olduğunda, CDF grafiği aniden çok dik bir tırmanış yapar.

Sonuç: Eğri çok dik olduğu için, orijinal karanlık bölgedeki gözle görülmeyen minik bir sensör gürültüsü (örneğin 5 ile 7 arasındaki 2 birimlik fark), eşitlendikten sonra devasa bir farka (örneğin 20 ile 90 arasına) gerilerek uzatılır. Görünmez gürültüler, devasa kontrast farkları olarak gözümüze batar (Noise Amplification).

3. Kazanan Neden CLAHE (4. Görsel) Oldu?
CLAHE (4. görsele) baktığımızda kemikler (kaburgalar) muazzam belirginleşmiş, akciğer dokusu detaylanmış ama 2. görseldeki o "kumlu/sert" gürültü oluşmamıştır.

Nedeni: CLAHE, resmi 8×8 ızgaralara bölerek lokal çalıştı ve en önemlisi verdiğin clipLimit (Kontrast Sınırı) sayesinde histogramdaki o devasa sivri tepeleri (siyah yığılmalarını) tıraşladı. CDF eğrisinin aniden dikleşmesine izin vermediği için gürültü patlamasını engelledi.
"""