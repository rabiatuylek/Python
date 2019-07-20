class personel:
    baslangıc_maas = 1.400
    def __init__(self,ad,soyad,tel):
        self.ad = ad
        self.soyad = soyad
        self.tel = tel

    def tamadı(self):
        return "{} {}".format(self.ad,self.soyad)
    def tel(self):
        return "+(90){}".format(self.tel)
    def __str__(self):
        return "{} {} {}".format(self.ad,self.soyad,self.tel)


class yazilimci(personel):
    baslangıc_maas = 10.000

    def __init__(self,ad,soyad,tel,yazılımdili):
        super().__init__(ad,soyad,tel)                     # super self.ad = ad yazmamamızı saglıyor.
        # personel.__init__(ad,soyad,tel)  süper metodu ile aynı isi gorur. ama super() size dinamiklik katar.
        self.yazılımdili = yazılımdili


    def __str__(self):
        return "{} {}".format(super().__str__(),self.yazılımdili)  # yukarıdaki class ta yazdık cunku.


per = personel("rabia","tuylek","1345256")
yaz = yazilimci("rabia","tuylek","1345256","python")
print(per)
print(yaz)

#rabia tuylek 1345256
#rabia tuylek 1345256 python

print(issubclass(personel,yazilimci))
# false


