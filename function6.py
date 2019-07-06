def mail(ad:str , soyad:str , domain:str = "bilge adam")->str :
    print(ad,soyad,domain)
    return ""
#mail("rabia","tuylek","hotmail")
#print(type(mail("","")))
print(mail("rabia","tuylek","hotmail"))
print("mail metodunun geriye donus tipi:", mail.__annotations__)
#mail metodunun geriye donus tipi: {'ad': <class 'str'>, 'soyad': <class 'str'>, 'domain': <class 'str'>, 'return': <class 'str'>}