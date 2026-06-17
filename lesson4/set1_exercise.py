#Exercise 1
print("Exercise 1".center(50,"*"))

#No. 1
names = ["Mark","John","Mary","Henry","Alice"]
print(names[1])

#No. 2
names[0] = "Salah"
print(names)

#No. 3
names.append("Charlotte")
print(names)

#No. 4
names.insert(2,"Bathel")
print(names)

#No. 5
names.pop(3)
print(names)

#No. 6
print(names[-1])

#No. 7
food = ["Chicken","Fries","Beef","Pork","Juice"]
print(food[2:])

#No. 8
country_list = ["Mexico","USA","Canada"]
new_list = country_list.copy()
print(new_list)

#No. 9
for country in country_list:
    print(f"World Cup is in {country}")

#No. 10
animals = ["Dog","Cat","Sheep","Lion","Tiger","Mouse","Zebra"]
print(f"Original list: {animals}")
animals.sort()
print(f"Ascending Order: {animals}")
animals.sort(reverse=True)
print(f"Descending Order: {animals}")

#No. 11
for animal in animals:
    if "a" in animal:
        print(animal)

#No. 12
first = ["Mike"]
second = ["Michael", "David"]

joined = first + second
print(joined)

print()
print("Exercise 2".center(50,"*"))
#No. 1
x = ("samsung", "iphone", "tecno", "redmi")
print(x)

#No. 2
print(x[-2])

#No. 3
list1 = list(x)
list1[1] = "itel"
x = tuple(list1)
print(x)

#No. 4
list1 = list(x)
list1.append("Huawei")
x = tuple(list1)
print(x)

#No. 5
for y in x:
    print(y)

#No. 6
list1 = list(x)
list1.pop(0)
x = tuple(list1)
print(x)

#No. 7
city = tuple(("Kampala","Gulu","Mbarara","Jinja"))
print(city)

#No. 8
(city1, city2, city3, city4) = city
print(city1)
print(city4)

#No. 9
print(city[1:4])

#No. 10
first_tuple = tuple("Mike")
second_tuple = ("Michael", "David")

joined_tuple = first_tuple + second_tuple
print(joined_tuple)

#No. 11
color = ("Blue","Red","Green","Yellow","Brown")*3
print(color)

#No. 12
this_tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
answer = this_tuple.count(8)
print(f"The number 8 appears: {answer}")

print()
#Exercise 3
print("Exercise 3".center(50,"*"))

#No. 1
beverages = {"Fanta","Pepsi","Cocacola","Mirinda"}

#No. 2
beverages.update(("Juice","Water"))
print(beverages)

#No. 3
mySet = {"oven", "kettle", "microwave", "refrigerator"}

print("Is microwave in mySet: ", "microwave" in mySet)

#No. 4
mySet.remove("kettle")
print(mySet)

#No. 5
for x in mySet:
    print(x)

#No. 6
my_set = {"Man U","Man City","Liverpool","Arsenal"}
my_list = ["Chelsea","Spurs"]

my_set.update(my_list)
print(my_set)

#No. 7
first_names = {"Yamal","Ronaldo","Messi","Salah"}
ages = {18,41,38,34}

new = first_names.union(ages)
print(new)
print()

#Exercise 4
print("Exercise 4".center(50,"*"))

#No. 1
string = "World Cup "
year = 26
print(string+str(year))

#No. 2
txt = "    Hello,       Uganda!       "
txt = txt.replace(" ","")
print(txt)

#No. 3
print(txt.upper())

#No. 4
print(txt.replace("U","V"))

#No. 5
y = "I am proudly Ugandan"
print(y[1:5])

#No. 6
x = "All \"Data Scientists\" are cool!"
print(x)


print()
#Exercise 5
print("Exercise 5".center(50,"*"))

Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

#No. 1
print("The shoe size is ",Shoes["size"])

#No. 2
Shoes["brand"] = "Addias"
print(Shoes)

#No. 3
Shoes.update({"type":"sneakers"})
print(Shoes)

#No. 4
keys = Shoes.keys()
print(keys)

#No. 5
values = Shoes.values()
print(values)

#No. 6
print("Does key 'size' exist: ", "size" in Shoes)

#No. 7
for key, values in Shoes.items():
    print(f"Key:{key}, Values: {values}")

#No. 8
Shoes.pop("color")
print(Shoes)

#No. 9
Shoes.clear()
print(Shoes)

#No. 10
liverpool_fc = {
    "name": "Liverpool Football Club",
    "nickname": "The Reds",
    "founded": 1892,
    "stadium": "Anfield",
    "city": "Liverpool",
    "color": "Red"
}

new_copy = liverpool_fc.copy()
print(new_copy)

#No. 11

person = {
    "profile": {
        "first_name": "John",
        "last_name": "Mike",
        "age": 24
    },
    "contact": {
        "email": "john@email.com",
        "phone": "123456789"
    },
    "interests": ["coding", "football"]
}

print(person)