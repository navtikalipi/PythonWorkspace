from abc import ABC, abstractmethod

class Electronics(ABC):
    @abstractmethod
    def playvideo(self):
        pass

class Laptop(Electronics):
    def playvideo(self):
        print("Press play button from keyboard")

class Mobile(Electronics):
    def playvideo(self):
        print("Press play button from keyboard")

laptop=Laptop()
laptop.playvideo()

mobile=Mobile()
mobile.playvideo()