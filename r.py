#a = 23
#print(a)
#b = ("hi")
#print(b)
# programcı hataları (error)
# program kusurları (bug)
# istisnalar (exceptions)
# mantıksal hatalar (logical arrays)


#try:
    #telefon_numarasi = int(input("lutfen numara gir:"))
    #print("telefon numaranız :", telefon_numarasi)
# hatalı bir seyler yazılabilir bu gibi durumlarda try icine yazilir.
#except ValueError:
    #print("islem hatasi")
   # print(int(input("lutfen gecerli bir sayı girin:")))
#except ZeroDivisionError:
    #print("islem hatasi")
   # print("sıfıra bolunme hatasi")




# try ve except beraber yazılır BİR KALIPTIR.



#try:
    #sayi_bir = int(input("lutfen birinci sayiyi gir:"))
    #sayi_iki = int(input("lutfen ikinci sayiyi giriniz:"))

    #toplam = sayi_bir + sayi_iki
    #fark = sayi_bir - sayi_iki
    #bolum = sayi_bir / sayi_iki
    #carpım = sayi_bir * sayi_iki

    #print( "sayıların toplamı:",toplam,
         # "\nsayıların farkı:",fark,
         # "\nsayıların bolumu :", bolum)
#except ValueError:
    #print("value error hatasi yada sytanx error")
#except ZeroDivisionError:
    #print("zero division hatasi")
#except:
    #print("islem hatasi")

#try:
    #sayi = int(input("sadece sayisal veri giriniz:"))
    #print("gelen sayi",sayi)
    #sayi = sayi / 0
#except ValueError as ex:
 #   print("Value Error")
 #   print("hata",ex)
#except ZeroDivisionError as ex:
 #   print("Zero Division error")
  #  print("hatali",ex)
#except Exception as ex:
 #   print("except")
  #  print("hata var",ex)




try:
    sayi_bir = int(input("lutfen bolunecek sayiyi girin"))
    sayi_iki = int(input("lutfen bolecek olan sayiyi giriniz:"))


except ValueError as exp:
    print("islem hatasi",exp)
else:
    try:
        print(sayi_bir / sayi_iki)
    except ZeroDivisionError:
        print("sayi 0 degerine bolunemez.")




try:
    sayi = int(input("sayi giriniz:"))
    print("tebrikler")
except:
    print("hata aldik")
finally:
    print("her islem sonucusuda calisir.")
    #connection.close()







