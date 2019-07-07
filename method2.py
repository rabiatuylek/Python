# .capitalize() parametrede verilen değerin ilk harfini büyük olarak değiştirir.

#isim = "rabia".capitalize()
#print(isim)
# Rabia

# .title() metin içerisinde yer alan tüm ayrık kelimelerin ilk harfini büyük olarak teslim eder.
#isim = "rabia tuylek"
#print(isim.title())



# sorted()  dizi içerisinde yer alan elemanları A dan Z ye , 0 dan 9 a sıralama yapar.

#sonuc = sorted("bilgeadam")
#print(sonuc)
# ['a', 'a', 'b', 'd', 'e', 'g', 'i', 'l', 'm']
# alfabetik sıraya gör degil Ascii kod üzerinden devam eder.
# türkçe harfleri en sona atar.

#import locale
#locale.setlocale(locale.LC_ALL,"turkish_Turkey.1254")  # windows için   BUNUN AMACI NE TAM OLARAK
#sonuc = sorted("bilge adamç")
#print(sonuc)
#[' ', 'a', 'a', 'b', 'd', 'e', 'g', 'i', 'l', 'm', 'ç']



# .reverse() elimizde var olan metni yada dizi gibi nesneleri sıralama yapmadan tersine cevirme islemi yapar.
#sayilar = [1,2,3,4,5,6,7,8]
#karakterler = ["a","b","c"]
#metin = "bilge adam"

#sayilar.reverse()
#karakterler.reverse()
#print(sayilar)
#print(karakterler)

#[8, 7, 6, 5, 4, 3, 2, 1]
#['c', 'b', 'a']




# .split() icerisinde verilen parametreye göre soldan sağa doğru ayırma islemi gerçekleştirir.
#elemanlar = "yazılım,sistem,teknik çizim,web grafik"
#elemanlar = elemanlar.split()
#print(elemanlar)
# ['yazılım,sistem,teknik', 'çizim,web', 'grafik']

#elemanlar = "yazılım,sistem,teknik çizim,web grafik"
#elemanlar = elemanlar.split(",")
#print(elemanlar[:])
#['yazılım', 'sistem', 'teknik çizim', 'web grafik']









