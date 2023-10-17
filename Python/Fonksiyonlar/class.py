




class Person():
    name = ""
    age = 0
    gender = ""
    job = ""



    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender


deniz = Person("Deniz",24,"Male")

print(deniz.age)
print(deniz.name)
print(deniz.gender)


print("""
********************************************
""")


class Dog():

    year = 7

    def __init__(self,age):
        self.age = age
        self.dogHumanAge = age * self.year
    def humanAge(self):
        return self.age * self.year

myDog = Dog(3)

print(myDog.humanAge())

print(myDog.dogHumanAge)


