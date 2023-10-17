# Metod nedir?
"""

şimdiye kadar pythonda kullanabildiğimiz bir çok veritipi gördük ve bazı veritiplerinin
metodlarını kullandık. Aslında bu veritiplerini oluşturan her bir değişken Pythonda obje(object)
olarak düşünülür ve Python geliştiricileri bu objelere birçok method tanımlamıştır.

Metodlar obje üzerinde belli işlemler gerçekleştiren objelere özgü fonsiyonlardır.
şu şekilde kullanılır.

obje.herehangi_bir_metod(değerler(opsiyonel))

"""




a = [1,2,3,4,5]   # a listesini belirledik.

a.insert(1,"Murat")  # insert komutu ile 1'in sonrasıda gelen değişkeni murat ile değiştirdik.
print(a)
[1, 'Murat', 2, 3, 4, 5]  #çıktısı elde edilir.

a.append("Python")   # append komutu ile listenin sonuna python eklemesi yaptık.
print(a)
[1, 'Murat', 2, 3, 4, 5, 'Python']  #çıktısı elde edilir.

a.pop()   # pop komutu ile liste sonuna eklenen elemanı çıkardık.
print(a)
[1, 'Murat', 2, 3, 4, 5]   #çıktısı elde edilir.



help(a.append)




