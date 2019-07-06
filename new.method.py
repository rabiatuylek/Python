# 1)
#def hesapla():
#    toplam = 0
#    for sayi in range(1,1001):
#        toplam += sayi
#    print(toplam)
#hesapla()

# yukarıdaki önemli bir örnek tekrar yap. sonuc 500500

# dısarıdan girilen 2 sayinin toplamını ekrana yazdırma
# kural 1 kesinlikle method icerisinde parametrenin nerden geleceği tanımlanmaz.
# metot içinde parametreye değer atanmaz.
#def hesapla(sayi1 , sayi2):
    # sayi1 = int(input("1.sayi"))
    # sayi2 = int(input("2.sayi"))   bunlarlada olur.
#    toplam = sayi1 + sayi2
#    print(toplam)
#hesapla(3,4)



# dısarıdan aldıgın isim ve soyisime gore mail adresi olusturun.


def mail(isim , soyisim = None):
    if soyisim is None:
        a = isim + "@bilgeadam.com"
    else:
        a = isim.lower() + "." + soyisim.lower() + "@bilgeadam.com"
    print(a)
mail(input("lutfn ad gir"))
mail(input("lutfen ad gir"), input("soyad gir"))
# yaptın, oldu.
# none anlamı kullanıcı soyismini yazmayabilir.





