import random
menu = {"turk kahvesi": 20, "filtre kahve": 25, "cay": 10, "su": 5}
masalar = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
dolu_masa = set()
bos_masalar = set()
liste = []
price = []
for i in range(100):
    sayı = random.randint(1, 10)
    dolu_masa.add(sayı)
    if len(dolu_masa) == 7:
        break

for i in masalar:
    if i not in dolu_masa:
        bos_masalar.add(i)

print(dolu_masa)
print(bos_masalar)
while True:
    masa = int(input("Masanızı Seciniz: "))
    if masa in dolu_masa:
        print("Dolu Masa Sectiniz Tekrar deneyin")
    else:
        print("Hosgeldiniz: ")
        break
while True:
    siparis = input("Lütfen siparisinizi giriniz: ")
    siparis = siparis.lower()
    siparis = siparis.replace("ü", "u")
    siparis = siparis.replace("ç", "c")
    siparis = siparis.replace("ş", "s")

    if siparis == "q":
        print("Urun Adı ", " adet ", " Fiyat ", " Masa No:")
        for ad, adet, fiyat in liste:
            print(f"Ürün adı: {ad.title()} -- adeti: {adet} -- fiyatı: {fiyat}")

        print(f"{masa} nolu masanın Toplam Fiyatı: {sum(price)}'Tldir.")

        break

    adet = int(input("Lütfen kaç adet girmek istediğinizi yazınız: "))

    if siparis in menu.keys():
        fiyat = menu[siparis] * adet
        veri = (siparis, adet, fiyat)

        price.append(fiyat)
        liste.append(veri)