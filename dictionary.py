# Dictionaries
# dictionary key value formatında dataları listelemek için kullanılır.

personeller = [
    {
        "ıd" : 1,
        "ındex":0,
        "firstname": "rabia",
        "lastname" : "tuylek"
    },
    {
        "ıd" : 2,
        "ındex": 1,
        "firstname": "er",
        "lastname": "adamm"
    }
]
#print(personeller[0])
#personeller[2]["firstname"] = "okan"
#print("personel adı:",personeller[2]["firstname"], "olarak güncellendi")

guncellenecekIndex = 1
guncellenecekKey = "firstname"

oldname = personeller[guncellenecekIndex][guncellenecekKey]
personeller[guncellenecekIndex][guncellenecekKey] = "okan"
print(oldname,"yeni ad:", personeller[1]["firstname"],"olarak guncellendi")

personeller.append({"ıd":3, "ındex": 2, "firstname": "mehmet", "Lastname":"bakan"})
print(personeller[:])
#bu kodlar guzelce calısıyor. Evde daha iyi anla.
print("personel adı:", personeller[0]["firstname"], "\npersonel soyadı:",personeller[0]["lastname"])

# eger format icerisinde index degeri belirtilmezse default olarak 0,1,2,,,, gibi devam eder.

