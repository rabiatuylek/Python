# .index() , .rindex(), .find() , .rfind()

metin = "bilge adam besiktas yazılım dersleri"
sonuc = metin.index("a") # verilen kararkteri metin icerisinde soldan saga doğru arama islemi yapar.
# belirtilen kararkter var ise index degerini , yok ise vluererror.
print(sonuc)
# 6

metin = "bilge adam besiktas yazılım dersleri"
sonuc = metin.rindex("a")
print(sonuc)      # sagdan sola dogru arama islemi yapıyor.


