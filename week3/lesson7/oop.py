class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def __init__(self,breed,age):
        self.breed = breed
        self.age = age

    def sound(self):
        super().sound()
        print("Dog Sound")

    def details(self):
        print(f"Breed:{self.breed} Age:{self.age}")



if __name__=="__main__":
    dog1 = Dog("Spike",3)

    dog1.details()
    dog1.sound()

