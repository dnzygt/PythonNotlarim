

# PYTHONDA HER BİR DOSYA BİR MODÜL OLARAK KABUL EDİLİR.


# modül kullanımı örnek math modülü



import math

dir(math)


"""sayı = int(input("Sayı:"))

math.factorial(sayı)

print(math.factorial(sayı))"""


"""math.floor(5.6)       # kendisinden önceki en büyük tam sayı
print(math.floor(5.6))"""

"""math.ceil(5.6)           # kendisinden sonraki en küçük tam sayı
print(math.ceil(5.6))"""

# help(math) ile kullanılabilen modülleri görebiliriz.

"""import math as matematik   # math ifadesini matematik olarak değiştirdik

matematik.factorial(5)
print(matematik.factorial(5))"""


# YÖNTEM 2

"""from math import *  # bütün math işlemerlini içeri alır

factorial(5)
print(factorial(5))

print(floor(5.43))"""

"""
from math import floor,ceil

# yazarak sadece iki fonksiyon dahil ediyoruz.

"""


def faktorial(sayı):
    print("Benim fonksiyonum")

    faktoriyel = 1
    if(sayı == 0 or sayı == 1):
        faktoriyel *= sayı
        sayı -= 1
    return faktoriyel

from math import *

print(factorial(5))     # bu durumda python son gördüğü fonksiyonu alıyor.
                        # el ile yazdığımız faktöriyeli alsaydı benim
                        # fonksiyon yazardı. bilgi olsun






