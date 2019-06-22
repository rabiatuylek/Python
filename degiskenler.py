# print("rabia")
# print(1)
a = 'rabia'
print(a)
sayi = 5
print(type(sayi))
# degisken iki ayri kelimeden olusamaz
# int, float, string
onsalikli_sayi = 4.6
print(onsalikli_sayi)
print(type(onsalikli_sayi))

isim = "rabia tuylek"
print(isim)

isi = "rabia"
soyad = " tuylek"
print(isi + " " + soyad)

fullname = isi + " " + soyad
print("kullanici adi:", fullname)

x = True
y = False
print(x)

print(type(isi))

print(type(x))

# \n bir alt satira gecmek
print((fullname + "\n")*5)




############################################################################################
# int()
## convert : elinizdeki bir veri tipini baska bir veri itipine cevirmek icin kullanilir

sayi1 = input("lutfen sayi girin : ")
sayi2 = input("lutfen sayi girin : ")

sonuc1 = int(sayi1) + int(sayi2)
print(sonuc1)

print(type(sonuc1))
# c charp ve java için string + int oluyor ancak python için string + int olmaz.

print("islem sonucu: " + str(sonuc1))
print(type(sonuc1))





print("islem sonucu: ",sonuc1)
print(type(sonuc1))




print("islem sonucu : " + str(sonuc1))
print(type(sonuc1))

print("""
      bilge
      man
      besiktas""")

# """ bunun ozelligi alt alta satirlar yazabiilirz.

print("bilge adam besiktas istanbul")
########################################


print("bilge adam \"besiktas\" istanbul")
st = "rabia\ttuylek"
print(st)
#int()
#str()
#float()
# CHAR () verdiginiz sayisal degerin , karakter degerini temsil eeder.
# ord() verdiginiz karakter degerinin sayisal ascii kod degerini temsil eder.



print(chr(65),ord('A'))
print(chr(90),ord('a'))
print(chr(97),ord('Z'))
print(chr(122),ord('z'))






