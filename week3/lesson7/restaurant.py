class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name:{self.restaurant_name} \nCuisine Type:{self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} Restaurant is open !!!")


restaurant = Restaurant("Cafe Javas","Chicken")
restaurant2 = Restaurant("KFC","Chicken")
restaurant3 = Restaurant("Food Hub","Chicken")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

restaurant.open_restaurant()

print("\n\n===User Class====")
class User:
    def __init__(self,firstname,lastname,age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def describe_user(self):
        print(f"Firstname:{self.firstname} Lastname:{self.lastname} Age:{self.age}")

    def greet_user(self):
        print(f"Hello {self.firstname} {self.lastname}!")


user1 = User("James","Bob",25)
user1.describe_user()
user1.greet_user()