# dısarıdan aldıgı degerlerin toplamını geriye donen method

def hesapla(sayi1, sayi2):
    toplam = sayi1 + sayi2
    return toplam   # metot sonucunda geriye döndurmek istedigimiz deferi, return anahtar kelimesinin onune ekliyoruz.
print("islem sonucumuz :",hesapla(5,7))


def hesapla(sayi1, sayi2):
    toplam = sayi1 + sayi2
    print(toplam)
hesapla(4,5)    # aradaki fark anlasıldı. return yazdığında onune eklediğimiz şey printte yazılmıyor.
