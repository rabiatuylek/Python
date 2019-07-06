# disaridan bir sayisal dizisinin parametre olarak alan bir metot yaziniz.Metot, parametredeki dizide yer alan
# elemanların toplamının karekökünü dondursun.
# import  math
import math
def karekok(sayilar):
    toplam = 0
    for sayi in sayilar:
        toplam += sayi
    return math.sqrt(toplam)

sonuc = karekok([1,2,3,4,45,68])
print("islem sonucu:",sonuc)