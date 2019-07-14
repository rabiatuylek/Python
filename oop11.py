# init
class personel:
    isim = ""
    soyisim = ""
    yas = 0

    def __str__(self):
        return "{} {}".format(self.isim,self.soyisim)
    def __init__(self,firstname,lastname,age):
        self.isim = firstname
        self.soyisim = lastname
        self.yas = age

# __init__ metodu old dolayı, artık aşağıdaki kullanım sekli çalısmaz.
#per = personel() # instance = per
#per.isim = "rabia"
#per.soyisim = "tuylek"
#per.yas = 100
#print(per)


employee = personel("rabia","tuylek",100)
print(employee)
# rabia tuylek  = sonuc bu

