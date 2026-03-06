import cv2

# 0 numaralı cihaz varsayılan kamerandır.
# Eğer harici bir USB kamera takarsan burayı 1 yapabilirsin.
cap = cv2.VideoCapture(0)

# Kamera açık olduğu sürece dönecek döngü
while True:
    # Kameradan anlık olarak bir kare oku.
    # 'ret' okumanın başarılı olup olmadığını (True/False) döndürür.
    # 'frame' ise o anki fotoğraf matrisidir.
    ret, frame = cap.read()

    if not ret:
        print("Kameradan görüntü alınamadı.")
        break

    # Okunan kareyi anlık gri tonlamaya çevirelim.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Pencerelerde göster
    cv2.imshow('Kamera (Renkli)', frame)
    cv2.imshow('Kamera (Gri)', gray)

    # Çıkış Mekanizması:
    # cvt.waitKey(1), her döngüde 1 milisaniye klavyeden tuşa basılmasını bekler.
    # Eğer basılan tuş 'q' (quit) ise döngüyü kır.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Döngü kırıldıktan sonra donanımı serbest bırak ve pencereleri kapat.
cap.release()
cv2.destroyAllWindows()