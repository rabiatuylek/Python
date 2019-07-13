class personel:
    adi = 0
    def kovma(self, personeli_kovma):
        print(self.adi , "adlı personel {} zamanında kovuldu".format(personeli_kovma))
    def al(self,personeli_al):
        print(self.adi,"adlı personel {} zamanında ise alındı".format(personeli_al))
    def guncelleme(self, personel_guncelleme):
        print(self.adi, "adlı personelin {} tane bilgisi guncellendi".format(personel_guncelleme))

per = personel() # yukarıda yazdıklarımızı kullanabilmek için bunu yazmamız gerek.
per.adi = "rabia tuylek"
per.kovma("12.07.2083")
per.al("13.09.2134")
per.guncelleme(5)

# rabia tuylek adlı personel 12.07.2083 zamanında kovuldu
#rabia tuylek adlı personel 13.09.2134 zamanında ise alındı
#rabia tuylek adlı personelin 5 tane bilgisi guncellendi