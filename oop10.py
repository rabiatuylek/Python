# __init__ constructor yapıcı metot

class personel:
    isim = ""
    soyisim = ""
    yas = 0

per = personel()
per.isi = "rabia"
per.soyisim = "tuylek"
per.yas = 100
print(per)
# <__main__.personel object at 0x01DECB70>


class personel:
    isim = ""
    soyisim = ""
    yas = 0

    def __str__(self):
        return "{} {}".format(self.isim,self.soyisim)

per = personel()
per.isim = "rabia"
per.soyisim = "tuylek"
per.yas = 100
print(per)
# rabia tuylek





























