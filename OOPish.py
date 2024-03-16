import turkguney# Owner of M-Guney
import random
import os
print(50*"=")
print(f"İsim şehir hayvan oyununa hoş geldiniz")

harfler=('A', 'B', 'D', 'E', 'G', 'H', 'I', 'K', 'M', 'N', 'O', 'R', 'S', 'T', 'U', 'V', 'Y', 'Z', 'Ç', 'İ', 'Ş')
secilmis_harf  = random.choice(harfler)
print(f"Seçilen harf  --> {secilmis_harf}")

#Toplam oynanma  sayısı ile ilgili okuma ve yazma kısmı
try:
    with open("toplam_calisma_sayisi.txt", "r") as dosya:
        toplam_calisma_sayisi = int(dosya.read())
except FileNotFoundError:
    # Dosya bulunamazsa, "w" (write) modunda açarak dosyayı oluşturun
    with open("toplam_calisma_sayisi.txt", "w") as dosya:
        dosya.write("0")
    toplam_calisma_sayisi = 0

toplam_calisma_sayisi += 1
with open("toplam_calisma_sayisi.txt", "w") as dosya: #    w denemesinin nedeni eski bilginin yenisiyle değişmesi
    dosya.write(str(toplam_calisma_sayisi))         #   eskinin silinip yeninin girilmesi



class Sehir:
    """
        Sehiristek fonksiyonu ile sehirin inputu alınır
        Sehir_kontrol fonk ile sehir_input Şehirler.txt nin içinde var mı kontrol edilir
        writedcity fonk ile yazılan yanlış değer farklı (yazılmıssehir) bir txt dosyasına kayıt edilir
    """#Aynısı Isim ve Hayvan için de geçerli olmaktadır.
    def __init__(self):
        self.sehirlerdosya = open("Şehirler.txt", "r", encoding="utf-8")
        self.icerik = set([line.strip() for line in self.sehirlerdosya])  # her satırı bir birinden ayırdım
        self.sehirlerdosya.close()
        self.puan=0

    def sehiristek(self):
        self.sehir_input = input("Sehir: ")
        self.sehir_input = turkguney.lowertoupper(self.sehir_input)
        if self.sehir_input[0] != secilmis_harf:
            print(f"Girdiğiniz {self.sehir_input} kelimesi {secilmis_harf}'den farklı bir harfle başlamaktadır.")
            print("Lütfen tekrar giriniz.")
            self.sehiristek()

    def writedcity(self):
        try:
            with open("yazılmıssehirler.txt", "a", encoding="utf-8") as dosya:
                dosya.write(self.sehir_input + "\n")
        except FileNotFoundError:
            with open("yazılmıssehirler.txt", "w", encoding="utf-8") as dosya:
                dosya.write(self.sehir_input + "\n")
        dosya.close()


    def sehir_kontrol(self):
        if self.sehir_input not in self.icerik:
            print(f"{self.sehir_input} ile eşleşme bulunamadı!!!!!!!!!!!!!!")
            self.writedcity()
            print(f"{self.sehir_input} ile eşleşme bulunamadı!!!!!!!!")
            print("Lütfen Tekrar deneyin")
            self.sehiristek()
            self.sehir_kontrol()
        else:
            print(f"{self.sehir_input} ile eşleşme bulundu")
            self.puan+=1


class Isim:
    def __init__(self):
        self.isimlerdosya = open("İsimler.txt", "r", encoding = "utf-8")
        self.isimler = set([line.strip() for line in self.isimlerdosya])  # her satırı bir birinden ayırdım
        self.isimlerdosya.close()
        self.puan=0

    def isimistek(self):
        self.isim_input  = input("İsim: ")
        self.isim_input = turkguney.all_lowertoupper(self.isim_input)
        if self.isim_input[0] != secilmis_harf:
            print(f"Girdiğiniz {self.isim_input} kelimesi {secilmis_harf}'den farklı bir harfle başlamaktadır.")
            print("Lütfen tekrar giriniz.")
            self.isimistek()
    
    def writednames(self):
        try:
            with open("yazılmısisim.txt", "a", encoding="utf-8") as dosya:
                dosya.write(self.isim_input + "\n")
        except FileNotFoundError:
            with open("yazılmısisim.txt", "w", encoding="utf-8") as dosya:
                dosya.write(self.isim_input + "\n")
        dosya.close()

    def isim_kontrol(self):
        if self.isim_input not in self.isimler:
            errormsg = "HATA".center(50,"!")
            print(errormsg)
            print(f"{self.isim_input.title()} ile eşleşme bulunamadı!!!")
            self.writednames()
            print("Lütfen Tekrar deneyin")
            self.isimistek()
        if self.isim_input in self.isimler:
            print(f"{self.isim_input} ile eşleşme bulundu")
            self.puan+=1
        else:
            print("ne yaptıysan bana bildir çünkü nasıl bu hatayı alabildin bilmiyorum ")


class Hayvan:
    def __init__(self):
        self.hayvanlardosya = open("hayvanlar.txt", "r" , encoding = "utf-8")
        self.hayvanlar = set([line.strip() for line in self.hayvanlardosya])
        self.hayvanlardosya.close()
        self.puan=0

    def hayvanistek(self):
        self.hayvan_input = input("Hayvan: ")
        self.hayvan_input = turkguney.lowertoupper(self.hayvan_input)
        if self.hayvan_input[0] != secilmis_harf:
            print(f"Girdiğiniz {self.hayvan_input} kelimesi {secilmis_harf}'den farklı bir harfle başlamaktadır.")
            print("Lütfen tekrar giriniz.")
            self.hayvan_input()
    
    def writedanimal(self):
        try:
            with open("yazılmıshayvan.txt", "a", encoding="utf-8") as dosya:
                dosya.write(self.hayvan_input + "\n")
        except FileNotFoundError:
            with open("yazılmıshayvan.txt", "w", encoding="utf-8") as dosya:
                dosya.write(self.hayvan_input + "\n")
        dosya.close()
    
    def hayvan_kontrol(self):
        if self.hayvan_input not in self.hayvanlar:
            errormsg = "HATA".center(50,"!")
            print(errormsg)
            print(f"{self.hayvan_input} ile eşleşme bulunamadı")
            self.writedanimal()
            print("Lütfen Tekrar deneyin")
            self.hayvanistek()
            self.hayvan_kontrol()
        elif self.hayvan_input in self.hayvanlar:
            print(f"{self.hayvan_input} ile eşleşme bulundu")
            self.puan+=1
        else:
            print("ne yaptıysan bana bildir çünkü nasıl bu hatayı alabildin bilmiyorum ")


#Correct Way To Start
isim_instance = Isim()        #Obje tanımlaması yaptım çağırmak için
isim_instance.isimistek()
isim_instance.isim_kontrol()

sehir_instance = Sehir()
sehir_instance.sehiristek()
sehir_instance.sehir_kontrol()

hayvan_instance = Hayvan()
hayvan_instance.hayvanistek()
hayvan_instance.hayvan_kontrol()

print("Düzgün bir şekilde tamamladınız")
print("Puanınız: ",isim_instance.puan+sehir_instance.puan+hayvan_instance.puan)
print("İsim şehir oyunun oynanma sayısı: ",toplam_calisma_sayisi)
print(50*"=")
#Eğer ki istek olması durumunda Bitki ve Eşya ksımı eklenebilir
#Bitki,#Eşya
#Muhammed S. Güney  muhammedyazilim@gmail.com