import psycopg2
import random
import time


class Nutritionist():
    def __init__(self):
        self.__baglanti_olustur()
        self.__kullanici_tablo_olustur_1()
        self.__yemek_tablo_olustur()
        self.start()

    def start(self):
        print("Hoşgeldiniz Girdiğiniz yemekler 100 gram üzerinden kalori hesabı yapılacaktır. Çıktılar ise grama karşlık gelen kalorileri gösterecektir...\n choise == 7'e basarsanız Hazır yemekler sisteme eklenecektir. Diğer durumda kendiniz ekleyebilirsiniz.")
        choise = input("1-Kullanıcı oluştur\n2-Gıda ürünü ekle\n3-Bir günlük yemek listesini göster\n4-Beş günlük yemek listesini göster\n5-Kayıtlı olan kullanıcıları göster\n6-Kayıtlı olan Besinleri Göster\nİşlem seçiniz: ")
        if choise == "1":
            self.create_user()
            time.sleep(3)
            self.start()

        elif choise == "2":

            self.create_food()
            time.sleep(3)
            self.start()

        elif choise == "3":
            name = input("İsim giriniz: ")
            self.__tek_kullanici_goster(name)
            self.hesap(name)
            time.sleep(4)
            self.start()

        elif choise == "4":

            name = input("İsim giriniz: ")
            self.__tek_kullanici_goster(name)
            print("Day 1:")
            self.hesap(name)
            print("*" * 70)
            print("Day 2:")
            self.hesap(name)
            print("*" * 70)
            print("Day 3:")
            self.hesap(name)
            print("*" * 70)
            print("Day 4:")
            self.hesap(name)
            print("*" * 70)
            print("Day 5:")
            self.hesap(name)

            time.sleep(10)
            self.start()

        elif choise == "5":
            self.Kullanicilari_göster()
            time.sleep(3)
            self.start()

        elif choise == "6":
            self.Besinleri_goster()
            time.sleep(3)
            self.start()

        elif choise == "7":
            self.__YemekEkle()
            self.start()


        else:
            print("Geçersiz işlem...")
            self.start()

    def __baglanti_olustur(self):
        self.connection = psycopg2.connect(
            user="postgres",
            password="1fclj271",
            host="127.0.0.1",
            port="5432",
            database="Nutritionist"
        )
        self.cursor = self.connection.cursor()
        self.connection.commit()

    def __yemek_tablo_olustur(self):
        query = "create table if not exists  food(name TEXT, caloeries INT)"
        self.cursor.execute(query)
        self.connection.commit()

    def __kullanici_tablo_olustur_1(self):
        query_1 = "create table if not exists  kullanici(name TEXT, age INT, gender TEXT, boy INT, weight INT, calories INT)"
        self.cursor.execute(query_1)
        self.connection.commit()

    def create_food(self):
        metin = "{0:20} {1:<20}"
        isim = input("Eklemek istediğiiniz gıda ürününün isimini giriniz: ")
        calorie = int(input("Girdiğiniz gıda ürününün kalori miktarının giriniz: "))
        isim = isim.lower()

        query_food = '''
        select name from food
        '''
        self.cursor.execute(query_food)
        data_food = self.cursor.fetchall()
        data_name = (isim, )
        if data_name in data_food:
            print("Böyle bir besin daha önce ekleme yaptınız...")
        else:
            query = f"insert into food values('{isim}', {calorie})"

            self.cursor.execute(query)
            self.connection.commit()


            print(metin.format("İsim", "Kalori"))
            print(metin.format(f"{isim}'li ürün", f"{calorie} değeriyle eklendi..."))

    def Kullanicilari_göster(self):

        query = "select * from kullanici"
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        metin1 = "{0:20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}"
        print(metin1.format("İsim", "Yaş", "Cinsiyet", "Boy(cm)", "Kilo", "Ortalama Kalori"))
        print(metin1.format("-" * 20, "-" * 20, "-" * 20, "-" * 20, "-" * 20, "-" * 20))
        for isim, yas, cinsiyet, boy, kilo, kalori in data:
            print(metin1.format(isim, yas, cinsiyet, boy, kilo, kalori))

    def __YemekEkle(self):
        query_1 = "insert into food values('potato', 93), ('fried Egg', 143),('bread', 256), ('almond', 575), ('meatball', 160), ('rice', 139), ('apple', 52), ('banana', 88), ('cauliflower', 25), ('broccoli', 26)"
        self.cursor.execute(query_1)
        self.connection.commit()

    def __tek_kullanici_goster(self, name):
        query3 = f"select * from kullanici where name='{name}'"
        self.cursor.execute(query3)
        data = self.cursor.fetchone()
        metin1 = "{0:20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}"
        print(metin1.format("İsim", "Yaş", "Cinsiyet", "Boy(cm)", "Kilo", "Ortalama Kalori"))
        print(metin1.format("-" * 20, "-" * 20, "-" * 20, "-" * 20, "-" * 20, "-" * 20))
        print(metin1.format(data[0], data[1], data[2], data[3], data[4], data[5]))

    def Besinleri_goster(self):
        query = "select * from food"
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        metin = "{0:20} {1:<20}"
        print(metin.format("Besin", "Kalori Değeri"))
        print(metin.format("-" * 20, "-" * 20))
        for isim, kalori in data:
            print(metin.format(isim, kalori))

    def __boy_kilo_endex(self, boy, weight):
        boy = boy / 100
        endex = weight / pow(boy, 2)
        endex = round(endex, 0)
        if endex <= 20:
            bulk_or_cut = "bulk"
        else:
            bulk_or_cut = "cut"

        return bulk_or_cut

    def __Gender(self, gender, bulk_or_cut):
        if gender == "kadin" and bulk_or_cut == "cut":
            calories = 1700

        elif gender == "kadin" and bulk_or_cut == "bulk":

            calories = 2700

        elif gender == "erkek" and bulk_or_cut == "bulk":
            calories = 3200

        elif gender == "erkek" and bulk_or_cut == "cut":
            calories = 2200

        return calories

    def __display_create_user(self, name):
        query1 = f"select * from kullanici where name='{name}'"
        self.cursor.execute(query1)
        data = self.cursor.fetchone()
        metin1 = "{0:20} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}"
        print(metin1.format("İsim", "Yaş", "Cinsiyet", "Boy(cm)", "Kilo", "Ortalama Kalori"))
        print(metin1.format("-" * 20, "-" * 20, "-" * 20, "-" * 20, "-" * 20, "-" * 20))
        print(metin1.format(data[0], data[1], data[2], data[3], data[4], data[5]))
        print("Başarılı Şekilde Databaseye kayıt olmuştur.")

    def create_user(self):
        name = input("İsim giriniz: ")
        age = int(input("Yaşınızı giriniz: "))
        gender = input("Cinsiyetinizi giriniz (Kadın veya Erkek şeklinde): ")
        boy = int(input("Boyunuzu giriniz (cm olarak) : "))
        weight = int(input("Kilonuzu tam sayı olarak giriniz: "))
        name = name.lower()
        gender = gender.lower()
        gender = gender.replace("ı", "i")

        bulk_or_cut = self.__boy_kilo_endex(boy, weight)

        calories = self.__Gender(gender, bulk_or_cut)

        query_1 = "select * from kullanici"
        self.cursor.execute(query_1)
        veri = self.cursor.fetchall()
        if veri == []:
            query = f"insert into kullanici values('{name}', {age}, '{gender}', {boy}, {weight}, {calories})"
            self.cursor.execute(query)
            self.connection.commit()

            self.__display_create_user(name)

        else:
            for i in veri:
                if name not in i:
                    query = f"insert into kullanici values('{name}', {age}, '{gender}', {boy}, {weight}, {calories})"
                    self.cursor.execute(query)
                    self.connection.commit()

                    self.__display_create_user(name)
                else:
                    print("Böyle bir kullanici vardır...")

    def rastgele_yemek(self, kullanici_verisi, calories):
        query_1 = "select * from food"
        self.cursor.execute(query_1)
        tum_yemekler = self.cursor.fetchall()
        sayi = len(tum_yemekler)
        rastgele = random.randint(0, sayi - 1)
        yemek_adeti_rastegele = random.randint(1, 3)
        secilen_yemek = tum_yemekler[rastgele][0]
        secilen_yemek_kalorisi = tum_yemekler[rastgele][1] * yemek_adeti_rastegele
        agirlik = 100 * yemek_adeti_rastegele
        yemek_bilgileri = [secilen_yemek, secilen_yemek_kalorisi, agirlik]

        return secilen_yemek, secilen_yemek_kalorisi, yemek_bilgileri, agirlik

    def hesap(self, name):
        query = "Select calories from kullanici where name='{}'".format(name)
        self.cursor.execute(query)
        kullanici_verisi = self.cursor.fetchone()
        calories = kullanici_verisi[0]

        total_1 = 0
        total = 0
        secilen_yemekler = []
        yemek_listesi = []
        while True:
            metin = "{0:20} {1:<20} {2:<20}"
            a = self.rastgele_yemek(kullanici_verisi, calories)
            secilen_yemek = a[0]
            secilen_yemek_kalorisi = a[1]
            yemek_bilgileri = a[2]
            agirlik = a[3]
            if total < calories:
                if secilen_yemek not in secilen_yemekler:
                    secilen_yemekler.append(secilen_yemek)
                    total += secilen_yemek_kalorisi
                    yemek_listesi.append(yemek_bilgileri)
                else:
                    pass

            else:
                total1 = 0
                print(metin.format("Yemek", "Kalori", "Ağırlık"))
                for yemek, kalori, gram in yemek_listesi:
                    total1 += kalori
                    print(metin.format(yemek, kalori, gram))

                print(metin.format("-" * 20, "-" * 20, "-" * 20))
                print(metin.format("Toplam", "Kalori", total1))
                break


d1 = Nutritionist()
