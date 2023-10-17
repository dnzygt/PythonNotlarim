

"""
a = "TahanınGöbeği"
type(a)
print(type(a))

for i in a:
    print(i*5)
"""


"""
liste = [13,25,36,84,599]

index = 0

for i in liste:
    print("{}. index elemanı: {}".format(index,i))
    index += 1
"""
"""
toplam = 0
liste = [1,2,3,4]

for i in liste:
    toplam = toplam + i
    print("{} eleman toplamı: {}".format(i,toplam))
print("Toplam:",toplam)
"""

"""
liste = [21,3,34,5,65,76,87,98,9,79,56,4,7,618,763,68]


deger = input("İstenilen değerler için seçim yapınız:")

for i in liste:
    if(deger == "çift"):
        if(i % 2 == 0):
            print(i)
    elif (deger == "tek"):
        if (i % 2 == 1):
            print(i)
"""


"""
sözlük = {'bir':1,'iki':2,'üç':3,'dört':4}
print(type(sözlük))

print(sözlük.values())
print(sözlük.keys())
print(sözlük.items())

for i in sözlük:
    print(i)

for i in sözlük.keys():
    print(i)

for i in sözlük.values():
    print(i)

for i in sözlük.items():
    print(i)
"""





sys_şifre = "5858"
giriş_hakkı = 3

while True:


    şifre = input("Şifre:")

    if(şifre != sys_şifre):
        giriş_hakkı -= 1
        print("Hatalı Şifre...")
        if (giriş_hakkı == 0):
            print("Giriş Hakkınız Kalmadı!!")
            break
        continue




    else:
        print("Hoşgeldiniz")

        print("""
                    ****************************
                    ---------A Bankası----------

                    1. Bakiye Sorgulama
                    2. Para Yatırma
                    3. Para Çekme
                    4. Çıkış
                    ****************************

                    """)
        bakiye = 1000
        while True:


            işlem = input("Yapmak istediğiniz işlemi giriniz:")

            if(işlem == "4"):
                print("Hoşçakalın İyi Günler...")
                break
            elif(işlem == "1"):
                print("Bakiyeniz:",bakiye)
                continue
            elif(işlem == "2"):
                miktar = int(input("Miktarı giriniz:"))
                bakiye += miktar
                print("Yeni Bakiye:",bakiye)
                continue
            elif(işlem == "3"):
                miktar = int(input("Miktarı giriniz:"))
                bakiye -= miktar
                print("Yeni Bakiye:",bakiye)
                continue
























