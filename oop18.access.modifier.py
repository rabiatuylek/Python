class cup1:
    def __init__(self):
        self.color = None       # public variable
        self.content = None     # public variable

    def fill(self,beverage):
        self.content = beverage

    def empty(self):
        self.content = None

    def __str__(self):
        return self.color + " "+ self.content

cup = cup1()
cup.color = "red"
cup.content = "tea"

print(cup)
cup.empty()
cup.content = "coffee"
print(cup)

#red tea
#red coffee

# bunu evde anlamaya calıs.


class cup2():
    def __init__(self):
        self.color = None          # public variable
        self._content = None       # protected variable _ olması farkından dolayı
# korumalı üye, c# gibi dillerde miras alınan sınıflarda gorunsede python dilinde tek bir _ çizgisi vardır.

    def fill(self,beverage):
        self._content = beverage

    def empty(self):
        self._content = None

    def __str__(self):
        return self.color + " " + self._content

cu = cup2
cu.color = "blue"
cu._content = "tea"
print(cu)























class cup3():
    def __init__(self,color):
        self._color = color          # protected variable
        self.__content = None       # prite variable __ olması farkından dolayı
# korumalı üye, c# gibi dillerde miras alınan sınıflarda gorunsede python dilinde tek bir _ çizgisi vardır.

    def fill(self,beverage):
        self.__content = beverage

    def empty(self):
        self.__content = None

    def __str__(self):
        return self._color + " " + self.__content

cuppa = cup3("blue")
cuppa._cup3__content = "tea"
print(cuppa)

#hepsinin çıktısı
#red tea
#red coffee
#<class '__main__.cup2'>
#blue tea













