# dısarıdan girilen degerin, tek veya cift olma durumuna göre geriye deger dönen metot, sayı cift ise : -1 , tek ise : 1, sıfıra esit
# ise : 0 degerini teslim etsin.

#def deger(sayi):

 #   if sayi == 0:
 #       cift += 2
 #       r = 0
 #   elif  sayi % 2 == 0:
 #       r = -1
 #   else:
 #       r = 1
 #   return r
#print(deger(int(input("lutfen sayi degeri girin :"))))
#yadaa
#deger(int(input("lutfen sayi degeri girin :")))
#print(r)




# disaridan girilen ilk kelimenin ilk iki harfi büyük, geri kalanı kucuk alınız.
# ikinci kelimenin icerisinde gecen tum a lari e ile degistiriniz.
# ve sonuna @hotmail.com ekleyerek geri dondururuz.


def Mail(isim , soyisim):
     isim_ = str(isim[0:2]).upper()  + str(isim)[2:].lower()
     soyisim_ = soyisim.replace("a","e")
     return "{}.{}@hotmail.com".format(isim_,soyisim_)
mail = Mail("rabia","tuylek")
print("mail adresiniz", mail)

# bu ornek zordu evde bak KESİNLİKLE BAK.















