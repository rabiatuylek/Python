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

pers = calisan("murat", "vuranok", 5000,"besiktas", 40)
print(pers)
pers.bilgigoster()
pers.zamyap(10000)
pers.departmandegistir("kadıkoy")

# SONUCLAR
#çalısan sınıfına ait bilgiler gosterilmektedir
#isim : murat
#soyisim : vuranok
#yas : 40
#maas : 5000
#departman : besiktas
#calısanın maaşına zam yapıldı
#murat vuranok personelin maası : 5000 tl den 15000 tl ye yukseltildi
#çalısanın departmanı degistirildi
#murat vuranok personelin departmanı : besiktas departmanından besiktas departmanına gecisi saglandı

# HOCANIN YAZDIKLARI
# personel,in maasına zam yapıldıgında veya departman degistirildiğinde, kullanıcıya eski deger ve yeni degerleri gosterin

# x personelinin departmanı : s departmanından y departmanına gecis saglandı
# x personelinin maası : x tl den y tl ye yukseldi.


