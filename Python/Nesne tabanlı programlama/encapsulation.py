


# OBJE ODAKLI PROGRAMLAMA

# OBJECT ORİENTED PROGRAMMING

    #ABSTRACTION , ENCAPSULATİON , INHERITANCE , POLYMORPHİSM




# encapsulation (hapsetmek demek) (çok önemliymiş)


class Phone():

    def __init__(self,name,price):
        self.name = name
        self.price = price

    def info(self):
        print(f"{self.name} price is {self.price} dollar.")


iphone = Phone("İphone 14",1000)

iphone.info()

"""
iphone.price = 400

iphone.info()   # şeklinde değiştirilebilir
"""

# bu fiyatın değiştirilmesini istemiyorsak


class Phone1():

    def __init__(self,name,price):
        self.name = name
        self.__price = price    # price yanına __ yazarak kitleriz

    def info(self):
        print(f"{self.name} price is {self.__price} dollar.")


iphone1 = Phone1("İphone 15",1200)

iphone1.__price = 900

iphone1.info()


# eğer değiştirilmesi isteniyorsa başka bir metod koyabiliriz


class Phone2():

    def __init__(self,name,price):
        self.name = name
        self.__price = price

    def info(self):
        print(f"{self.name} price is {self.__price} dollar.")

    def changePrice(self,price):
        self.__price = price


iphone2 = Phone2("Samsung A74",600)

iphone2.info()

iphone2.changePrice(500)

iphone2.info()



