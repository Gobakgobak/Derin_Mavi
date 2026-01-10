import cv2

# 1. Kamera Erişimi
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kamera açılmadı!")
    exit()

while True:
    # Görüntüyü oku
    ret, frame = cap.read()
    if not ret:
        break

    # 2. Görüntü Boyutlarını Otomatik Anlama
    height, width, _ = frame.shape

    # 3. Matematiksel Hesaplama (Merkezdeki 200x200'lük alan)
    # Merkezin koordinatlarını bulup 100px sağa/sola, yukarı/aşağı gidiyoruz
    x_start = (width // 2) - 100
    y_start = (height // 2) - 100
    x_end = x_start + 200
    y_end = y_start + 200

    # 4. Bölgesel İşleme (ROI)
    # Belirlenen alanı kes
    roi = frame[y_start:y_end, x_start:x_end]

    # Bu alanı siyah-beyaz (grayscale) yap
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    # İPUCU: Gri alanı tekrar renkli (BGR) formata çevir (Kanal sayısını 3 yapmak için)
    # Bu işlem görüntüyü renklendirmez, sadece 3 kanallı "gri" bir resim yapar.
    gray_roi_3_channel = cv2.cvtColor(gray_roi, cv2.COLOR_GRAY2BGR)

    # İşlenmiş alanı orijinal görüntünün üzerine yerleştir
    frame[y_start:y_end, x_start:x_end] = gray_roi_3_channel

    # Görselleştirme için dikdörtgen çizelim (isteğe bağlı, örnekte kırmızı kutu var)
    cv2.rectangle(frame, (x_start, y_start), (x_end, y_end), (0, 0, 255), 2)
    cv2.putText(frame, "Filtre: Gray", (x_start, y_start - 10), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # 5. Görselleştirme
    cv2.imshow('Derin Mavi ROI Odevi', frame)

    # 'q' tuşuna basıldığında çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Temizlik
cap.release()
cv2.destroyAllWindows()
