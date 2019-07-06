#kullanıcı dısarıdan dilediği kadar sayi giricek,her sayi girdikten sonra, sayi girmeye devam edip etmeyeceği sorulacak.
# kullanıcı y Y tuşuna basarsa,yeni bir sayi girmesi istenilecek
# kullanıcı harici bir tusa basar ise, iceriye aldıgı sayilar içerisindeki tek sayilar
# içerisinde yer alan en büyük en en küçük sayinin birbirine farkını geriye dönecek.

#def deger(sayi):
#    if deger >= 0:
#        print("tekrar giricek misin")
 #   elif deger == "y" or deger == "Y":
 #       print("yeni bir sayi gir")
 #   else:
 #       deger % 2 != 0



#def farkhesapla():
#    go_on = "y"
#    tek_sayilar = []
#    while go_on == "y" or go_on == "Y":
#        number = float(input("lutfen sayi girin"))
#        if number % 2 != 0:
#            tek_sayilar.append(number);
#        go_on = input("yeni bir sayi eklemek ister misin (Y\\N) :")
#    return max(tek_sayilar) - min(tek_sayilar)
#sonuc = farkhesapla()
#print(sonuc)

# OLMADI EVDE YAP



# kullanıcı dısarıdan string olarak sayi dizi gönderecek
# gelen string degeri geriye sayisal bir dizi olarak döndürünüz.



def converttolist(string):
    mylist = string.split()
    for n in range(len(mylist)):
        if mylist[n].count("."):
            mylist[n] = float(mylist[n])
        else:
            mylist[n] = int(mylist[n])

    return mylist
    print(mylist)
result = converttolist(input("1 2.0 3 4 5 6 7.8 6 5 4"))
print(result)
# tekrar et











