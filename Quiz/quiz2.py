





# 1

x = 5
y = 3
z = 6
print(x > y and z > x)



# 2

print(x < y or z > y)


# 3

yas = 20

if yas < 18:
    print("18 yaşından küçüksünüz!")
elif yas >= 18 and yas < 30:
    print("18 ile 30 yaş arasında bir gençsin.")
elif yas >= 30 and yas < 40:
    print("30 ile 40 yaş arasındasın yaşlı seni.!")
else:
    print("40 yaşından büyüksün yaşlı seni...")


# 4

myDictionary = {"k1":10,"k2k":"a","k32":30,"k4":"c"}

for i in myDictionary.values():

    if i == "c":
        print("Bu sözlük içerisinde c vardır.")

# veya

if "c" in myDictionary.values():
    print("Evet")


# 5

myOtherDictionary = {"b":203,"c":"a","a":400,"d":"f"}

for i in myOtherDictionary.keys():

    if i == "a":
        print("Bu sözlük içerisinde a vardır.")



# 6


myNumbers = [1,2,3,4,5,6,19,20,32,21,20,1111,23,24]

for i in myNumbers:

    if i % 2 == 0:

        print(i)


# 7

rList = [3,2,5,8,4,6,9,12]

for r in rList:
    cevreList = []

    pi = 3.14
    cevre = 2*pi*r

    cevreList.append(cevre)
    print(cevreList)




# 8

ageNameList = [("Ahmet",30),("Ayşe",24),("Mehmet",40),("Fatma",29)]

ageNameList1 = []
for (i,y) in ageNameList:
    ageNameList1.append(y)
print(ageNameList1)

# veya

yasListe = []
for (isim,yas) in ageNameList:
    yasListe.append(yas)
print(yasListe)



# 9

metalList = ["Metallica","Iron Maiden","Dream Theater","Megadeth","AC/DC"]

from random import randint

print(metalList[randint(0,len(metalList)-1)])




# 10

numberList = [5,7,18,21,20,10,405,24]

a = [i % 2 == 0 for i in numberList]

print(a)












