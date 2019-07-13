from datetime import datetime
from datetime import timedelta
class personel:
    firstname = ""
    lastname  = ""
    mail = ""
    phone = ""
    hiredata = "{}/{}/{} {}:{}".format(datetime.now().year,datetime.now().month,datetime.now().day,datetime.now().day,datetime.now().hour,datetime.now().minute)
    firedays = 0
    adress = ""

    def iseAl(self):
        print("personel adı :{}\nPersonel Soyadı :{}\npersonel mail : {}\npersonel phone : {}\npersonel ise giris : {}\npersonel adres : {}\npersonel sozlesme bitis : {}".format (
            self.firstname,
            self.lastname,
            self.mail,
            self.phone,
            self.hiredata,
            self.adress,
            100))
    def guncelle(self):
        # personel bilgilerini güncelleme
        pass
    def kov(self,ıd):
        # personeli veri tabanından silme
        # status = 3
        pass

time = datetime.now()
pers = personel()

pers.firstname = "Rabia"
pers.lastname = "Tuylek"
pers.mail = "rabiatuylek@hotmail.com"
pers.phone = "+901234567"
pers.hiredata = "{}/{}/{} {}:{}".format(time.year,time.month,time.day,time.day,time.hour,time.minute)
pers.firedays = 150
pers.adress = "İstanbul / Besiktas "

pers.iseAl()
#personel adı :Rabia
#Personel Soyadı :Tuylek
#personel mail : rabiatuylek@hotmail.com
#personel phone : +901234567
#personel ise giris : 2019/7/13 13:13
#personel adres : İstanbul / Besiktas
#personel sozlesme bitis : 100


# hocanın github ından bak.
# bu en zor örnek , kodlaya kodlaya oturucak.
