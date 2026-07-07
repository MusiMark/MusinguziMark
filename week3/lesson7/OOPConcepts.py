# Lab Activity 1
class Student():
    def __init__(self,age,name,student_number):
        self.age = age
        self.name = name
        self.student_number = student_number


student = Student(26,"Mark","240007000")

print(student.student_number)

#Access Modifiers

#Example
# There are only 3; -Public -Private -Protected

class Employee:
    def __init__(self):
        self.name = "John"
        self.__salary = 6000000

    def salary(self):
        return self.__salary

emp = Employee()
print(emp.name,emp.salary())

#Exercise
class Car:
    def __init__(self,brand,model,price):
        self.brand = brand
        self._model = model
        self.__price = price


    def getPrice(self):
        return self.__price

car1 = Car("Mercedes","GL-2",12000000)
print(car1.brand)
print(car1._model)
print(car1.getPrice())

