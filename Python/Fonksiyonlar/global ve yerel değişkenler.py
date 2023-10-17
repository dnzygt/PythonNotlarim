



"""
def fonksiyon():
    a = 10
    print(a)

fonksiyon()
print(a)

             #yerel değişken yok olduğu için hata veriyor.
"""

"""
b = 5         #global değişken olduğundan hatasız çalıştı

def fonksiyon():
    print(b)

fonksiyon()

         #verilen değer fonksiyon() ifadesinden önce olmalı
"""

"""
def fonksiyon():
    print(s)
fonksiyon()
s = "Python"    # değişken fonksiyon() ifadesinden sonra olduğundan
                # fonksitonumuz s değişkenini göremez ve hata verir.
"""

"""
c = 10

def fonksiyon():
    c = 2
    print(c)
fonksiyon()
print(c)
              # globaldeki c değeri görülür fakat öncelik fonksiyonun içindeki
              # local değerdir. bu ifade de önce local değer yazılır sonra
              # global değer yazılır.
"""


# GLOBAL İFADESİNİ KULLANALIM

"""

d = 5             # d = 5 değerini verdik.
                  
def fonksiyon():  
    global d
    d = 3                 # foksiyon içerisinde d ifademizi global hale getirdik
    print(d)              

fonksiyon()             # fonksiyonu çalıştırdığımız zaman d ifademizfonksiyonun
print(d)                # içerisindeki d ifadesine evrildi
                        # yeni d ifademiz hen localde hem globalde 3 olarak değişti.
                        
"""
# fakat çok kullanışlı değil genellikle local kullanılır.



# İF WHİLE DÖNGÜSÜ İÇİNDE LOCAL VE GLOBAL İNCELEYELİM

                      # local değişkenler fonksiyonların içinde bulunur.

if True:
    e = 4
    print(e)
print(e)


