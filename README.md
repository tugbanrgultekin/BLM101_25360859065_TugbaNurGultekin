# BLM101_25360859065_TugbaNurGultekin
- *Ad/Soyad: Tuğba Nur Gültekin*
- *Numara: 25360859065*
- *Bölüm: Bilgisayar Mühendisliği*
- *Ders: Bilgisayar Mühendisliğine Giriş* 
- *Öğretim Üyesi: Prof. Dr. Turgay Tugay Bilgin*
- *Proje Konusu: Veri Depolama ve Sayısal Sistemler (1. Proje)*
# KOD AÇIKLAMASI
## Projenin Amacı
 Bu projede Python programlama dili kullanılarak, kullanıcının girdiği onluk tabandaki bir sayıyı ikilik (binary) veya onaltılık (hexadecimal) tabana dönüştüren bir hesap makinesi geliştirilmiştir.
 Proje hazırlanışında Python'un hazır 'bin()' ve 'hex()' fonksiyonları kullanılmamıştır. Taban dönüşümü işlemleri tamamen matematiksel döngüler ile ifade edilmiştir. Ek olarak dönüştürülen sayının bellekte kaç bitlik alan kapladığı ve sayının bellekte nasıl saklandığı kod çıktısı olarak kullanıcıya gösterilebilmektedir.
 ## Kullanılan Kütüphaneler
 Bu projede herhangi bir harici kütüphane kullanılmamıştır. Python'un zaten içerisinde bulunan 'input(), print(), abs(), len()' gibi yerleşik fonksiyonlar yeterli olmuştur. Bu nedenle kodu şahsi cihazınızda çalıştırmak için ek bir kurulum gerekmemektedir.
 ## Program Çalışma Mantığı
 - Program çalıştığında öncelikle kullanıcıdan onluk tabanda bir sayı girilmesi istenir. 
 - Girilen sayı pozitif veya negatif olabilir. 
 - Daha sonra kullanıcıya iki seçenek sunulur.
    1. İkilik Tabana Dönüştürme 
    2. Onaltılık Tabana Dönüştürme
 - Seçim sonucu ikilik (binary), onaltılık (hexadecimal) dönüşüm değeri, bellekte saklanması iki'nin tümleyeni (two's complement) şeklinde, kaç bitlik kutucuklar halinde saklandığı gösterilir.
 ## Taban Dönüştürme Algoritması
 1. Sayı hedef tabana tamsayı bölmesi ile bölünür.
 2. Bölme işleminde kalan değer bulunur.
 3. Kalan değer, yeni tabandaki basamak değerini temsil eder.
 4. Bu işlem sayı 0 (sıfır) olana kadar devam eder.
 5. Bulunan kalanlar tersten okunarak sonuç oluşturulur.
 Onaltılık taban dönüşümünde 10-15 arası değerler 'A,B,C,D,E,F' karakterleri ile gösterilir.
 ## Bellekte Kapladığı Alan Algoritması
 - İki'nin tümleyeni, bilgisayarlarda negatif sayıların ikilik bellekte gösterilmesi için kullanılan yöntemdir.
 - Algoritma sabit bit uzunluğu kullanılarak uygulanır.(4,8,16,32)
 - İlk adımda ikilik sayının tüm bitleri ters çevirilir:
    - 0->1
    - 1->0
 - Bu işlem sonucunda sayının bir'in tümleyeni elde edilir.
 - İkinci adımda terslenmiş sayıya ikilik düzende 1 eklenir.
 - Toplama işlemi en sağ bitten sola doğru, elde mantığıyla yapılır.
 - Bit sayısı değişmez, en soldaki bit işaret biti olur.
         0 ise pozitif, 1 ise negatif.
 - Bu yöntem sayesinde bilgisayarda çıkarma işlemi, toplama ile aynı donanım kullanılarak yapılır.
 ## Bellek (Bit) Gösterimi Mantığı
 Dönüştürülen sayının ikilik karşılığına bakılarak bellekte kaç bitlik alan kapladığı belirlenir.
 - Kullanılan kurallar:
   - 4 bitten küçük veya eşitse -> 4 bit
   - 8 bitten küçük veya eşitse -> 8 bit
   - 16 bitten küçük veya eşitse -> 16 bit
   - Daha büyükse 32 bit
 - Seçilen bit uzunluğuna ulaşana kadar ikilik sayının soluna '0' eklenir. Bu işlem bellekte saklama mantığını temsil etmektedir.
## Program Özellikleri
- Onluk tabandan ikilik ve onaltılık tabana dönüşüm yapar.
- 'bin()' ve 'hex()' fonksiyonları kullanılmaz.
- Pozitif ve negatif sayılarla çalışır.
- Kullanıcı için kullanışlı ve açıklamalı bir yapısı bulunmaktadır.
- Program basit yapıda olmasına rağmen, temel bilgisayar bilimleri konularını anlamaya yardımcı olmaktadır.
> “All information can be represented by sequences of binary digits; the manipulation of these bits using logical operations is the essence of digital computation.”                                                                             
> “Tüm bilgi ikilik basamaklar (bitler) ile temsil edilebilir; bu bitlerin mantıksal işlemlerle işlenmesi dijital hesaplamanın özüdür.”
>
> ~Claude Shannon
                 
                                                                                                          
