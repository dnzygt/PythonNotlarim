print("""

Faktöriyel Bulma Programı

çıkmak için q'ya basın
""")

while True:
    sayı = input("Bir sayı giriniz:")

    if(sayı == "q"):
        print("Çıkış Yapılıyor...")
        break

    else:
        sayı = int(sayı)

        faktöriyel = 1

        for i in range(1,sayı+1):
            faktöriyel *= i
        print("faktöriyel",faktöriyel)
