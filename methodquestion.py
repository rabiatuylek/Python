# dısarıdan girilen metin içerisinde yer alan tüm karakterlerin ascii kod değerlerinin toplamını bulunuz.

a = print(ord("A",))   # karakterin ascii kod karsılıgını temsil eder.
b = print(ord("B"))


def metintoplama(string):
    havuz = 0
    liste = list(string)
    for i in liste:
        havuz +=ord(i)  # bu kısım çok önemli
    return havuz
metin =input("lutfen gir")
result = metintoplama(metin)
print(result)



