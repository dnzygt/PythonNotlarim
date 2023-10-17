


# 1

my_string = "Python Öğreniyorum" # 5. harfi değişkene ata.

bes = my_string[4]

print(bes)


# 2

my_new_string = "ProgramlamayaMerhabaDedik"

# 5.ve 8. kkarakterler dahil yazır.

my_new_string[4:8]
print(my_new_string[4:8])


# 3

my_last_string = "Afyonkarahisarlılaştıramadıklarımızdanmısınız"

my_last_string[::-1]
print(my_last_string[::-1])


# 4

type(4+12.2+48)
print(type(4+12.2+48))


# 5

toplam = 5+7*12

print(toplam)


# 6

# bu listeyi iki farklı yoldan oluşturun [1,3,"a"]

liste = [1,3,"a"]
print(liste)
print(type(liste))

liste1 = (1,3,"a")
print(liste1)
print(type(liste1))


# 7

my_list = [3.14,4,[2,3,"b"],True] # b'yi tek satıra al

my_list[2][2]
print(my_list[2][2])



# 8

my_dictionary = {"key1":20.25, "kk2":[40,{"k21":"a"}]}
# a'yı tek satıra alın.

print(my_dictionary["kk2"][1]["k21"])


# 9

# Asagidaki liste set'e cevirilince hangi degerler icinde kalacaktir?
my_list_to_be_set = [3,4,9,3,21,22,4,3,9,10,21,22]

set(my_list_to_be_set)
print(set(my_list_to_be_set))


# 10

# Asagidaki ifadenin sonucu ne olacaktir?
x = 30 * 5 + 3
y = 108 - 2 * 4
x > y

print(x>y)