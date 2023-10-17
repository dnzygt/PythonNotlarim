"""
sayı = int(input("Sayı:"))

i = 1
toplam = 0

while (i<sayı):
    if(sayı % i == 0):
        toplam += i
    i += 1
if(toplam == sayı):
    print("Mükemmel bir sayıdır.")
else:
    print("Mükemmel bir sayı değildir.")
"""
"""
sayı = input("Sayı:")
basamak_sayisi = len(sayı)
sayı = int(sayı)
basamak = 0
toplam = 0

gecici_sayı = sayı

while (gecici_sayı > 0):
    basamak = gecici_sayı % 10

    toplam += basamak ** basamak_sayisi

    gecici_sayı //= 10

if (toplam == sayı):
    print(sayı, "bir armstrong sayısıdır.")
else:
    print(sayı, "bir armstrong sayısı değildir.")
    
"""
"""
sayı = int(input("Sayı:"))
basamak = str(sayı)
toplam = 0
basamak1 = len(basamak)

for x in basamak:
    sayı1 = x ** basamak1

    toplam += sayı1
if(sayı == toplam):
    print("armstrong")
else:
    print("armstrong değil")
    
"""

for i in range(1,11):
    print("*****************")
    for j in range(1,11):
        print("{} x {} = {}".format(i,j,i*j))

