import time
import os
import requests

kullanici_sozluğu = {}
odeme_sozlugu = {}
metin = "{0:15} {1:<15}"


class User():
    def __init__(self, isim, ana_para, odemeler=None):
        self.ana_para = ana_para
        self.isim = isim
        if odemeler is None:
            self.odemeler = []

        else:
            self.odemeler = odemler

    def odeme_yontemi_ekle(self, odeme):
        self.odemeler = list(self.odemeler)
        return self.odemeler.append(odeme)


class Odeme():
    def __init__(self, odeme_turu, fiyati):
        self.odeme_turu = odeme_turu
        self.fiyati = fiyati


class Genel():
    @staticmethod
    def kullanici_olustur():
        isim = input("Kullanici isimini giriniz: ")
        ana_para = int(input("Ana Parayı giriniz: "))
        isim = isim.lower()
        return isim, ana_para

    @staticmethod
    def odeme_olustur():
        odeme_turu = input("Ödeme türünü giriniz: ")
        fiyati = int(input("Fiyatını giriniz: "))
        odeme_turu = odeme_turu.lower()
        return odeme_turu, fiyati

    @staticmethod
    def dolar_ceviri():
        result = requests.get("http://data.fixer.io/api/latest?access_key=3eaf33d4a77e6bd74182ebc4c486ad51")
        birimler_dict = result.json()
        paralar_dict = birimler_dict["rates"]
        amount = paralar_dict["TRY"]

        amount1 = paralar_dict["USD"]
        return amount1 / amount


while True:
    islem = input(
        "1-Kullanici Olustur.\n2-Ödeme Türü Oluştur.\n3-Kullanici Ödemesi Ekle.\n4-Ödemeler Toplamı Göster.\n5-Ödemeleri Kaydet ve Günü bitir.\n6-Ödemeleri Ana Paradan Düşür.\nProgramdan çıkış yapmak için 'q' basınız...\nGirmek istediğiniz işlemi seçiniz: ")

    if islem == "q":
        print("Çıkış yapılıyor.......")
        break

    if islem == "1":
        g1 = Genel.kullanici_olustur()
        kullanici = User(g1[0], g1[1])
        tag = kullanici.isim
        kullanici_sozluğu[tag] = kullanici
        print(kullanici_sozluğu[tag].odemeler)

    elif islem == "2":
        g2 = Genel.odeme_olustur()
        odeme = Odeme(g2[0], g2[1])
        tag = odeme.odeme_turu
        odeme_sozlugu[tag] = odeme

        print(
            f"{tag.title()} ketegorisi olan ödeme {g2[1]} Türk lirası ödeme yapılmıştır. Yaptığınız alışveriş, provizyonda beklemektedir. Provizyondan çıkması için -- işlem == 3'den doğrulama yapmanız gerekmektedir....")
        time.sleep(2)

    elif islem == "3":

        print("Provizyonda bekleyen ödemeler")
        for i in odeme_sozlugu.values():
            print(metin.format(i.odeme_turu, i.fiyati))

        isim = input("Kullanici isimini giriniz: ")
        odeme_yontemi = input("Ödeme Yöntemini giriniz: ")

        if isim in kullanici_sozluğu.keys():
            kullanici_nesnesi = kullanici_sozluğu[isim]
            print(kullanici_nesnesi.ana_para)
        else:
            print("Böyle bir kullanci bulunmamaktadır.")
            continue
        if odeme_yontemi in odeme_sozlugu.keys():
            odeme_nesnesi = odeme_sozlugu[odeme_yontemi]
            kullanici_nesnesi.odeme_yontemi_ekle(odeme_nesnesi)
            print("Ödemeler")
            print(metin.format("Ödeme Türü", "Fiyatı"))
            print(metin.format("-" * 15, "-" * 15))

            for i in kullanici_nesnesi.odemeler:
                print(metin.format(i.odeme_turu.title(), i.fiyati))
        else:
            print("böyle bir ödeeme yöntemi yoktur...")

    elif islem == "4":
        isim = input("Kullanici isimini giriniz: ")
        isim = isim.lower()
        if isim in kullanici_sozluğu.keys():
            kullanici_nesnesi = kullanici_sozluğu[isim]
        else:
            print("Böyle bir kullanci bulunmamaktadır.")
            continue

        print("Ödemeler")
        print(metin.format("Ödeme Türü", "Fiyatı"))
        print(metin.format("-" * 15, "-" * 15))

        for i in kullanici_nesnesi.odemeler:
            print(metin.format(i.odeme_turu.title(), i.fiyati))

        total = 0
        print(metin.format("-" * 15, "-" * 15))
        for i in kullanici_nesnesi.odemeler:
            total += i.fiyati
        dolar = Genel.dolar_ceviri()

        print(metin.format(f"TRY {total}", f"Dolar {dolar * total}"))

    elif islem == "5":
        isim = input("Kullanici isimini giriniz: ")
        isim = isim.lower()
        if isim in kullanici_sozluğu.keys():
            kullanici_nesnesi = kullanici_sozluğu[isim]
        else:
            print("Böyle bir kullanci bulunmamaktadır.")
            continue
        total = 0
        for i in kullanici_nesnesi.odemeler:
            total += i.fiyati

        path = f"./{kullanici_nesnesi.isim}.txt"

        if os.path.isfile(path):
            with open(f'{kullanici_nesnesi.isim}.txt', 'ta+', encoding='utf-8') as fa:
                print(kullanici_nesnesi.isim, total, kullanici_nesnesi.ana_para, file=fa)
                fa.seek(0)
                lines = fa.readlines()
                print("Bu zamana kadar olan toplam ödemeler...")
                print(metin.format("-" * 15, "-" * 15))
                dolar = Genel.dolar_ceviri()
                print(metin.format(f"{kullanici_nesnesi.isim}", "Ödemeleri"))
                for i in lines:
                    liste = i.split(" ")
                    print(metin.format(f"TRY: {liste[1]}", f"Dolar: {dolar * int(liste[1])}"))
                break

        else:
            with open(f'{kullanici_nesnesi.isim}.txt', 'tw', encoding='utf-8') as fa:
                print(kullanici_nesnesi.isim, total, kullanici_nesnesi.ana_para, file=fa)
                break

    elif islem == "6":
        isim = input("Kullanici isimini giriniz: ")
        isim = isim.lower()
        path1 = f"./{isim}.txt"

        try:
            if os.path.isfile(path1):
                with open(f"{isim}.txt", "tr", encoding="utf-8") as fr:
                    liste = fr.readlines()
                    ana_para = liste[0].split(" ")

                    giderler_toplami = 0
                    for i in liste:
                        if isim in i:
                            new_liste = i.split(" ")
                            giderler = new_liste[1]
                            giderler = int(giderler)
                            giderler_toplami += giderler

                    genel_butce = int(ana_para[2]) - giderler_toplami

                    if genel_butce <= 0:
                        print("Böyle bir ödeme gerçekleştiremiyoruz... Bakiyeniz yetersiz...")

                    else:

                        kullanici = User(isim, genel_butce)
                        tag = kullanici.isim
                        kullanici_sozluğu[tag] = kullanici
                        print(metin.format("Kullanıcı isimi", "Güncel Bakiye"))
                        print(metin.format("-" * 15, "-" * 15))
                        print(metin.format(kullanici_sozluğu[tag].isim, kullanici_sozluğu[tag].ana_para))

            else:
                print("Böyle bir kullanıcı bulunmamaktadır.")
        except:
            print("Burası sadece finally bölümü için açtım")

        finally:
            if isim in kullanici_sozluğu.keys():
                kullanici_nesnesi = kullanici_sozluğu[isim]
                print(f"{kullanici_nesnesi.isim} kullanıcının ödeme yapamadan önceki parası {ana_para[2]}")
                print(f"{kullanici_nesnesi.isim} kullacının ödeme yaptıktan sonra kalan parası {kullanici_nesnesi.ana_para}")
                os.remove(path1)


    else:
        print("Yanlış işlem girişi yaptınız....")