

class Fruit():

    def __init__(self,name,calories):
        self.name = name
        self.calories = calories
    def info(self):
        print(f" a {self.name} has {self.calories} calories. ")

    def __str__(self):           # özel fonksiyon
        return f"{self.name}: {self.calories}"

    def __len__(self):
        return self.calories



myFruit = Fruit("banana",150)

print(myFruit.name)
print(myFruit.calories)

myFruit.info()

print(myFruit)

print(len(myFruit))




# başka metodlar


class Train():

    def __init__(self,name):
        self.name = name

    def __getitem__(self, item):
        if item == "a":
            return self.name
        else:
            return "Not Found"

myTrain = Train("myTrain")

print(myTrain["b"])

# internetten özel metdolara bakılabilir.


