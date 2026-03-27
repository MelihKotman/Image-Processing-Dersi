import cv2

sonraki_kare = cv2.imread('images/zaman2.jpeg', 0)
onceki_kare = cv2.imread('images/zaman1.jpeg', 0)

# cv2.subtract kullanması negatifleri 0 yapar (saturation)
fark = cv2.subtract(sonraki_kare, onceki_kare)

# Eger mutlak (absolute) fark istersek daha etkilidir:
mutlak_fark = cv2.absdiff(sonraki_kare, onceki_kare)

# Elde edilen fark görselini eşikleyerek 'hareket maskesi' bul
# Parlaklığı 30'dan büyük farkları tamamen beyaz (255) yap
_, hareket = cv2.threshold(mutlak_fark, 30, 255, cv2.THRESH_BINARY)
cv2.imshow("Hareket Algilandi", hareket)
cv2.waitKey(0)
cv2.destroyAllWindows()