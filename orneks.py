# asagıda yer alan dosyalar icerisinde .png olanların sayısını ekrana yazdırın.

file1 = "ba.png"
file2 = "ba.ghf"
file3 = "na.mp3"
file4 = "ba.png"
file5 = "ba.tff"
file6 = "ba.hfj"
file7 = "ba.gjr"
file8 = "ba.bvn"
file9 = "ba.ref"
file10 = "ba.png"

def kontrol(*param):
    toplam = 0
    for i in param:
        result = i.endswith(".png")
        if result :
            toplam += 1
    return toplam
toplam1 = kontrol(file1,file2,file3,file4,file5,file6,file7,file8,file9,file10)
print(toplam1)

# 3
# EVDE KESİN TEKRAR



# .swapcase() metin içerisinde yer alan büyük karakterleri küçük, küçük karakterleri ise büyük harfe cevirir.







# .strip() metin basındaki veya sonundaki karakteri silmek için kullanılır.
metin = "bilge adam"
metin = metin.strip(" ")
print(metin)
print(len(metin))

metin = "bilge adam"
metin = metin.lstrip() # soldaki boslugu siler.
print(len(metin))

metin = "bilge adam"
metin = metin.rstrip() # sağdaki boslugu siler.
print(len(metin))




