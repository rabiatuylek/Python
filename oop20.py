# 20.07.2019
class Person:
    firstname = "",
    lastname = "",
    phone = "",
    mail = ""

    def __str__(self):
        return "".format(self.firstname , self.lastname)


def main():
    ekle = "a"
    sil = "d"
    guncelle = "u"
    liste = "ı"
    bul = "f"

    print("lutfen yapmak istediğiniz isi seçin")
    print("-"*32)
    print("kisi eklemek için :a\nkisi silmek için : d\nkisi guncellemek için : u\nkisi listesi  : ı\nkisi bulmak için  : f")
    print("-" * 32)

main()

#--------------------------------
#kisi eklemek için :a
#kisi silmek için : d
#kisi guncellemek için : u
#kisi listesi  : ı
#kisi bulmak için  : f
#--------------------------------

