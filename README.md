# image_processing_maze_solve

oluşturduğumuz sistem bir görüntü üzerinde bazı görüntü işleme tekniklerini kullanarak bir labirentin çözülmesini gerçekleştirir. 
oluşturduğumuz sistemimiz labirentin boş kanallarını doldurarak sürekli çıkışı arar ve her çıkışı bulamadığını izlediği yolun sonuna bir kontür atarak çıkışları bulup sonuca ulaşır. En sonunda çıkışa ait doğru sonucu bulduğunda izlediği yolu renklendirerek sonucu gösterir.
yaptığımız işlemlere ait kodların amaçları adım adım aşağıda verilmiştir:

1. Görüntünün yüklenmesi:
   - "cv2.imread" fonksiyonuyla görüntü dosyası okunur.

2. Gri tonlamaya dönüştürme:
   - "cv2.cvtColor" fonksiyonuyla renkli görüntü, gri tonlamalı görüntüye dönüştürülür.

3. Eşikleme:
   - "cv2.threshold" fonksiyonuyla gri tonlamalı görüntü eşiklenir ve siyah-beyaz ikili bir görüntü elde edilir.

4. Konturların bulunması:
   - "cv2.findContours" fonksiyonuyla eşiklenmiş görüntüdeki konturlar bulunur.

5. Konturların çizdirilmesi:
   - "cv2.drawContours" fonksiyonuyla konturlar, görüntü üzerine çizdirilir.

6. İkinci konturun çizdirilmesi:
   - İlk konturun üzerine birinci kontur çizdirilir.

7. İkinci eşikleme:
   - İkinci konturların çizildiği görüntü, belirli bir eşik değeriyle eşiklenir.

8. Genişleme:
   - Labirentin genişlemesini sağlamak için "cv2.dilate" fonksiyonu kullanılır.

9. Seyreltme:
   - Genişlemiş labirentin daraltılması için "cv2.erode" fonksiyonu kullanılır.

10. Fark hesaplama:
    - "diff = cv2.absdiff(genisleme, seyreltme)" 
      komutu ile Genişleme ve seyreltme sonucu elde edilen görüntüler arasındaki fark hesaplanır.

11. Maske oluşturma:
    - "b, g, r = cv2.split(img)
      mask_inv = cv2.bitwise_not(diff)"
      Fark görüntüsünün tersini alarak bir maske oluşturulur.
      ardından Maske kullanılarak renk kanalları maskelenir ve giriş görüntünün renk kanalları ayrılır.

14. Sonuç görüntüsünün oluşturulması:
    - Maskelenmiş renk kanalları birleştirilerek çözülmüş labirentin sonuç görüntüsü elde edilir.

aldığımız sonuç çıktısı aşağıda paylaşılmıştır.

![çıktı](https://github.com/aylanckerem/image_processing_maze_solve/assets/96474969/d51be28f-81aa-4828-ac92-37dab80eaa1c)
