# LİSTELERİ ÜRETMEK VE OLUŞTURMAK

"""
liste1 = [1,2,3,4,5]

liste2 = []

for i in liste1:
    liste2.append(i)
print(liste2)
"""
"""
liste1 = [1,2,3,4,5]

liste2 = [i for i in liste1]   #LİST COMPREHENSİON ÖRNEĞİ
print(liste2)
"""
"""
liste = [2,3,4]

liste1 = [i * 2 for i in liste]
print(liste1)
"""
"""
liste = [(1,2),(2,3),(4,5)]

liste1 = [i*j for i,j in liste]
print(liste1)
"""

"""

liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste1 = []
for i in liste:
    for x in i:
        liste1.append(x)
print(liste1)


liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste1 = [x for i in liste for x in i]
print(liste1)

"""