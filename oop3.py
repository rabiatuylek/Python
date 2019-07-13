class ogrenci:

    '''
    self : sınıf içerisinde yer alan metotların , diğerlerinden farkı hangi sınıf içerisinde çalıştıgını belirtmesidir.
    Self anahtar kelimesini vererek metodun bu sınıf içerisinde çalıştıgını belirtmiş oluruz. Tanımlama yapılırken eklenir
     fakat kullanım sırasında python bunu bizim için kendisi yapacaktır.
    '''
    adi = ""
    def Notver(self,ogrenci_not):
        print(ogrenci_not, "adlı ogrenciye not verildi")
    def cezaver(self,ogrenci_ceza):
        print(ogrenci_ceza,"ceza verildi")
    def yoklamagir(self,ogrenci_yoklama):
        print(ogrenci_yoklama,"yoklama girildi")

# kullanım yöntemleri:
# class içerisinde tanımlanmış metotlara ulaşma
# 1)
ogrenci.Notver("","70")
ogrenci.cezaver("","disiplin")
ogrenci.yoklamagir("","geldi")

#70 adlı ogrenciye not verildi
#disiplin ceza verildi
#geldi yoklama girildi

########################################################################################################
# 2)
Ogrenci = ogrenci()
Ogrenci.adi = "rabia tuylek"
Ogrenci.Notver("rabia tuylek")


