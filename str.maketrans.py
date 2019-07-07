kaynak = "sçöğÇSHFLFĞİ"
hedef = "sdgjIYSChgfdg"

ceviri_rablo = str.maketrans(kaynak,hedef)
print(ceviri_rablo)



metin = "bilge adam bireysel egitimlerde python dersleri"
print(metin)
metin = metin.translate(ceviri_rablo)
print(metin)

# olmadı !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!