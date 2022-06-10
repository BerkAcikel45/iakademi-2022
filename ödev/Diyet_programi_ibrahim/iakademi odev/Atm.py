kayitli = [{"isim": "ibrahim", "password": "1234", "para": 50000},
           {"isim": "mustafa", "password": "5678", "para": 150000}]


def para_cekme(bakiye, tutar):
    new_bakiye = bakiye - tutar

    return new_bakiye


def para_yatırma(bakiye, tutar):
    new_bakiye = bakiye + tutar

    return new_bakiye





parola = input("Parolanızı giriniz: ")

for i in kayitli:
    if i["password"] != parola:
        print("Hata giriş Yapıtınız...")
        break

    else:
        para = i["para"]
        print("hosgeldiniz", i["isim"])


        while True:
            print("İşlemler;\n 1- Para çekme\n2-Para Yatırma\n3-Bakiye göster\n4-Para çek\nÇıkış Yapmak için 'q' basınız....")
            islem = input("Yapmak istediğiniz işlemi seciniz:")
            if islem == "q":
                print("Tekrar görüşmek üzere...")
                break

            elif islem == "1":
                tutar = int(input("Çekmek istediğiniz tutarı giriniz: "))
                new_para = para_cekme(para, tutar)

                if new_para < 0:
                    print("İşlem Başarısız...")

                else:
                    para = new_para
                    print(f"Güncel Bakiyeniz: {para}")