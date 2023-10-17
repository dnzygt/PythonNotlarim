"""İF ELİF ELSE"""


"""

yaş = int(input("Yaşınızı Giriniz:"))

if(0 < yaş < 18):
    print("Mekana Giremezsiniz!")
elif(yaş >= 18):
    print("Mekana Hoşgeldiniz!")
else:
    print("Hatalı Giriş!")

"""


# else yazmak zorunlu değil, elif komutu ile de bitebilir.

vize = float(input("Notunuzu Giriniz:"))
final = float(input("Notunuzu Giriniz:"))

ortalama = (vize*40/100)+(final*60/100)
G = "Sınava girmedi!"
print(ortalama)

if(100 >= ortalama > 90):
    print("Harf Notunuz : AA")
elif(90 >= ortalama > 85):
    print("Harf Notunuz : BA")
elif(85 >= ortalama > 80):
    print("Harf Notunuz : BB")
elif(80 >= ortalama > 75):
    print("Harf Notunuz : BC")
elif(75 >= ortalama > 70):
    print("Harf Notunuz : CC")
elif(70 >= ortalama > 65):
    print("Harf Notunuz : DC")
elif(65 >= ortalama > 50):
    print("Harf Notunuz : DD")
elif(50 >= ortalama > 0):
    print("Harf Notunuz : FF")



# DENEME

print("Oyunumuza Hoşgeldiniz")

a = "Yeni Oyun"
b = "Kayıt Yükle"
c = "Ayarlar"
d = "Çıkış"




seçenek = input("Ne yapmak istiyorsunuz? :")

if(seçenek == "a"):
    print("Yeni Oyun Başlatılıyor...")
elif(seçenek == "b"):
    print("Kayıt Dosyaları Açılıyor...")
    a = "kayıt 1"
    b = "kayıt 2"
    c = "kayıt 3"
    seçenek1 = input("Hangi kaydı yüklemek istiyorsunuz? :")
    if(seçenek1 == "a"):
        print("Kayıt 1 Yükleniyor...")
    elif(seçenek1 == "b"):
        print("Kayıt 2 Yükleniyor...")
    elif(seçenek1 == "c"):
        print("Kayıt 3 Yükleniyor...")
    else:
        print("Kayıt Bulunamadı.")
elif(seçenek == "c"):
    print("Ayarlara giriliyor...")
elif(seçenek == "d"):
    print("Çıkış Yapılıyor...")