def decorator_metot(metot):
    def sarmal_metot():
        print("sarmal metot".format(metot.__name__)) # metodun adı ne onu sağlar __name__ metodu
        return metot()
    return sarmal_metot

@decorator_metot    # iki fonk sonucunu birbirine karıstırmaz. ayrı ayrı sonuc verdirir.
def print_metot():
    print("metot calıstı")
print_metot()

# sarmal metot
# metot calıstı  sonucları
