



# 1

def toplama(a,b):
    print(a,b)

x = toplama(3,4)
print(x)                     # cevap --->   3 4


# 2

def usselIslem(x = 5, y = 3):
    print(x ** y)                # cevap 125

usselIslem()


# 3

def usselIslem(x = 5, y = 3):
    print(x ** y)
usselIslem(2,4)         # cevap 16


# 4

def myLoop(*args):
    for element in args:
        print(element / 2)

myLoop(3,2,1,5,3,4)  # teker teker 2'ye bölümleri çıkacak
                           # (1.5 , 1 , 0.5 , 2.5 , 1.5 , 2)



# 5


def myFunc(num):
    return num ** 3

myList = [2,3,4,5,6]
for num in myList:
    print(myFunc(num))

# veya ----- map fonksiyonunu

print(list(map(myFunc,myList)))






# 6

barkodDizisi = ["ABC231","SA3123XYZ","XYZA123Q","QRE1231KJ","X112QGL"]

yeniBarkodDizisi = []


for i in barkodDizisi:
    def controlString():
        return "XYZ" in barkodDizisi
    if "XYZ" in i:
        yeniBarkodDizisi.append(i)

print(yeniBarkodDizisi)


# veya ----------- filter fonks.

print(list(filter(lambda string : "XYZ" in string ,barkodDizisi)))





# 7

myVar = "Atil Samancioglu"


def ornekFonksiyon():
    myVar = "Atil"

    def digerFonksiyon():
        print(myVar)
    digerFonksiyon()

print(ornekFonksiyon())


# 8

class Kedi():

    def __init__(self, isim, yas=5):
        self.isim = isim
        self.yas = yas

    def yasiCarp(self):
        return self.yas * 3

kedim = Kedi("Tonton")
kedim.yasiCarp()
print(kedim.yasiCarp())




# 9

class Ogrenci():

    def __init__(self, isim, sinavNotu):
        self.isim = isim
        self.__sinavNotu = sinavNotu

    def notuGoster(self):
        print(f"{self.isim} sınav notu: {self.__sinavNotu}")

ogrenci = Ogrenci("Mehmet",85)

ogrenci.__sinavNotu = 75

ogrenci.notuGoster()



# 10

# Soyut sınıflar ve methodlar oluşturmamıza olanak tanıyan,
# kodlarımızı daha planlı şekilde yazmamızı mümkün kılan
# aynı zamanda büyük projelerde bize
# yapısal olarak fayda sağlayabilecek OOP prensibinin adı nedir?

# cevap : abstraction









