# dısarıdan gelecek olan parametre sayisi belirsiz olan durumlar için kullanılan metot örneği

#def hesapla(*sayilar):    # başına * koyduğumuz an altta istediğimiz kadar sayi ekleyebiliriz.parametre sayisinin belirsiz old. gösterir.
#    toplam = 0
#    for i in sayilar:
#        toplam += i
#    return toplam
#result = hesapla(1,2,3,4,5,6,7,8,9,10,11,12,13)
#print(result)




# metot(ad,soyad,telefon,gorev)
# metot(*parametreler):

#def metot(ad,soyad,telefon,gorev,*par):
 #   print(ad,soyad,telefon,gorev,par)


#def metot1(*parametreler):
 #   print(parametreler)

#metot("rabia","tuylek","344","dasn",34,3,45,3,56,567,7,9)
#metot1("rabia","tuylek","344","dasn")

#rabia tuylek 344 dasn (34, 3, 45, 3, 56, 567, 7, 9)
#('rabia', 'tuylek', '344', 'dasn')





#def metotvol1(**params):
#    print(params)

#metotvol1(ad = "rabia", soyad = "tuylek", tel = "34556", mail = "hotmail")

#{'ad': 'rabia', 'soyad': 'tuylek', 'tel': '34556', 'mail': 'hotmail'}





#def metotvol1(**params):
#    print(params["ad"])

#metotvol1(ad = "rabia", soyad = "tuylek", tel = "34556", mail = "hotmail")
#rabia



def kayitlar(**params):
    print("-"*25)
    for key.value in params.items():
        print("{0:<7}:{1}".format(key,value))
    print("-"*25)

kayitlar({
    ad = "rabia",
    soyad = "tuylek",
    tel = "34556",
    mail = "hotmail"})   # bu olmadı









