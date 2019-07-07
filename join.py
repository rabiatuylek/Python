# .join metinsel degerleri birbirine eklemek icin kullanılır , seperator verilebilir.
#metin = list(input("lutfen gir"))
#print("-".join(metin))
# r-a-b-i-a-t-u-y-l-e-k

#-----------------------------------------------------------------------------------------------------------------------

# .count() metin yada dizi icerisinde parametrede verilen degerin, adet bilgisini teslim eder.

#metin = "bilge adam besiktas"
#sonuc = metin.count("b")
#print("metin içinde bundan",sonuc, "tane vardır")
#print("metin içerisinde verdiğiniz parametre {} adet içermektedir".format(sonuc))
#metin içinde bundan 2 tane vardır
#metin içerisinde verdiğiniz parametre 2 adet içermektedir






#metinler = ["ankara","edirne", "ankara"]
#son = metinler.count("ankara")
#print(son)
# 2





a = "rabia tuylek"
son = a.count("a")
print(son)
son =a.count("a",2)  # arama islemine 2.indexten basla.
print(son)




metin = "bilge adam besiktas yazılım dersleri, klima on tarafı sogutmuor"
son = metin.count("a",6,9) # 6 dan başlayarak 9 a kadar git. (index degeri yani)
print(son)