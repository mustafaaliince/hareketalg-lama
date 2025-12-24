🛡️ Hareket Algılayan Güvenlik Kamerası (OpenCV)
Bu proje, Python ve OpenCV kütüphanesi kullanılarak geliştirilmiş, gerçek zamanlı hareket algılama yeteneğine sahip bir güvenlik kamerası simülasyonudur. Bilgisayarın kamerasından alınan iki kare arasındaki farkı analiz ederek hareket eden nesneleri tespit eder ve bunları görsel olarak işaretler.

🚀 Özellikler
Gerçek Zamanlı Tespit: Kamera görüntüsünü anlık olarak işler.

Gürültü Filtreleme: Gaussian Blur kullanarak görüntüdeki küçük parazitleri temizler.

Dinamik Eşikleme: Hareketli nesneleri net bir şekilde ayırmak için ikili eşikleme (thresholding) uygular.

Görsel Bildirim: Hareket algılandığında nesne etrafına yeşil çerçeve çizer ve ekranda uyarı metni gösterir.

🛠️ Kurulum
Bu projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

Depoyu Klonlayın:

Bash

git clone https://github.com/kullanici-adiniz/proje-adinizi-buraya-yazin.git
cd proje-adinizi-buraya-yazin
Gerekli Kütüphaneleri Yükleyin: Sadece OpenCV kütüphanesine ihtiyacınız vardır:

Bash

pip install opencv-python
💻 Kullanım
Programı çalıştırmak için terminale şu komutu yazın:

Bash

python main.py
Program açıldığında kamera görüntüsü pencerede belirecektir.

Çıkış yapmak için klavyeden 'q' tuşuna basmanız yeterlidir.

⚙️ Teknik Çalışma Mantığı
Kod, temelde şu görüntü işleme adımlarını takip eder:

Frame Differencing: Ardışık iki kare arasındaki mutlak fark (cv2.absdiff) alınır.

Grayscale & Blur: Renk detayları atılarak görüntü gri tona çevrilir ve yumuşatılarak hatalı tespitler engellenir.

Thresholding & Dilation: Farklar belirginleştirilir ve boşluklar doldurulur.

Contour Detection: Belirginleşen farkların koordinatları (konturları) bulunur.

Area Filter: Çok küçük hareketlerin (ışık değişimi vb.) kutulanmaması için bir alan filtresi uygulanır.

📝 Notlar
Eğer kameranız açılmazsa kod içerisindeki kamera_id = 0 değerini 1 yaparak tekrar deneyebilirsiniz.

Işık değişimlerine karşı hassasiyeti ayarlamak için cv2.threshold içerisindeki 20 değerini değiştirebilirsiniz.
