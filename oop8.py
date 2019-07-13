# __str__ methodu  C# ToString metodunun karsılıgıdır. Class'ın override edilmesi
class personel:
    isim    = ""
    soyisim = ""
    yas     = 0


p = personel()
p.isim = "Rabia"
p.soyisim = "Tuylek"
p.yas = 88
print(p)
# <__main__.personel object at 0x00AFF950>  => ilgili sınıfın ram(hesap) üzerindeki adresini teslim eder.


print(p.isim + " " + p.soyisim)
print(p)
#  Rabia Tuylek
