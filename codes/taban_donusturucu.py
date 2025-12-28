# -*- coding: utf-8 -*- 
# Yukarıdaki satır dosyanın türkçe karakterleri düzgün okumasını sağlar

def onluk_tabani_donustur(sayi, taban): # Bu fonksiyon onluk bir sayıyı istenen tabana (2 veya 16) manuel olarak çevirir
    rakamlar = "0123456789ABCDEF" # Onaltılık sayılarda kalan sayıyı harfe çevirmek için 
    sonuc = "" # Sonuc sayı burada biriktirilecek, başlangıçta boş

    # Kullanıcı sıfır girerse bölme işlemi yapma, direkt sıfır döndür
    if sayi == 0:
        return "0"

    while sayi > 0: 
        kalan = sayi % taban  # Bu kalan yeni tabandaki basamak
        sonuc = rakamlar[kalan] + sonuc # Kalanı karaktere çevir, sona değil başa ekle çünkü ilk bulunan kalan en sağdaki basamaktır
        sayi //= taban # Tamsayı bölme bir sonraki basamağa geç

    return sonuc # Hesaplanan sonucu geri döndürür


def ikilik_bellek_gosterimi(ikilik_sayi): #  Kaç bitlik kutucuk gerektiğini bulur, sola sıfır ekler
    bit_sayisi = len(ikilik_sayi) # İkilik sayının kaç basamaklı olduğunu bulur

    if bit_sayisi <= 4:
        kutucuk = 4
    elif bit_sayisi <= 8:
        kutucuk = 8
    elif bit_sayisi <= 16:
        kutucuk = 16
    else:
        kutucuk = 32

    while len(ikilik_sayi) < kutucuk: # Seçilen kutucuk boyutuna gelene kadar sola 0 ekle, bellekte böyle saklanır
        ikilik_sayi = "0" + ikilik_sayi

    return kutucuk, ikilik_sayi # Kaç bitlik kutucuk, bellekteki ikilik gösterim


# ---------------- ANA PROGRAM ----------------

sayi = int(input("Onluk tabanda bir sayı giriniz (pozitif veya negatif): ")) # Kullanıcıdan sayı alma

print("\n1 - İkilik (Binary)")
print("2 - Onaltılık (Hexadecimal)")

secim = input("Dönüştürmek istediğiniz tabanı seçiniz (1/2): ") # Kullanıcıdan seçim alır

mutlak_sayi = abs(sayi) # abs() mutlak değer alma fonksiyonu, negatif sayılarda dönüşümü kolaylaştırır

if secim == "1":
    ikilik = onluk_tabani_donustur(mutlak_sayi, 2) # Sayıyı ikiliğe çevir
    kutucuk, bellek = ikilik_bellek_gosterimi(ikilik) # Bellekte kaç bit gerektiğini hesapla

    if sayi < 0:
        ikilik = "-" + ikilik # Sayı negatifse başına '-' ekle

    print("\nİkilik Karşılığı:", ikilik) # İkilik sonucu yazdır
    print(f"Bu sayı {kutucuk} bitlik kutucuklar halinde saklanır.") # Kaç bitlik alanda saklandığını söyler
    print("Bellek Gösterimi:", bellek) # Bellekteki halini yazdır

elif secim == "2":
    onaltilik = onluk_tabani_donustur(mutlak_sayi, 16) # Sayıyı onaltılığa çevir
    ikilik = onluk_tabani_donustur(mutlak_sayi, 2) # Bellek için ikiliye de çevir
    kutucuk, bellek = ikilik_bellek_gosterimi(ikilik) # Bellek boyutunu hesapla

    if sayi < 0:
        onaltilik = "-" + onaltilik # Sayı negatifse başına '-' ekle

    print("\nOnaltılık Karşılığı:", onaltilik) # Onaltılık sonucu yazdır
    print(f"Bu sayı {kutucuk} bitlik kutucuklar halinde saklanır.") # Bellek bilgisini yazdır
    print("Bellek Gösterimi:", bellek) # Bellek görünümünü yazdır

else:
    print("Hatalı seçim yaptınız!") # Kullanıcı 1 veya 2 dışında bir şey girerse bu satır çalışır
