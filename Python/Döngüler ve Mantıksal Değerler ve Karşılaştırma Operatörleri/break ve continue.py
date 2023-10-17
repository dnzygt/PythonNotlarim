# BREAK VE CONTİNUE



# Break : Döngü herhangi bir yerde break ifadesi ile karşılaştığı zaman durur.
# Break ifadesi sadece içinde bulunduğu döngüyü sonlandırır.

#örnek ile inceleyelim.
"""
i = 0

while (i < 10):
    print("i:",i)
    i += 1
"""
#şimdi break ifadesinin kullanalım.
"""
i = 0

while (i < 10):
    if(i == 7): #komutu ile i=7 için durma emrini verdik.
        break
    print("i:",i)
    i += 1
"""
"""
liste = [1,2,3,4,5]

for i in liste:
    if(i==4):
        break
    print("i:",i)
    i += 1
"""
"""
while True:
    isim = input("İsminizi Girin(Çıkmak için q'ya basın):")
    if(isim == "q"):
        print("Programdan Çıkılıyor...")
        break
    print("İsminiz:",isim)
"""



# CONTİNUE ifadesini inceleyelim

#break ifadesine göre daha az kullanılır.
#döngü herhangi bi yerde geri kalan hiçbir işlemi yapmıyor ve başa dönüyor.
"""
i = 0

while (i<10):

    if(i == 2):
        continue      İFADEMİZ SONSUZ DÖNGÜYE GİRER.

    print(i)
    i += 1
"""
"""
i = 0

while (i<10):

    if(i == 2):
        i += 1   #arttırma işlemi uygularız.
        continue

    print(i)         arttırma işlemi ile i=2 için atlamış olduk.
    i += 1
"""

#continue çok tercih edilmez.



# PASS

"""

PASS BİTMEMİŞ KODLARI GEÇMEK İÇİN YAZILIR 
BİR NEVİ HATA  ALMAMAK İÇİN

"""








