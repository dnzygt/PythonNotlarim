


# OBJE ODAKLI PROGRAMLAMA

# OBJECT ORİENTED PROGRAMMING

    #ABSTRACTION , ENCAPSULATİON , INHERITANCE , POLYMORPHİSM


# polymorphism


class Banana():

    def __init__(self,name):
        self.name = name
    def info(self):
        return f"100 calories {self.name}"


class Apple():

    def __init__(self, name):
        self.name = name
    def info(self):
        return f"150 calories {self.name}"

banana = Banana("banana")
apple = Apple("apple")

# önce objeyi oluşturmak lazım yukardaki gibi

# f" ***  {}" format işlemidir

fruitList = [banana,apple]

for fruit in fruitList:
    print(fruit.info())























