class employee:
    '''
 Personel tanımlama
 Personeli Tanımla
    '''
    firstname = ""
    lastname = ""
    department= ""
    mail = ""
    phone = ""

# employee sınıfından instance ( yeni bir örnek) almak
personel = employee()
personel.mail = "ba@hotmail.com"
personel.department = "yazılım"
personel.firstname = "rabia"
personel.lastname = "tuylek"
print(personel)
print(personel.firstname,personel.lastname)
#<__main__.employee object at 0x011AF0F0>         ram daki adresidir o sayılar.
#rabia tuylek
# eger sınıfı direkt olarak yazdırırsak bize, o sınıfın adı ve hesap üzerindeki adresi teslim eder.
