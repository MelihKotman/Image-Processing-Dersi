import cv2
import numpy as np

# 1. Basit bir 8x8 matris oluşturalım (0: Arka plan, 1: Nesneler)
# Bu örnekte çapraz duran pikseller var.
matris = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
], dtype=np.uint8)

# 2. 4-Bitişiklik (4-Connectivity) ile nesneleri bul
# Çapraz duran pikselleri BİRBİRİNE BAĞLI KABUL ETMEZ, ayrı nesneler sanır.
num_labels_4, labels_4 = cv2.connectedComponents(matris, connectivity=4)

# 3. 8-Bitişiklik (8-Connectivity) ile nesneleri bul
# Çapraz duran pikselleri BİRBİRİNE BAĞLI KABUL EDER, tek bir nesne olarak sayar.
num_labels_8, labels_8 = cv2.connectedComponents(matris, connectivity=8)

# Çıktıları görelim
print("--- Orijinal Matris ---")
print(matris)

# Arka plan da (0) bir etiket sayıldığı için nesne sayısını bulurken 1 çıkarıyoruz.
print(f"\n4-Bitişiklik Algoritması {num_labels_4 - 1} farklı nesne buldu.")
print(f"8-Bitişiklik Algoritması {num_labels_8 - 1} farklı nesne buldu.")