import time
import sys

sozluk_kurs = dict()
sozluk_ogrenci = dict()
sozluk_ogretmen = dict()

class Student():
    sayi = 0

    def __init__(self, name, surname, no, adres, password):
        self.name = name
        self.surname = surname
        self.no = no
        self.adres = adres
        self.password = password
        Student.sayi += 1


class Teacher(Student):
    sayi = 0

    def __init__(self, name, surname, no, adres, password):
        super().__init__(name, surname, no, adres, password)
        Teacher.sayi += 1


class Course():
    sayi = 0

    def __init__(self, name, student=None, teacher=None):
        self.name = name
        if student is None:
            self.student = []
        else:
            self.student = student
        if teacher is None:
            self.teacher = []
        else:
            self.teacher = teacher
        Course.sayi += 1

    def add_student(self, new_student):
        self.student = list(self.student)
        return self.student.append(new_student)

    def add_teacher(self, teacher):
        self.teacher = list(self.teacher)
        return self.teacher.append(teacher)

    def Show_Student(self):
        metin = "{0:15} {1:15} {2:<15}"
        print(metin.format("İsim", "Soyad", "No"))
        print(metin.format("-" * 15, "-" * 15, "-" * 15))
        for i in self.student:
            print(metin.format(i.name, i.surname, i.no))

    def Show_teacher(self):
        metin = "{0:15} {1:15} {2:<15}"
        print(metin.format("İsim", "Soyad", "No"))
        print(metin.format("-" * 15, "-" * 15, "-" * 15))
        for i in self.teacher:
            print(metin.format(i.name, i.surname, i.no))

    def delete_student(self, student):
        if student in self.student:
            self.student.remove(student)

    def delete_teacher(self, teacher):

        if teacher in self.teacher:
            self.teacher.remove(teacher)


def input_student_or_teacher():
    isim = input("İsim giriniz: ")
    soyad = input("Soyad giriniz: ")
    No = int(input("Numara giriniz: "))
    adres = input("Adresinizi giriniz: ")
    sifre = input("Lütfen şifrenizi giriniz: ")

    isim = isim.lower()
    soyad = soyad.lower()
    return isim, soyad, No, adres, sifre


def student_or_teacher_delete():
    isim = input("isim giriniz: ")
    soyad = input("Soyad giriniz: ")
    kurs_ismi = input("Kurs ismi giriniz: ")
    parola = input("Lütfen öğrenci parolası giriniz: ")

    isim = isim.lower()
    soyad.lower()
    kurs_ismi = kurs_ismi.lower()

    return isim, soyad, kurs_ismi, parola,


def active_courses():
    metin1 = "{0:20}"
    print(metin1.format("Aktif Olan kurslar"))
    print(metin1.format("-" * 20))
    for i in sozluk_kurs.values():
        print(metin1.format(i.name))


while True:
    islem = input(
        "İşlemler;\n1- Öğrennci Kaydı Olustur.\n2-Öğrencileri Göster.\n3-Öğretmen Kaydı Olustur.\n4-Kayıtlı Öğretmenleri Göster.\n5-Kurs Olustur.\n6-Tüm kursları Göster\n7-Kursa Öğremci Kaydet.\n8-Kursa Öğretmen Kaydet\n9-Kursatan Öğrenci Sil.\n10-Kusrtan Öğretmen Sil.\n11-Kursa Kayıtlı Olan öğrencileri Göster\n12-Kursa Kayıtlı olan Öğretmenleri Göster\nÇıkış Yapmak için 'q' basınız.\nGirmek istediğiniz işlemi giriniz:  ")
    if islem == "q":
        print("Çıkış yapılıyor...")
        time.sleep(3)
        break
    if islem == "1":
        output = input_student_or_teacher()
        stundent = Student(output[0], output[1], output[2], output[3], output[4])
        tag = str(stundent.name + stundent.surname)
        print(tag)
        if tag not in sozluk_ogrenci.keys():
            sozluk_ogrenci[tag] = stundent
            print(f"{output[0]} isimli öğrenci başarılı şekilde kayıt olmuştur...")
            time.sleep(3)

        else:
            sys.stderr.write("Girdiğiniz öğrenci bilgileri sistemimizde kayıtlıdır. Kontrol ediniz.")
            sys.stderr.flush()
            time.sleep(3)
            continue

    elif islem == "2":
        metin = "{0:15} {1:15} {2:<15} {3:20}"
        print("Sisteme kayıtlı olan öğrenciler")
        print(metin.format("İsim", "Soyad", "No", "adres"))
        print(metin.format("-" * 15, "-" * 15, "-" * 15, "-" * 20))
        for i in sozluk_ogrenci.values():
            print(metin.format(i.name, i.surname, i.no, i.adres))
        print(f"Sisteme kayıtlı öğrenci sayısı {Student.sayi}'dir.")
        time.sleep(5)

    elif islem == "3":
        output = input_student_or_teacher()
        teacher = Teacher(output[0], output[1], output[2], output[3], output[4])
        tag = str(teacher.name + teacher.surname)
        sozluk_ogretmen[tag] = teacher
        print(f"{output[0]} isimli öğretmen kaydı olusturulmuştır...")
        time.sleep(3)

    elif islem == "4":
        metin = "{0:15} {1:15} {2:<15} {3:20}"
        print("Sisteme kayıtlı olan öğrentmenler")
        print(metin.format("İsim", "Soyad", "No", "adres"))
        print(metin.format("-" * 15, "-" * 15, "-" * 15, "-" * 15))
        for i in sozluk_ogretmen.values():
            print(metin.format(i.name, i.surname, i.no, i.adres))
        print(f"Sisteme kayıtlı olan öğretmen sayısı {Teacher.sayi}'dir.")
        time.sleep(5)

    elif islem == "5":

        name = input("Kurs ismi giriniz: ")
        course = Course(name)
        tag = course.name
        if name not in sozluk_kurs.keys():
            sozluk_kurs[tag] = course
            print(f"{tag.title()} isimli kurs olusturulmuştur")
            time.sleep(3)
        else:
            sys.stderr.write(f"{tag} isimli kurs bulunmaktadır...")

    elif islem == "6":
        metin = "{0:20}"
        print(metin.format("Kurslar"))
        print(metin.format("-" * 20))
        for i in sozluk_kurs.values():
            print(metin.format(i.name))
        print(f"Olusturalan kursların sayısı {Course.sayi}'dir.")
        time.sleep(4)

    elif islem == "7":
        active_courses()
        output = student_or_teacher_delete()
        new_output = str(output[0] + output[1])
        if new_output in sozluk_ogrenci:
            ogrenci_nesnesi = sozluk_ogrenci[new_output]
        else:
            sys.stderr.write("Girdiğiniz öğreci ismi bulunmamaktadır...\n")
            sys.stderr.flush()
            time.sleep(4)
            continue
        if output[3] == ogrenci_nesnesi.password:
            print("Parola Dogru")
            time.sleep(2)

        else:
            sys.stderr.write("Girdiğiniz şifre yanlıştır...\n")
            sys.stderr.flush()
            time.sleep(4)
            continue

        if output[2] in sozluk_kurs:
            kurs_nesnesi = sozluk_kurs[output[2]]
            kurs_nesnesi.add_student(ogrenci_nesnesi)
            print(
                f"{ogrenci_nesnesi.name} isim ögrenci başarılı şekilde {kurs_nesnesi.name} kursa kayıt olmştur...")
            time.sleep(3)
        else:
            sys.stderr.write("Girdiğiniz kurs ismi bulunmamaktadır...\n")
            sys.stderr.flush()
            time.sleep(4)
            continue


    elif islem == "8":
        active_courses()

        output = student_or_teacher_delete()
        new_output = str(output[0] + output[1])
        if new_output in sozluk_ogretmen:
            ogretmen_nesnesi = sozluk_ogretmen[new_output]
        else:
            sys.stderr.write("Girdiğiniz öğretmen ismi bulunmamaktadır...\n")
            sys.stderr.flush()
            time.sleep(4)
            continue
        if output[3] == ogretmen_nesnesi.password:
            print("Parola Dogru")
            time.sleep(2)

        else:
            sys.stderr.write("Girdiğiniz şifre yanlıştır...\n")
            sys.stderr.flush()
            time.sleep(4)
            continue

        if output[2] in sozluk_kurs:
            kurs_nesnesi = sozluk_kurs[output[2]]
            kurs_nesnesi.add_teacher(ogretmen_nesnesi)
            print(
                f"{ogretmen_nesnesi.name} isimli öğrentmen başarılı şekilde {kurs_nesnesi.name} kursuna kayıt olmştur...")
            time.sleep(3)
        else:
            sys.stderr.write("Girdiğiniz Kurs ismi bulunmamaktadır...\n")
            sys.stderr.flush()
            time.sleep(4)
            continue

    elif islem == "9":
        active_courses()

        output = student_or_teacher_delete()
        new_output = str(output[0] + output[1])
        if new_output in sozluk_ogrenci:
            ogrenci_nesnesi = sozluk_ogrenci[new_output]
        else:
            sys.stderr.write("Girdiğiniz öğrenci ismi bulunmamaktadır...\n")
            sys.stderr.flush()
            time.sleep(4)
            continue

        if output[3] == ogrenci_nesnesi.password:
            print("Parola Dogru")
            time.sleep(2)

        else:
            sys.stderr.write("Girdiğiniz şifre yanlıştır...\n")
            sys.stderr.flush()
            time.sleep(4)
            continue

        if output[2] in sozluk_kurs:
            kurs_nesnesi = sozluk_kurs[output[2]]
            kurs_nesnesi.delete_student(ogrenci_nesnesi)
            print(f"{ogrenci_nesnesi.name} isimli öğrenci {kurs_nesnesi.name} kurstan çıkarılmıştır...")
            print("Kursta olan öğrenciler")
            kurs_nesnesi.Show_Student()
            time.sleep(3)
        else:
            sys.stderr.write("Girdiğiniz Kurs ismi bulunmamaktadır...\n")
            sys.stderr.flush()
            time.sleep(4)
            continue



    elif islem == "10":
        active_courses()

        output = student_or_teacher_delete()
        new_output = str(output[0] + output[1])
        if new_output in sozluk_ogretmen:

            ogretmen_nesnesi = sozluk_ogretmen[new_output]

        else:
            sys.stderr.write("Girdiğiniz öğretmen ismi bulunmamaktadır...\n")
            sys.stderr.flush()
            time.sleep(4)
            continue
        if output[3] == ogretmen_nesnesi.password:
            print("Parola Dogru")
            time.sleep(2)

        else:
            sys.stderr.write("Girdiğiniz şifre yanlıştır...\n")
            sys.stderr.flush()
            time.sleep(4)
            continue

        if output[2] in sozluk_kurs:
            kurs_nesnesi = sozluk_kurs[output[2]]

            kurs_nesnesi.delete_teacher(ogretmen_nesnesi)
            print(f"{ogretmen_nesnesi.name} isimli öğrenci {kurs_nesnesi.name} kurstan çıkarılmıştır...")
            print("Kursta olan öğretmenler")
            kurs_nesnesi.Show_teacher()
            time.sleep(3)
        else:
            sys.stderr.write("Girdiğiniz kurs ismi bulunmamaktadır...\n")
            sys.stderr.flush()
            time.sleep(4)
            continue

    elif islem == "11":
        active_courses()

        kurs_ismi = input("Kurs ismini giriniz: ")

        if kurs_ismi in sozluk_kurs:
            kurs_nesnesi = sozluk_kurs[kurs_ismi]
            print(f"{kurs_nesnesi.name} kayıtlı öğrenciler")
            kurs_nesnesi.Show_Student()
            time.sleep(5)
        else:
            sys.stderr.write("Girdiğiniz kurs ismi bulunmamaktadır...\n")
            sys.stderr.flush()
            time.sleep(4)
            continue

    elif islem == "12":
        active_courses()

        kurs_ismi = input("Kurs ismini giriniz: ")
        kurs_ismi = kurs_ismi.lower()
        if kurs_ismi in sozluk_kurs:
            kurs_nesnesi = sozluk_kurs[kurs_ismi]
            print(f"{kurs_nesnesi.name} kayıtlı öğretmenler")
            kurs_nesnesi.Show_teacher()
            time.sleep(5)

        else:
            sys.stderr.write("Girdiğiniz kurs ismi bulunmamaktadır...\n")
            sys.stderr.flush()
            time.sleep(4)
            continue

    else:
        sys.stderr.write("Geçersiz Kod girişi yaptınız... Tekrar deneyiniz.\n")
        sys.stderr.flush()
        time.sleep(3)
        continue
