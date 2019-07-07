#metin = "murat vuranok yazılım besiktas"
#sonuc = metin.split(' ',2)
#print(sonuc)
# ['murat', 'vuranok', 'yazılım besiktas']


#metin = "murat vuranok yazılım besiktas"
#sonuc = metin.split()
#print(sonuc)
#['murat', 'vuranok', 'yazılım', 'besiktas']



#metin = "murat vuranok yazılım besiktas hocası "
#sonuc = metin.split(' ',3)
#print(sonuc)
# ['murat', 'vuranok', 'yazılım', 'besiktas hocası ']

#-----------------------------------------------------------------------------------------------------------------------

# .rsplit() icerisine verilen parametreyi sağdan sola doğru ayırma islemi yapar.
#a = "murat, vuranok,yazılım,besiktas hocası "
#sonuc = a.rsplit(' ',2)
#print(sonuc)
#['murat, vuranok,yazılım,besiktas', 'hocası', '']


#-----------------------------------------------------------------------------------------------------------------------

# .splitlines() her bir alt satırda elemanların aralarına [,] karakterini ekler
# not : metin altta yer alan ornek gibi yazıldıysa geçerlidir.

#metin = """
#bilge
#adam
#rabia
#tuylek
#python
#dersleri
#"""
# print(metin.splitlines())
#['', 'bilge ', 'adam', 'rabia', 'tuylek', 'python ', 'dersleri']

# eger parametre olarak sonuna True eklerseniz aralarına [\n] ekler.
#print(metin.splitlines(True))

#-----------------------------------------------------------------------------------------------------------------------


#metin = "bilge adam BESİKTAS"
#print(metin.lower()) # tüm kararkterler kucuk
#print(metin.upper())  # tüm kararkterler buyuk

#bilge adam besi̇ktas
#BILGE ADAM BESİKTAS


#------------------

#metin = "SFfsdfDSGKL"
#result = metin.islower() # tüm kararkterlerin kucuk olup olmadıgını kontrol eder. True / False degerlerini teslim eder islem sonucunda.
#result = metin.isupper() #üm kararkterlerin buyuk olup olmadıgını kontrol eder. True / False degerlerini teslim eder islem sonucunda.
#print(result)
# False

#-----------------------------------------------------------------------------------------------------------------------









































