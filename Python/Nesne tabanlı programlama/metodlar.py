


class Yazılımcı():

    def __init__(self,isim,soyisim,numara,maaş,diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maaş = maaş
        self.diller = diller

    def bilgilerigöster(self):
        print("""
        Yazılımcı objesinin özellikleri:
        
        İsim : {}
        Soyisim : {}
        Numara : {}
        Maaş : {}
        Diller : {}
        
        """.format(self.isim,self.soyisim,self.numara,self.maaş,self.diller))

    def zam_yap(self,zam_miktarı):
        print("Zam yapılıyor...")
        self.maaş += zam_miktarı
        print("Yeni maaş belirleniyor.\nYeni maaş:",self.maaş)
    def dil_ekle(self,yenidil):
        print("Dil ekleniyor...")
        self.diller.append(yenidil)
        print("Yeni dil başarıyla eklendi")




yazılımcı = Yazılımcı("Deniz","Yiğit",58,3000,"Türkçe,İngilizce")

print(yazılımcı.bilgilerigöster())

yazılımcı.zam_yap(2000)

















