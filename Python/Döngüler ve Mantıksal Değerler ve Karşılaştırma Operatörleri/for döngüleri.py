"""

For Döngüleri

For döngüleri, listelerin, demetlerin, stringlerin ve hatta sözlüklerin
üzerinde dolaşmamızı sağlayan döngü türüdür.

"""
"""""
liste = [1,2,3,4,5,6,7]

for i in liste:
    print(i)
"""
"""
toplam = 0
liste = [1,2,3,4,5,6,7]
for i in liste:
    toplam = toplam + i
    print("Toplam: {} , Eleman: {}".format(toplam,i))

   #CEVAP 
# Toplam: 1 , Eleman: 1
# Toplam: 3 , Eleman: 2
# Toplam: 6 , Eleman: 3
# Toplam: 10 , Eleman: 4
# Toplam: 15 , Eleman: 5
# Toplam: 21 , Eleman: 6
# Toplam: 28 , Eleman: 7
"""

"""
liste = [11,23,36,41,56,73,89]

for i in liste:
    if(i % 2 == 0):
        print(i)
"""

"""
a = "python"
for i in a:
    print(i)
"""

"""
liste = [(2,5),(6,4),(8,2)]

for (i,j) in liste:
    print("i: {},j: {}".format(i,j))  -BU DURUMDA İŞLEM YAPILABİLİR-
"""

"""
# KEYS VALUES İTEMS

sözlük = {'bir':1,'iki':2,'üç':3}

sözlük.keys()
#dict_keys(['bir', 'iki', 'üç'])

sözlük.values()
#dict_values([1, 2, 3])

sözlük.items()
#dict_items([('bir', 1), ('iki', 2), ('üç', 3)])
"""

"""
sözlük = {'gitmek':"bir yerden başka bir yere varmak",'atmak':"tutulan bir şeyi uzağa doğru fırlatmak"}

for (i,j) in sözlük.items():
    print("Kelime:",i ,"-","Anlamı:",j)

#CEVAP
# Kelime: gitmek - Anlamı: bir yerden başka bir yere varmak
# Kelime: atmak - Anlamı: tutulan bir şeyi uzağa doğru fırlatmak
"""

"""    DENEME

liste = list(range(11))
a = 1

for i in liste:
    print("i_{}:".format(a),i)
    a += 1
"""


# enumerate komutu
"""
myList = [10,20,30,40,50,60]

for i in enumerate(myList):
    print(i)
"""
#enumerate komutu değer ve değerlere ait indexleri yan yana
# (tuple) çıktı olarak verir

