#sehirler = ["adana","ankara","ardahan","amasya","edirne"]
#for sehir in sehirler:
#    print(sehir)

#i = 0
#while i<len(sehirler):
#    sehir = sehirler[i]
#    print(sehir)
#    i = i + 1

# dizi icerisinde yer alan elemanların ismi icerisinde "m" harfi bulunanların yazdırılması

#sehirler = ["adana","ankara","ardahan","amasya","edirne"]
#for sehir in sehirler:
#    if("m" in sehir):
 #       print(sehir,"bu sehir m harfi içeriyor")
 #   else:
 #       print(sehir,"bu sehir içinde m harfi yok")


# dısarıdan girilen metni harf harf alt alta yazdırınız


#metin = input("lutfen kelime giriniz")
#for a in metin:
#    print(a)

# 10 ile 20 arasındaki asal sayıları yazdır

#a = range(10,20)
#for sayi in a:
#    if sayi>=10 and sayi<=20:
#        if sayi % 2 == 0:
 #           print(sayi,"asal degil")
 #       elif sayi % 3 == 0:
 #           print(sayi,"asal degil")
  #      elif sayi % 5 == 0:
 #           print(sayi,"asal degil")
 #       elif sayi % 7 == 0:
 #           print(sayi,"asal degil")
  #      else:
  #          print(sayi,"asal sayıdır")
#print(a)




#sifrenin 3 defa yanlis girilmesi dahiline kullanıcıyı uyaran uygulama

for i in range(3):
    parola = input("sifre gir")
    if i == 2:  # sifre 3 defa yanlis girildi.
        print("sifrenizi 3 defa yanlıs giridiniz")
    elif not parola:   # alan boş gecilirse
        print("alan bos gecemez")
    elif len(parola) in range (3,8):  # parola 3 ile 8 karakter aralıgında olmalı
        print("parolanız:",parola,"olarak belirlenmistir")
    else:
        print("ya yuh hala dogru sifreni girmedin mi")








