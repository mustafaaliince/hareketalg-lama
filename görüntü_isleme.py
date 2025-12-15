import cv2
import time

# 1. AYARLAR
# Windows'ta kameranın hızlı açılması için cv2.CAP_DSHOW ekliyoruz.
# Eğer harici kamera kullanıyorsan 0 yerine 1 yazman gerekebilir.
kamera_id = 0 
cap = cv2.VideoCapture(kamera_id, cv2.CAP_DSHOW)

# Kamera açıldı mı kontrol et
if not cap.isOpened():
    print("HATA: Kamera açılamadı! Lütfen 'kamera_id' değerini 1 yapıp dene.")
    print("Ayrıca başka bir programın (Zoom, Teams) kamerayı kullanmadığından emin ol.")
    exit()

print("Hareket Sensörü Başlatıldı... Çıkmak için 'q' tuşuna bas.")

# İlk iki kareyi okuyoruz (karşılaştırma yapmak için)
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    # İki kare arasındaki farkı bul
    diff = cv2.absdiff(frame1, frame2)
    
    # Görüntüyü gri tona çevir (işlem kolaylığı için)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    
    # Gürültüyü azaltmak için bulanıklaştır
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Eşik değeri belirle (Hareketi netleştir)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    
    # Çizgileri kalınlaştır (Daha net algılama için)
    dilated = cv2.dilate(thresh, None, iterations=3)
    
    # Konturları (hatları) bul
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Her bir hareket için kutu çiz
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        
        # Çok küçük hareketleri görmezden gel (rüzgar, ışık titremesi vs.)
        if cv2.contourArea(contour) < 900:
            continue
            
        # Hareket eden nesnenin etrafına yeşil kutu çiz
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame1, "Hareket Algilandi", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Sonucu ekranda göster
    cv2.imshow("Guvenlik Kamerasi", frame1)
    
    # Döngü için kareleri kaydır
    frame1 = frame2
    ret, frame2 = cap.read()
    
    # Görüntü alınamazsa döngüyü kır
    if not ret:
        break

    # 'q' tuşuna basılırsa çık
    if cv2.waitKey(10) == ord('q'):
        break

# Temizlik
cap.release()
cv2.destroyAllWindows()
print("Program sonlandırıldı.")