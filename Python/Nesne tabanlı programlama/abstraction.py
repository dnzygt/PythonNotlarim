


# OBJE ODAKLI PROGRAMLAMA

# OBJECT ORİENTED PROGRAMMING

    #ABSTRACTION , ENCAPSULATİON , INHERITANCE , POLYMORPHİSM




# abstraction ( soyutlama )



from abc import ABC, abstractmethod

class Car(ABC):

    @abstractmethod
    def maxSpeed(self):
        pass


class Tesla(Car):

    def maxSpeed(self):
        print("200 km")

tesla = Tesla()

tesla.maxSpeed()






















