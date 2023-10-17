print("""
****************************
Kullanıcı Girişi
****************************
""")

sys_kullanıcı_adı = "Deniz"
sys_parola = "5858"

kullanıcıAdı = input("Kullanıcı Adı:")
şifre = input("Şifre:")

if(kullanıcıAdı == sys_kullanıcı_adı and şifre == sys_parola):
    print("Giriş Başarılı")
elif(kullanıcıAdı != sys_kullanıcı_adı or şifre != sys_parola):
    print("Kullanıcı Adı veya Şifre Yanlış!")