



# OBJE ODAKLI PROGRAMLAMA

# OBJECT ORİENTED PROGRAMMING

    #ABSTRACTION , ENCAPSULATİON , INHERITANCE , POLYMORPHİSM



class Musician():

    def __init__(self,name):
        self.name = name
        print("Musician class")

    def test1(self):
        print("Test 1")

    def test2(self):
        print("Test 2")

deniz = Musician("Deniz")


class MusicianPlus(Musician):

    def __init__(self,name):
        Musician.__init__(self,name)
        print("Musician Plus")
    def test3(self):
        print("Test 3")



atlas = MusicianPlus("Atlas")
atlas.test3()
print(type(atlas))















