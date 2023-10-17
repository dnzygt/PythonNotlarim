
print("""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

Hesap makinesi

1.toplama
2.çıkarma
3.çarpma
4.bölme

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
""")




def çıkarma(*a):

    toplam = a[2]

    for i in a:
        toplam -= i
    print(toplam)

çıkarma(13,1)  # BİTMEDİ








