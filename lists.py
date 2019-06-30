# Tanımlama sekli
# bir dizinin maximum index degeri, eleman sayisinin bir eksi degeridir.
#sehirler = ["ankara","edirne","eskisehir","istanbul","kars","kayseri","adana"]
 # eleman sıra no  : 1,2,3
 # eleman index no : 0,1,2

#print(sehirler[0])
#index = len(sehirler)-1
#print(sehirler[index])
#print(sehirler[2:4])# 1parametrede verilen deger index degeridir 2parametrede ise ekrana yazdırılacak olan eleman sayısı
#print(sehirler[:])
# 1)  .append() dizi içerisine eleman eklemek için kullanılır.
# append dizinin sonundan baslar, eklenen her bir eleman dizinin son elemanıdır.
sehir = []
sehir.append("ankara")
sehir.append("edirne")
sehir.append("istanbul")
print(sehir[:])

# 2)  .insert() dizinin içerisinde beliritlen alana ekleme islemi yapar

sehir.insert(1,"rize")
print(sehir)
# 1.parametre hangi index degerine
# 2.parametre o index degerine hangi eleman eklenecek  ?

# 3)  .count() dizi içerisinde yer alan elemanların liste icerisinde kac defa gectiğini teslim eder

sehir.append("izmir")
sehir.append("istanbul")
print(sehir)
print("dizi içerisinde istanbul", sehir.count("istanbul"),"adet içermektedir")






# 4) .pop() dizi içerisinde eleman silme, parametre verilirse , verilen idex degerindeki parametreyi siler eger verilmezse dizinin en son elemaını siler.
#  .pop() metodunun özelliği silinen elemanı geriye teslim eder.

#sehir.pop()
#print(sehir)

#sehir.pop(2)
#print(sehir)

# 5) .remove() metodu dizi içerisinden eleman silme, eleman silmek için objeckt olarak 2 nesne ister (pop index mantığı ile remove ise,object mantıgı ile calisir.
#sehir.remove("istanbul")
#print(sehir) # ilk buldugu istanbul degerini isler.
# .remove metodu geriye eleman teslim etmez.

# 6) .sort() dizinin elemanlarını A dan Z ye > 0 dan 9 a sıralama islemi yapar.
print(sehir[:])
sehir.append("zonguldak")
sehir.sort()
print(sehir[:])

# 7) .reverse() dizi içerisindeki elemanları tersine çevirir.kesinlikle sıralama islemi yapmaz. diziyi oldugu gibi tersten yazdırır.
#sehir.reverse()
#print(sehir)
print(len(sehir))
print(sehir[:])
#del sehir
#print(sehir[1:4]) # liste silinmişti del ile. bu kod calısmaz artık böyle bir list yok.






