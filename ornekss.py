
# BU SAYFA BREAK METODU
#while True:   # sonsuz dongu , sonsuza kadar devam edicek. devamlı calısma sürecek.
#    sifre = input("lutfen sifre gir:")
 #   if not sifre:
 #       pass
 #   elif len(sifre) in range(3,8):
 #       print("yeni sifremiz:",sifre)
 #       break
 #   else:
  #      print("sifre 3 ile 8 karakter aralıgında olmalıdır")



  # break anahtar kelimesi durdurur.DONGUYU SONLANDIRIR

index = 5
while True:
    if index ==5:
        print(index)
        print("istenilen degere ulasıldı")
        break
    print(index)
    index += 1

