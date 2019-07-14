a = 40 # degeri 40 olan sayisal bir <class 'int'> tipinde bir degisken tanımladık.
b = a # b degiskeni tanımlayıp referansını a degiskeninden aldık.
c = [b] # c degiskeni tanımlayıp <class 'list'> b degerini referans olarak verdik.


print(type(a))
print(a)

del a
b = 100
print(b)
c[0] = -1
print(c[:])

#<class 'int'>
#40
#100
#[-1]




class point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "hesap uzerinden silindi")

pt1 = point()
pt2 = pt1
pt3 = pt2

print(id(pt1),id(pt2),id(pt3))   # nesnenin ram adresi degerinin ekrana yazdırılması

#4915024 4915024 4915024
#point hesap uzerinden silindi


######################################

class point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "hesap uzerinden silindi")

pt1 = point()
pt2 = pt1
pt3 = pt2

del pt1
print(id(pt1),id(pt2),id(pt3))   # nesnenin ram adresi degerinin ekrana yazdırılması
# pt1 tanımlanmadı diyecek


# id() nesnenin kimliğini döndürür. nesne yasam omru boyunca benzersiz ve sabit olacağı garantilenen (uniq) bir tam sayıdır. birbirinden
# benzersiz iki nesne aynı degere sahip olabilirler.