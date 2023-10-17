# FONSİYONLAR

"""

def fonksiyon_adı(parametre,parametre2,...(opsiyonel)):
    #fonsiyon bloğu
    Yapılacak işlemler
    # dönüş değeri - opsiyonel

"""
"""
def selamla():
    print("Merhaba...")
    print("Nasılsınız?")
"""
"""
type(selamla)
function 


selamla()
"""

# PARAMETRELER VE ARGÜMANLAR

"""
def selamla(isim):
    print("isminiz:",isim)
    print("Merhaba",isim,"nasılsın?")

selamla("Kemal")

"""

"""
def toplama(a,b,c):
    print("Toplamları:",a+b+c)

toplama(1,2,3)
"""

# faktöriyel hesaplama

"""

sayı = int(input("Faktöriyel hesaplaması için sayınızı giriniz:"))
def faktöriyel(sayı):
    faktöriyel = 1
    if (sayı == 0 or sayı == 1):
        print("Faktöriyel:",faktöriyel)
    else:
        while (sayı >= 1):
            faktöriyel *= sayı
            sayı -= 1
        print("Faktöriyel:",faktöriyel)

print(faktöriyel(sayı))
# print sonrası none işareti çıkıyor


"""



# RETURN İFADESİ

"""
def toplama(a,b,c):
    print("Toplamları:",a+b+c)
def üskare(a):
    print("Karesi:",a**2)


print(üskare(toplama(3,4,5)))  # ifadesi hata verir.
"""
"""
def toplama(a,b,c):
    return a+b+c
def üskare(a):
    return a**2
print(üskare(toplama(3,4,5)))   # return ifadesi ile fonsiyonları
                                         # istenilen şekilde kullanabiliriz.
"""


# girdili deneme


# RETURN İFADESİNDEN SONRA YAZILAN İŞLEMLER ÇALIŞMAZ.
# RETURN SON İFADEDİR.


"""
def toplama(*a):
    
    return a + a

toplama(4,3,2)

"""



# ARGÜMANLAR

#args, kwargs (arguments,key word arguments)



"""
def args_sum(*args):
    return sum(args)

args_sum(4,5,3)

print(args_sum(4,5,3))
"""

# ders 42 fonksiyon


"""
def kwargs_ex(**kwargs):
    print(kwargs)

kwargs_ex(apple = 100 , banana = 150 , melon = 200)

def kwargs_ex(**kwargs):
    if "apple" in kwargs:
        print("elma")
    else:
        print(":(")

kwargs_ex(apple = 100)
kwargs_ex(banana = 150)
"""


# ders 42

"""
def divideNumber(number):
    return number / 2

myList = [3,5,7,10,20,30]
myResultList = []

for num in myList:
    myResultList.append(divideNumber(num))

print(myResultList)



# MAP


# map bir sınıf.

# yukarıdaki divideNumber fonksiyonunun kullanımını map ile gösterelim

print(list(map(divideNumber,myList)))

# şeklinde çıktısını  alabiliriz.


"""


# liste içindeki verileri kontrol etmek



def controlString(string):
    return "Deniz" in string

print(controlString("deniz"))

myList = ["Deniz","DENİZ","deniz","Deniz Yiğit"]

print(controlString(myList))

print(list(map(controlString,myList)))





"""
# filter  --->  filtrelemek

print(list(filter(controlString,myList)))
"""

"""
# lambda

cokluLambda = lambda num : num * 3  # <---- AYNI

print(type(cokluLambda))

print(cokluLambda(20))

def coklu(num):                  # <-----     AYNI
    return num * 3
print(coklu(20))
"""



# GLOBAL VE LOCAL DEĞİŞKEN    VEYA KAPSAM

"""
#Global
myString = "Deniz"

def myFunction():
    #Enclosing
    myString = "Deniz 2"
    print(myString)

    def myFunction2():
        #Local
        myString = "Deniz 3"
        print(myString)

    myFunction2()


print(myString)
print(myFunction())
"""













