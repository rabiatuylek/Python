# dısarıdan aldıgı metin icerisindeki sesli karakterlerin ve sessiz karakterlerin sayisini ekrana yazdıran metot

#def metin(string):
#    sesli = ["a","e","i","o","u","ü","ö"]
#    liste = list(string)
#    seslicount = 0
#    sessizcount = 0
#    for i in liste:
#        if i in sesli:
#            seslicount += 1
#        else:
#            sessizcount += 1
#    print("toplam sesli harf sayisi",seslicount ,"\ntoplam sessiz harfs sayisi",sessizcount)
#metin(input("metin girin"))
# bu zordu anlamaya calis evde.

# dısarıdan aldıgı degere gore kare cizen method


#def kare_ciz(sayi):
#    index = 0
#    while index <= sayi:
#        metin = ""
#        for i in range(sayi + 1):
#            metin += "X  "
#        index += 1
#        print(metin)
#kare_ciz(10)


def kare_ciz(sayi):                           # bu daha basit ve anlasılır.
    index = 0
    while index <= sayi:
        print("X  "* sayi)
        index += 1
kare_ciz(10)


