# KARAR YAPILARI , if elif else
# karsılastırma operatorleri
# == soldaki deger sagdaki degere esit
# != soldaki deger sagdakine esit degil ornek olarak 4 != 3 sonucu true
# < , >
# =< kucuk yada esit
# => buyuk yada esit
# 1>= 1 sonuc true (esitlik)

#num = input("lutfen kullanıcı adınızı girin:")
#num = num.lower().replace("ı","i").replace("ç","c").replace("ö","o")
#print(num)
#if num == "admön":
 #   print("giris yapiniz")
#else:
 #   print("kullanıcınız hatali")    # STRİNG E ESİTLEDİĞİMİZDEN YAZDİGİMİZİN AYNİSİNİ SONUCTA YAZARSAK BİZE GİRİS YAPTINIZ DER SADECE TEK KOSULLA DOGRULUK !

#ornekler

#try:
 #   not_degeri = int(input("deger giriniz"))
   # if not_degeri < 0:
   #     print("0 dan kucuk not giremezsiniz")
    #elif not_degeri > 100:
     #   print("100 den buyuk deger giremezsiniz")
    #else:
     #   print("notunuz",not_degeri)
#except ValueError as exp:
 #   print("lutfen sayisal veri girin:")
#except Exception as exp:
 #   print("belirlenemeyen bir hata")



#try:
 #   sayi = int(input("lutfen sayi giriniz:"))
 #   if (sayi % 2 == 0):
  #      print("cifttir")
   # elif ((sayi % 2 != 0)):
    #    print("tektir")
#except Exception as hata:
 #   print(hata)
  #  print("sayi girmek ne kadar zor olabilir ki kardess")




# len() uzunlugu temsil eder.


#kelime = len(input("lutfen kelime giriniz"))
#if kelime >= 8 :
 #   print("onaylandi")
#else:
 #   print("daha uzun sifre gir")



#user_name = input("lutfen kullanıcı girin")
#password = input("lutfen sifre gir:")

#if user_name == "admin":
    #if password == "123":
   #     print("giris yaptiniz")
  #  else:
 #       print("sifreniz yanlis")
#else:
 #   print("kullanıcı adiniz yanlis")
#if user_name == "admin" and password =="123":
 #   print("tebrikss")
#else:
 #   print("tekrar baakkk")



# and sorguya katilan her bir kosulun saglanmasi
# or sorguya katilan herhangi bir kosulun saglanmasi
# not olumsuzluk katar true ise false , false ise true yapar

# ANOTHER EXAMPLE


not_ = int(input("lutfen notu gir:"))
if not_ > 0 and not_ <= 30:
    print("harf notunuz" + " " + "FF")
elif not_ > 30 and not_ <= 50:
    print("DD")
elif not_ > 50 and not_ <= 70:
    print("CC")
elif not_ > 70 and not_ <= 85:
    print("BB")
elif not_ > 85 and not_ <= 100:
    print("AA")
else:
    print("hatali deger")





urun = input("lutfen  ürünü adi soyleyin:")

if urun == "domates" or urun == "biber" or urun == "patlican":
    print("manav urun girdiniz")
elif urun == "dis macunu" or  urun == "parfum":
    print("kozmetik urun")
elif urun == "pc" or urun == "tablet":
    print(" tekno")
else:
    print("stok yok")

# .replace() ing harfe cevirir



kitap_sayi = int(input("lutfen kitap miktarını giriniz"))
toplam = kitap_sayi * 5
if kitap_sayi > 0:
    if kitap_sayi<=20:
        print("sonuc",toplam -(toplam*0.05))
    elif kitap_sayi>20 and kitap_sayi<=50:
        print("sonuc",toplam - (toplam * 0.10))
    elif kitap_sayi>50 and kitap_sayi<=100:
        print("sonuc",toplam -(toplam*0.15))
    else:
        print("sonuc",toplam -(toplam*0.25))










