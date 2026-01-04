# -*- coding: utf-8 -*- 
# Yukarıdaki satır dosyanın türkçe karakterleri düzgün okumasını sağlar

def onluk_tabani_donustur(sayi, taban): # Bu fonksiyon onluk bir sayıyı istenen tabana (2 veya 16) manuel olarak çevirir
    rakamlar = "0123456789ABCDEF" # Onaltılık sayılarda kalan sayıyı harfe çevirmek için 
    sonuc = "" # Sonuc sayı burada biriktirilecek, başlangıçta boş

    if sayi == 0:
        return "0" # Kullanıcı sıfır girerse bölme işlemi yapma, direkt sıfır döndür

    while sayi > 0: 
        kalan = sayi % taban  # Bu kalan yeni tabandaki basamak
        sonuc = rakamlar[kalan] + sonuc # Kalanı karaktere çevir, sona değil başa ekle çünkü ilk bulunan kalan en sağdaki basamaktır
        sayi //= taban # Tamsayı bölme bir sonraki basamağa geç

    return sonuc # Hesaplanan sonucu geri döndürür


def ikilik_bellek_gosterimi(ikilik_sayi): #  Kaç bitlik kutucuk gerektiğini bulur, sola sıfır ekler
    bit_sayisi = len(ikilik_sayi) # İkilik sayının kaç basamaklı olduğunu bulur

    if bit_sayisi <= 4: # 4 bitten küçük veya eşitse, 4 bitlik kutucuk
        kutucuk = 4
    elif bit_sayisi <= 8: # 8 bitten küçük veya eşitse, 8 bitlik kutucuk
        kutucuk = 8
    elif bit_sayisi <= 16: # 16 bitten küçük veya eşitse, 16 bitlik kutucuk
        kutucuk = 16
    else:
        kutucuk = 32 # 32 bitten küçük veya eşitse, 32 bitlik kutucuk

    while len(ikilik_sayi) < kutucuk: # Seçilen kutucuk boyutuna gelene kadar sola 0 ekle, bellekte böyle saklanır
        ikilik_sayi = "0" + ikilik_sayi

    return kutucuk, ikilik_sayi # Kaç bitlik kutucuk, bellekteki ikilik gösterim


def ikinin_tumleyeni(ikilik_sayi): # Bu fonksiyonun amacı pozitif bir sayının, 
    # sabit bit uzunluğu korunarak ikinin tümleyeni (two's complement) halini üretmek
    ters = "" # Bitleri tersine çevirmek için boş bir metin oluşturur
    for bit in ikilik_sayi: # Bu döngü ile ikilik sayının her bitine tek tek bakılır
        if bit == "0":
            ters += "1"
        else:
            ters += "0"

    sonuc = list(ters) # Bitleri tek tek değiştirebilmek için string-liste dönüşümü
    elde = 1 # +1 temsili

    for i in range(len(sonuc) - 1, -1, -1): # en sağdan en sola doğru ilerler
        if sonuc[i] == "1" and elde == 1: # Eğer bit 1, elde 1 ise
            sonuc[i] = "0" # 1+1=10, ikilik gösterimde bu 0'a eşittir
        elif sonuc[i] == "0" and elde == 1:
            sonuc[i] = "1"
            elde = 0

    return "".join(sonuc) # Liste tekrar stringe çevirilir


# ---------------- ANA PROGRAM ----------------

sayi = int(input("Onluk tabanda bir sayı giriniz (pozitif veya negatif): ")) # Kullanıcıdan sayı alma

print("\n1 - İkilik (Binary)")
print("2 - Onaltılık (Hexadecimal)")

secim = input("Dönüştürmek istediğiniz tabanı seçiniz (1/2): ") # Kullanıcıdan seçim alır

mutlak_sayi = abs(sayi) # abs() mutlak değer alma fonksiyonu, negatif sayılarda dönüşümü kolaylaştırır

if secim == "1":
    ikilik = onluk_tabani_donustur(mutlak_sayi, 2) # Sayıyı ikiliğe çevir
    kutucuk, bellek = ikilik_bellek_gosterimi(ikilik) # Bellekte kaç bit gerektiğini hesapla

    print("\nİkilik Karşılığı:", "-" + ikilik if sayi < 0 else ikilik) # İkilik sonucu yazdır
    print(f"Bu sayı {kutucuk} bitlik kutucuklar halinde saklanır.") # Kaç bitlik alanda saklandığını söyler

    if sayi < 0:
        ikinin_tumleyeni_bellek = ikinin_tumleyeni(bellek)
        print("Bellek Gösterimi (İki'nin Tümleyeni):", ikinin_tumleyeni_bellek)
    else:
        print("Bellek Gösterimi:", bellek) # Bellekteki halini yazdır

elif secim == "2":
    onaltilik = onluk_tabani_donustur(mutlak_sayi, 16) # Sayıyı onaltılığa çevir
    ikilik = onluk_tabani_donustur(mutlak_sayi, 2) # Bellek için ikiliye de çevir
    kutucuk, bellek = ikilik_bellek_gosterimi(ikilik) # Bellek boyutunu hesapla

    print("\nOnaltılık Karşılığı:", "-" + onaltilik if sayi < 0 else onaltilik) # Onaltılık sonucu yazdır
    print(f"Bu sayı {kutucuk} bitlik kutucuklar halinde saklanır.") # Bellek bilgisini yazdır

    if sayi < 0:
        ikinin_tumleyeni_bellek = ikinin_tumleyeni(bellek)
        print("Bellek Gösterimi (İki'nin Tümleyeni):", ikinin_tumleyeni_bellek) #
    else:
        print("Bellek Gösterimi:", bellek) # Bellek görünümünü yazdır

else:
    print("Hatalı seçim yaptınız!") # Kullanıcı 1 veya 2 dışında bir şey girerse bu satır çalışır
