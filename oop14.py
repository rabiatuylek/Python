class calisan():
    def __init__(self, isim, soyisim, maas,departman ,yas=10):
        print("calisan sınıfının yapıcı metodu calıstı")
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas
        self.maas = maas
        self.departman = departman

    def __str__(self):
        return "{} {} {} {}".format(self.isim, self.soyisim, self.yas, self.maas, self.departman)

    def bilgigoster(self):
        print("çalısan sınıfına ait bilgiler gosterilmektedir")
        print("isim : {}\nsoyisim : {}\nyas : {}\nmaas : {}\ndepartman : {}".format(
            self.isim,
            self.soyisim,
            self.yas,
            self.maas,
            self.departman))

    def zamyap(self, zam_orani):
        print("calısanın maaşına zam yapıldı")
        maas = self.maas
        self.maas += zam_orani
        print("{} personelin maası : {} tl den {} tl ye yukseltildi".format(self.isim + " "+ self.soyisim,maas,self.maas))

    def departmandegistir(self,departman):
        print("çalısanın departmanı degistirildi")
        departman = self.departman
        self.departman = departman
        print("{} personelin departmanı : {} departmanından {} departmanına gecisi saglandı".format(self.isim + " "+ self.soyisim,departman,
        self.departman))

class yonetici(calisan):     # yonetici sınıfına calısan sınıfını miras veriyoruz.
    def __init__(self,isim,soyisim,maas,departman,yas, kisi_sayisi):
        print("yonetici sınıfı, yapıcı metodu çalıştı")
        self.isim = isim
        self.soyisim = soyisim
        self.departman = departman
        self.maas = maas
        self.kisi_sayisi = int(kisi_sayisi)
        self.yas = yas

    def prin_base(self):
        for base in self.__class__.__bases__:
            print("miras alınan sınıf :",base.__name__)
    def __str__(self):
        return "{} {} {}".format(self.isim,self.soyisim,self.departman)
yon = yonetici("ahmet","mehmet",9000,"sistem",35,20)
print(yon)
yon.prin_base()
yon.bilgigoster()
yon.zamyap(1234)
yon.departmandegistir("yazılım")

# SONUCLAR
#yonetici sınıfı, yapıcı metodu çalıştı
#ahmet mehmet sistem
#miras alınan sınıf : calisan
#çalısan sınıfına ait bilgiler gosterilmektedir
#isim : ahmet
#soyisim : mehmet
#yas : 35
#maas : 9000
#departman : sistem
#calısanın maaşına zam yapıldı
#ahmet mehmet personelin maası : 9000 tl den 10234 tl ye yukseltildi
#çalısanın departmanı degistirildi
#ahmet mehmet personelin departmanı : sistem departmanından sistem departmanına gecisi saglandı