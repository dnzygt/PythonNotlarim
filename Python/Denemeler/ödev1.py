#Problem 1

"""
kilo = float(input("Kilo:"))
boy = float(input("Boy:"))

BKİ = kilo/boy**2

print("Beden Kitle Endeksi:",BKİ)

if(BKİ < 18.5):
    print("Zayıf")
elif(18.5 <= BKİ < 25):
    print("Normal")
elif(25 <= BKİ < 30):
    print("Fazla Kilolu")
elif(30 <= BKİ):
    print("Obez")
"""

#Problem 2

"""
a = float(input("Sayı 1:"))
b = float(input("Sayı 2:"))
c = float(input("Sayı 3:"))

if(a>=b and a>=c):
    print(a)
elif(b>=a and b>=c):
    print(b)
elif(c>=a and c>=b):
    print(c)
"""

#Problem 3

"""
vize1 = float(input("Vize 1:"))
vize2 = float(input("Vize 2:"))
final = float(input("Final:"))

ortalama = (vize1*30/100)+(vize2*30/100)+(final*40/100)

print("Ortalama:",ortalama)

if(100 >= ortalama >= 90):
    print("Harf Notunuz: AA")
elif(90 > ortalama >= 85):
    print("Harf Notunuz: BA")
elif(85 > ortalama >= 80):
    print("Harf Notunuz: BB")
elif(80 > ortalama >= 75):
    print("Harf Notunuz: CB")
elif(75 > ortalama >= 70):
    print("Harf Notunuz: CC")
elif(70 > ortalama >= 65):
    print("Harf Notunuz: DC")
elif(65 > ortalama >= 60):
    print("Harf Notunuz: DD")
elif(60 > ortalama >= 55):
    print("Harf Notunuz: FD")
elif(55 > ortalama):
    print("Harf Notunuz: FF")
"""

#Problem 4

"""
şekil = input("Şekil Adı:")

if(şekil == "Dörtgen"):
    a = int(input("Kenar 1:"))
    b = int(input("Kenar 2:"))
    c = int(input("Kenar 3:"))
    d = int(input("Kenar 4:"))
    if(a==b and a==c and a==d):
        print("Kare")
    elif(a==c and b==d):
        print("Dikdörtgen")
    else:
        print("Sıradan Dörtgen")
elif(şekil == "Üçgen"):
    a = int(input("Kenar 1:"))
    b = int(input("Kenar 2:"))
    c = int(input("Kenar 3:"))
    if(a==b and a==c):
      print("Eşkenar Üçgen")
    elif((a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a)):
        print("İkizkenar Üçgen")
    else:
        print("Sıradan Üçgen")
"""
import time
i = 5

while (0 < i):
    print("Son {} saniye...".format(i))
    i -=1
    time.sleep(1)
print("YENİ YIL KUTLU OLSUN")