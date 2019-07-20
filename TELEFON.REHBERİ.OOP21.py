# TELEFON REHBERİ


class person:
    firstname = "",
    lastname = "",
    phone = "",
    mail = ""

    def __str__(self):
        return "".format(self.firstname , self.lastname , self.phone)

    def bul(self,kelime):
        if kelime in self.firstname or \
                kelime in self.lastname or \
                kelime in self.phone or \
                kelime in self.mail:
            return True
        else:
            return False

kisiler = []
isimler = ["kelly","harry","henry","lily","ted","barney","robin","marshall","marvin","stella"]
soyisimler = ["fleming","jiem","pierce","howard","sanches","sims","thomas","mosby","stinson","eriksen"]

import random
# default olarak kullanıcı ekliyoruz.
for i in range(10):
    kisi = person()
    kisi.firstname = isimler[random.randint(0,9)]
    kisi.lastname = soyisimler[random.randint(0,9)].upper()
    kisi.phone = "+ (90) 5{} {} {} {} ".format(random.randint(10,100),random.randint(10,100),random.randint(10,100),random.randint(10,100))
    kisi.mail = "{}.{}@bilgeadam.com".format(kisi.firstname.lower(),kisi.lastname.lower())

    kisiler.append(kisi)


#for kisi in kisiler:
#    print("-"*40)
#    print("kisi adı :{}\nkisi soyadı : {}\nkisi telefon :{}\nkisi mail : {}".format(kisi.firstname,kisi.lastname,kisi.phone,kisi.mail))


def liste(kelime = ""):
    if kelime == "":
        index = 0
        for kisi in kisiler:
            print("-" * 40)
            print("kisi adı :{}\nkisi soyadı : {}\nkisi telefon :{}\nkisi mail : {}".format(index , kisi.firstname,
                                                                                            kisi.lastname,
                                                                                            kisi.phone, kisi.mail))
            index +=1

    else:
        index = 0
        for kisi in kisiler:
            if kisi.bul(kelime):
                print("-" * 50)
                print(
                    "Id           : {}\nKisi Adı     : {}\nKisi Soyadı  : {}\nKisi Telefon : {}\nKisi Mail    : {}".format(
                        index, kisi.firstname, kisi.lastname, kisi.phone, kisi.mail))
            index += 1


def main():
    ekle = "a"
    sil = "d"
    guncelle = "u"
    listele = "ı"
    bul = "f"
    islem = ""
    go_on = "y"
    result = True

    while result:

        print("lutfen yapmak istediğiniz isi seçin")
        print("-"*32)
        print("kisi eklemek için :a\nkisi silmek için : d\nkisi guncellemek için : u\nkisi listesi  : ı\nkisi bulmak için  : f")
        print("isleme devam etmek istemiyorsanız herhangi bir tusa basınız")
        print("-" * 32)
        islem = input("lutfen anahtar kelime gir").lower()

        if islem =="a":
            kisi = person()
            kisi.firstname = input("ad gir")
            kisi.lastname = input("soyad gir")
            kisi.phone = input("tel yaz")
            kisi.mail = input("mailini yaz")

            kisiler.append(kisi)
            print("eklendi")


        elif islem == "d":
            liste()
            id = int(input("silmek istenilen ıd yi yaz"))
            kisiler.remove(kisiler[id])
            print("silindi")

        elif islem == "u":
            liste()

            id = int(input("Lütfen Güncellemek İstediğiniz Kişinin ID Değerini Giriniz : "))

            update_person = kisiler[id]

            for key, value in vars(update_person).items():
                vl = input("Lütfen {} Giriniz : ".format(key))
                vars(update_person).__setitem__(key, vl)
            print("guncellendi")


        elif islem =="ı":
            liste()



        elif islem =="f":
            liste(input("anahtar kelime gir"))


        else:
            result = False
            print("çıktın")




main()

# KODUN TAMAMINA HOCADAN BAK


# homework
# kullanıcı dısarıdan tel no girdiğinde içeride formatlanması
# 34766879 gibi numarayı  +90 (000) 000 00 00 olarak alıcak.
#metot içerisine telefon numarası alıcak , geriye ise formatlı bir sekilde teslim edicek.
# min girilicek deger 10 hanedir. eger kullanıcı eksik deger girerse uyarı verin.