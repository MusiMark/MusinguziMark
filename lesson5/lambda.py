#Lab Activtiy 1
#Simple Lambda Activity

square = lambda x: x * x

print(square(3))

# Traditional FUnction
def add(a,b):
    return a+b
print(add(3,4))

#Lambda Equivalent
add_lamda = lambda a,b: a+b
print(add_lamda(3,4))

#Exercise 1
check_even = lambda x: x%2 == 0
print(check_even(2))

#Using filter
numbers = [1,2,3,24,5,6,7,8,9,10]

#filter even
list1 = list(filter(lambda x: x % 2 == 0, numbers))
print(list1)

#greater than
greater_than_20 = list(filter(lambda x: x > 20, numbers))
print(greater_than_20)

#Exec2 Using lambda using sorted
list2 = [ 'Cherry', 'Banana', 'Date', 'Apple', 'Mango', 'DragonFruit']

list2.sort(key = lambda x: len(x), reverse = True)
print(list2)

