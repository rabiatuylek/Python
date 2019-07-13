class ogrenci:

    '''
    self : sınıf içerisinde yer alan metotların , diğerlerinden farkı hangi sınıf içerisinde çalıştıgını belirtmesidir.
    Self anahtar kelimesini vererek metodun bu sınıf içerisinde çalıştıgını belirtmiş oluruz. Tanımlama yapılırken eklenir
     fakat kullanım sırasında python bunu bizim için kendisi yapacaktır.
    '''
    adi = ""
    def Notver(self,ogrenci_not):
        print(self.adi, "adlı ogrenciye {} notu verildi".format(ogrenci_not))
    def cezaver(self,ogrenci_ceza):
        print(self.adi,"adlı ogrenciye {} cezası verildi".format(ogrenci_ceza))
    def yoklamagir(self,ogrenci_yoklama):
        print(self.adi,"adlı ogrenci derse {}".format(ogrenci_yoklama))




Ogrenci = ogrenci()
Ogrenci.adi = "rabia tuylek"
Ogrenci.Notver(50)
Ogrenci.cezaver("disiplin")
Ogrenci.yoklamagir("geldi")



#rabia tuylek adlı ogrenciye 50 notu verildi
#rabia tuylek adlı ogrenciye disiplin cezası verildi
#rabia tuylek adlı ogrenci dersegeldi


