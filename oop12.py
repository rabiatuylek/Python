# inheritance = genisletme gibi dusunebiliriz.

class calisan():
    def __init__(self,isim,soyisim,maas,yas = 10):
        print("calisan sınıfının yapıcı metodu calıstı")
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas
        self.maas = maas
    def __str__(self):
        return "{} {} {} {}".format(self.isim,self.soyisim,self.yas,self.maas)
pers = calisan("murat","vuranok",40,5678)
print(pers)


# yas parametresi gondermezsek, içeride tanımlı default deger geçerli olacaktır.
#calisan sınıfının yapıcı metodu calıstı
#murat vuranok 5678 40
















class calisan():
    def __init__(self,isim,soyisim,maas,yas = 10):
        print("calisan sınıfının yapıcı metodu calıstı")
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas
        self.maas = maas
    def __str__(self):
        return "{} {} {} {}".format(self.isim,self.soyisim,self.yas,self.maas)
    def bilgigoster(self):
        print("çalısan sınıfına ait bilgiler gosterilmektedir")
        print("isim : {}\nsoyisim : {}\nmaas : {}".format(
            self.isim,
            self.soyisim,
            self.maas))


pers = calisan("murat","vuranok",40,5678)
print(pers)
pers.bilgigoster()

#calisan sınıfının yapıcı metodu calıstı
#murat vuranok 5678 40
#çalısan sınıfına ait bilgiler gosterilmektedir
#isim : murat
#soyisim : vuranok
#maas : 40















