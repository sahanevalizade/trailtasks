class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print(f"{self.name} ses cixarir.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} hurur.")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} miyavlayir.")

it = Dog("kopek")
pisik = Cat("pisik")

it.speak()    # Kopek hurur.
pisik.speak()  # Pisik miyavlayir.   