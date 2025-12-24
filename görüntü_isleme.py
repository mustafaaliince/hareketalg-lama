import cv2
import time

kamera_id = 0 
cap = cv2.VideoCapture(kamera_id, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("HATA: Kamera açılamadı! Lütfen 'kamera_id' değerini 1 yapıp dene.")
    print("Ayrıca başka bir programın (Zoom, Teams) kamerayı kullanmadığından emin ol.")
    exit()

print("Hareket Sensörü Başlatıldı... Çıkmak için 'q' tuşuna bas.")

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    
    dilated = cv2.dilate(thresh, None, iterations=3)
    
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
        (x, y, w, h) = cv2.boundingRect(contour)
        
        if cv2.contourArea(contour) < 900:
            continue
            
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame1, "Hareket Algilandi", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    cv2.imshow("Guvenlik Kamerasi", frame1)
    
    frame1 = frame2
    ret, frame2 = cap.read()
    
    if not ret:
        break

    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("Program sonlandırıldı.")
