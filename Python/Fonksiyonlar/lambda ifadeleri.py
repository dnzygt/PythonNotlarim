


"""

LİST COMPREHENSİON İFADELERİ HATIRLAYALIM

"""

"""
liste1 = [1,2,3,4,5]

liste2 = [ i * 2 for i in liste1]

print(liste2)

"""

# LAMBDA İFADELERİNİN MANTIĞI LİST COMPREHENSİONLARA BENZİYOR

"""
# LAMDA İFADELERİNİN YAPISI

etiket = lambda parametre1, parametre2, parametre3, ...
"""

"""
def ikiyleçarp(x):
    return x * 2
print(ikiyleçarp(3))


ikiyleçarp = lambda x : x * 2
print(ikiyleçarp(4))
"""


"""
def toplama(x,y,z):
    return x+y+z
print(toplama(10,11,12))


toplama = lambda x,y,z : x + y + z
print(toplama(2,3,4))

"""

# STRİNGLER İÇİNDE GEÇERLİ
"""
def tersçevir(s):
    return s[::-1]

print(tersçevir("Python Programlama"))



tersçevir = lambda s : s[::-1]
print(tersçevir("Programlama Python"))
"""


def çifttek(sayı):
    return sayı % 2 == 0
print(çifttek(4))
print(çifttek(5))


çifttek = lambda sayı : sayı % 2 == 0
print(çifttek(4))
print(çifttek(5))









