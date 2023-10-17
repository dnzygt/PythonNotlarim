print("""
************
ATM MAKİNESİ
************



1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme
4. Çıkış

""")

bakiye = 1000

while True:
    işlem = input("İşlemi seçiniz:")

    if(işlem == "4"):
        print("İyi günler yine bakleriz...")
        continue
    elif(işlem == "1"):
        print("Bakiyeniz: {}".format(bakiye))
    elif(işlem == "2"):
        miktar = int(input("Miktarı giriniz:"))
        bakiye += miktar
        print("Yeni bakiye:",bakiye)
        continue
    elif(işlem == "3"):
        miktar = int(input("Miktarı giriniz:"))
        if(miktar > bakiye):
            print("Yetersiz bakiye...")
            continue
        bakiye -= miktar
        print("Yeni bakiye:",bakiye)
        continue
    else:
        print("Geçersiz işlem...")



