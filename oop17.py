# ogrenci            : isim,soyisim,okul no, tckn, sınıf, mail, telefon
# ogretmen           : isim, soyisim,        tckn, sınıf ,mail, telefon, maas, brans
# mudur yardımcısı   : isim , soyisim,       ,tckn,      ,mail, telefon,  maas,        ,gorev
# mudur              : isim , soyisim,       ,tckn,      ,mail, telefon,  maas ,       ,gorev
# memur              : isim , soyisim,       ,tckn,      ,mail, telefon,  maas,        ,gorev
# hizmetli           : isim , soyisim,       ,tckn,      ,      telefon, maas,         ,gorev



class base_class:
    isim      = ""
    soyisim   = ""
    tckn      = ""
    mail      = ""
    telefon   = ""
    sınıf     = ""



class calisan:
    maas      = ""
    gorev     = ""


class ogrenci(base_class):
    okul_no   = ""
    sınıf     = ""

class ogretmen(base_class):
    maas     = ""
    brans    = ""
    sınıf    = ""

class mudur_yardımcısı(calisan):
    maas     = ""
    gorev    = ""

class mudur(calisan):
    maas     = ""
    gorev    = ""

class memur(calisan):
    maas     = ""
    gorev    = ""

class hizmetci(calisan):
    maas     = ""
    gorev    = ""


# github tan hocanınkisinden bak.


