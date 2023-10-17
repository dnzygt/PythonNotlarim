%%writefile myfile.txt
test1
test2
test3

# JUPYTER NOTEBOOK DA OLUŞTURULABİLİR.

# açıp okumak için

myFile = open("myfile.txt") #bu çalıştığında bir kere okuduk sayıldı.

myFile.read()   # kodunda bu text dosyasını okuyabiliyoruz

# ancak ikinci kere çalışltırıldığında text dosyamız sonda kalır.

myFile.seek(0)  # diyerek okuduğumuz metni sıfırlıyoruz.


# VEYA



with open("myfile.txt") as myFile:
    myContent = myFile.read()   # bu şekilde dosyamızı istediğimiz
                                # kadar açıp kapatabiliriz.


with open("myfile.txt",mode="w") as myNewFile: # w (write) yazmak için
    myNewFile.write("test4")

with open("myfile.txt",mode="w") as myNewFile: # r (read) okumak için
    myNewFile.write("test4")

# ancak bu komutlar dosyayı değiştirebilir

# dosyamızın bozulmaması ve değiştirilmemesi için append komutu kullanalım


with open("myfile.txt",mode="a") as myNewFile2:
    myNewFile.write("test4")





