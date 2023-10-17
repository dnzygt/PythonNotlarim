print("""******************

Hesap Makinesi Programı

İşlemler;

1.Toplama +

2.Çıkarma -

3.Çarpma *

4.Bölme /

******************""")


a= int(input("Birinci Sayıyı Giriniz:"))
işlem = input("İşlemi Giriniz:")
b= int(input("İkinci Sayıyı Giriniz:"))

if(işlem == "+"):
    print("{} {} {} = {}".format(a,işlem,b,a+b))
elif(işlem == "-"):
    print("{} {} {} = {}".format(a,işlem,b,a-b))
elif(işlem == "*"):
    print("{} {} {} = {}".format(a,işlem,b,a*b))
elif(işlem == "/"):
    print("{} {} {} = {}".format(a,işlem,b,a/b))
else:
    print("Geçersiz İşlem!")