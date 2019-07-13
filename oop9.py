# __str__ methodu  C# ToString metodunun karsılıgıdır. Class'ın override edilmesi
class personel:
    isim = ""
    soyisim = ""
    yas = 0

    def __str__(self):
        return " {} {}".format(self.isim, self.soyisim)

p = personel()
p.isim = "Rabia"
p.soyisim = "Tuylek"
p.yas = 56
print(p)

# str sadece ad soyad çıkartır ve sadece print(p) ile