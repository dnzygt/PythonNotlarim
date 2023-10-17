

"""
liste = [1,2,3,4,5]

liste.append(6)
print(liste)
"""
import time

# NESNE TABANLI PROGRAMLAMAYLA KENDİ OBJELERİMİZİ YARATABİLİRİZ


"""

class anahtar kelimesi python da sınıfları oluşturmak için kullandığımız
bir kelime.

bu class lar objeleri oluşturuken, özelliklerini ve metodlarını 
tanımladığımız bir yapı.

"""


# bir araba veri tipi oluşturalım

"""
class Araba():
    model = "Ferrari 911"
    renk = "Kırmızı"
    beygir = 300
    silindir = 8



araba1 = Araba()
print(araba1)

araba2 = Araba()
print(araba2)
"""
"""
print(araba1.model)
print(araba2.renk)
"""

# init foksiyonu

"""
init fonksiyonu pythonda yapıcı bir fonksiyondur
bu foksiyon objeleri oluşturuken otomatik olarak ilk çağırılan fonksiyondur
"""

"""
class Araba():
    model = "Ferrari 911"
    renk = "Kırmızı"
    beygir = 300
    silindir = 8
    def __init__(self):
        print("init foksiyonu çağırıldı")

araba1 = Araba()
"""                    # self'in anlamı objemizi gösteren bir referanstır


"""
class Araba():

    def __init__(self,model,renk,beygir,silindir):
        print("init fonksiyonu çağırıldı")

        self.model = model
        self.renk = renk
        self.beygir = beygir
        self.silindir = silindir


araba1 = Araba("Ferrari 911","Kırmızı",300,8)

araba2 = Araba("Mercedes AMG","Gri",310,8)


print(araba1.model)
print(araba2.model)
"""



class Araba():

    def __init__(self,model = "Bilgi Yok",renk = "Bilgi Yok",beygir = "Bilgi Yok",silindir = "Bilgi Yok"):
        print("init fonksiyonu çağırıldı")

        self.model = model
        self.renk = renk
        self.beygir = beygir
        self.silindir = silindir

araba = Araba(beygir = 200)

print(araba.beygir)