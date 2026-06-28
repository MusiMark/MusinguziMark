#Question 1
print("====Question 1====")

class Person:
    def __init__(self,name,id_number):
        self.name = name
        self.id_number = id_number

    def display_info(self):
        print(f"Name: {self.name}\nId Number: {self.id_number}")


class Student(Person):
    def __init__(self,name,id_number,major):
        super().__init__(name,id_number)
        self.major = major

    def display_info(self):
        print("~~~~Student~~~~")
        super().display_info()
        print(f"Major: {self.major}")

class Lecturer(Person):
    def __init__(self,name,id_number,department):
        super().__init__(name,id_number)
        self.department = department

    def display_info(self):
        print("~~~~Lecturer~~~~")
        super().display_info()
        print(f"Department: {self.department}")


student = Student("Fill Max",2400422334,"Civil Engineering")
lecturer = Lecturer("Tom Rick", 213324535, "Software")

student.display_info()
lecturer.display_info()



#Question 2
print("\n====Question 2====")
class Vehicle:
    def __init__(self,reg_number,rental_price):
        self.reg_number = reg_number
        self.rental_price = rental_price

    def display_info(self):
        print(f"Reg Number: {self.reg_number}\nRental Price: {self.rental_price}")

    def calc_rental_cost(self,no_of_days):
        cost = self.rental_price * no_of_days
        print(f"The rental cost: {cost}")

class Car(Vehicle):
    def __init__(self,reg_number,rental_price,seating_capacity):
        super().__init__(reg_number,rental_price)
        self.seating_capacity = seating_capacity

    def display_info(self):
        print("~~~Car~~~")
        super().display_info()
        print(f"Seating Capacity: {self.seating_capacity}")

class Motorcycle(Vehicle):
    def __init__(self,reg_number,rental_price,engine_capacity):
        super().__init__(reg_number,rental_price)
        self.engine_capacity = engine_capacity

    def display_info(self):
        print("~~~Motorcycle~~~")
        super().display_info()
        print(f"Engine Capacity: {self.engine_capacity}")

car1 = Car("UA 123A", 200000, 5)
bike1 = Motorcycle("KMC 789B", 30000, 250)

car1.display_info()
car1.calc_rental_cost(5)

bike1.display_info()
bike1.calc_rental_cost(5)

#Question 3
print("\n====Question 3====")
class BankAccount:
    def __init__(self,acc_number,balance:float = 0.0):
        self.acc_number = acc_number
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"Deposit [UGX {amount}] Successful")

    def withdraw(self,amount):
        if amount > 0:
            print("Amount must be greater than 0")
        else:
            self.balance -= amount
            print(f"Withdraw Successful")

    def get_balance(self):
        print(f"Balance: {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self,acc_number,balance,interest):
        super().__init__(acc_number,balance)
        self.interest = interest
        print(f"Savings Account({acc_number}) created  Initial balance: {self.balance}")

    def withdraw(self,amount):
        if amount < 0:
            print("Amount cannot be negative")
        elif amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print(f"Withdraw [UGX {amount}] Successful")

class CurrentAccount(BankAccount):
    def __init__(self,acc_number,balance,overdraft):
        super().__init__(acc_number,balance)
        self.overdraft = overdraft
        print(f"Current Account({acc_number}) created  Initial balance: {self.balance}")

    def withdraw(self,amount):
        if amount < 0:
            print("Amount cannot be negative")
        elif amount > (self.overdraft + self.balance):
            print("Transaction Failed: Exceeded the overdraft limit")
        else:
            self.overdraft -= amount
            print(f"Withdraw [UGX {amount}] Successful")

sav = SavingsAccount("SAV-1001", 1000000.0, 0.15)
sav.deposit(500000)
sav.withdraw(200000)
sav.get_balance()
sav.withdraw(2000000000)

cur = CurrentAccount("CUR-2002", 2000000.0, 500000.0)
cur.deposit(2000000)
cur.withdraw(600000)
cur.get_balance()
cur.withdraw(2000000000)

#Question 4
print("\n====Question 4====")
class Learner:
    def __init__(self,name,reg_number):
        self.name = name
        self.reg_number = reg_number

    def calculate_final_grade(self):
        pass

class Undergraduate(Learner):
    def __init__(self,name,reg_number,grade_list):
        super().__init__(name,reg_number)
        self.grade_list = grade_list

    def calculate_final_grade(self):
        total = sum(self.grade_list)
        average = total / len(self.grade_list)

        if average >= 80:
            print(f"Grade A ({average})")
        elif average >= 70:
            print(f"Grade B ({average})")
        elif average >= 60:
            print(f"Grade C ({average})")
        elif average >= 50:
            print(f"Grade D ({average})")
        else:
            print(f"Grade E ({average})")


class Postgraduate(Learner):
    def __init__(self,name,reg_number,grade_list):
        super().__init__(name,reg_number)
        self.grade_list = grade_list

    def calculate_final_grade(self):
        total_marks = 0
        for grade in self.grade_list:
            mark = (grade[0]*0.6) + (grade[1]*0.4)
            total_marks += mark

        average = total_marks / len(self.grade_list)

        if average >= 80:
            print(f"Grade A ({average})")
        elif average >= 70:
            print(f"Grade B ({average})")
        elif average >= 60:
            print(f"Grade C ({average})")
        elif average >= 50:
            print(f"Grade D ({average})")
        else:
            print(f"Grade E ({average})")

ug_student = Undergraduate("Alice Nsubuga", "UG/2026/001", [90,73,78,81,77])
pg_student = Postgraduate("Dr. Bob Okello", "PG/2026/889", [(90,80),(70,52),(60,75),(67,79),(56,70)])

ug_student.calculate_final_grade()
pg_student.calculate_final_grade()

#Question 5
print("\n====Question 5====")
class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def get_total_cost(self):
        return self.price

    def product_info(self):
        print(f"{self.name} --> {self.price}")

class PhysicalProduct(Product):
    def __init__(self,name,price,shipping_cost):
        super().__init__(name,price)
        self.shipping_cost = shipping_cost

    def get_total_cost(self):
        return self.price + self.shipping_cost

    def product_info(self):
        print(f"{self.name} --> {self.price} + {self.shipping_cost}")

class DigitalProduct(Product):
    def __init__(self,name,price,download_link):
        super().__init__(name,price)
        self.download_link = download_link

food = PhysicalProduct("Vanilla Cake",100000,1500)
book = PhysicalProduct("Hardcover Textbook", 45000.00, 4000)
software = DigitalProduct("Photo Editing Suite", 250000.00, "https://store.com")

cart = [food,book,software]
total_bill = 0
for product in cart:
    product.product_info()
    total_bill += product.get_total_cost()
print(f"Total Cart Bill: {total_bill}")

#Question 6
print("\n====Question 6====")
class Employee:
    def __init__(self,name,emp_number):
        self.name = name
        self.emp_number = emp_number

    def calculate_pay(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self,name,emp_number,salary):
        super().__init__(name,emp_number)
        self.salary = salary

    def calculate_pay(self):
        print(f"Salary({self.name}) --> {self.salary}")

class PartTimeEmployee(Employee):
    def __init__(self,name,emp_number,hourly_wage,no_of_hours):
        super().__init__(name,emp_number)
        self.hourly_wage = hourly_wage
        self.no_of_hours = no_of_hours

    def calculate_pay(self):
        pay = self.no_of_hours * self.hourly_wage
        print(f"Wage({self.name}) --> {pay}")

emp1 = FullTimeEmployee("Joan Kakwenzire", "FT-101", 1500000)
emp2 = PartTimeEmployee("David Ochieng", "PT-502", 20000.00,55)

emp1.calculate_pay()
emp2.calculate_pay()

#Question 7
print("\n====Question 7====")
class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email

    def login(self):
        print(f"{self.name} has logged in")


class Student(User):
    def __init__(self,name,email,reg_number):
        super().__init__(name,email)
        self.reg_number = reg_number
        self.enrolled_courses = []

    def enroll_in_course(self, course_name):
        self.enrolled_courses.append(course_name)
        print(f"{self.name} enrolled in course: {course_name}")

class TeachingAssistant(Student):
    def __init__(self,name,email,reg_number,assigned_course):
        super().__init__(name,email,reg_number)
        self.assigned_course = assigned_course

    def enroll_students(self):
        print(f"{self.name} has enrolled students in course: {self.assigned_course}")

assistant1 = TeachingAssistant("Alex_Mukasa", "alex@university.com", "STU-9942", "Advanced Python 101")

assistant1.login()
assistant1.enroll_in_course("Math 1")
assistant1.enroll_students()

#Question 8
print("\n====Question 8====")
class Staff:
    def __init__(self, name, staff_id):
        self.name = name
        self.staff_id = staff_id
        self.is_clocked_in = False

    def clock_in(self):
        self.is_clocked_in = True
        print(f"{self.name} (ID: {self.staff_id}) has clocked in for work.")


class Doctor(Staff):
    def __init__(self, name, staff_id, specialty):
        super().__init__(name, staff_id)
        self.specialty = specialty

    def perform_consultation(self, patient_name):
        if not self.is_clocked_in:
            print(f"Action denied. Dr. {self.name} must clock in first.")
            return
        print(f"Dr. {self.name} is examining {patient_name} regarding {self.specialty}.")


class Nurse(Staff):
    def __init__(self, name, staff_id, assigned_ward):
        super().__init__(name, staff_id)
        self.assigned_ward = assigned_ward

    def check_vitals(self, patient_name):
        if not self.is_clocked_in:
            print(f"Action denied. Nurse {self.name} must clock in first.")
            return
        print(
            f"Nurse {self.name} is checking blood pressure in the {self.assigned_ward} for {patient_name}.")


class Pharmacist(Staff):
    def __init__(self, name, staff_id, license_number):
        super().__init__(name, staff_id)
        self.license_number = license_number

    def dispense_medication(self, prescription_id):
        if not self.is_clocked_in:
            print(f"Action denied. Pharmacist {self.name} must clock in first.")
            return
        print(f"Dispensing order {prescription_id}. Verified under License: {self.license_number}.")


doc = Doctor("Dr. Isaac Nabeta", "DOC-404", "Cardiology")
nurse = Nurse("Sister Mary Namubiru", "NUR-202", "Pediatric Ward")
pharma = Pharmacist("Kintu Moses", "PHM-707", "UG-LIC-99812")

doc.clock_in()
nurse.clock_in()

doc.perform_consultation("Kato John")
nurse.check_vitals("Babirye Sarah")
pharma.dispense_medication("RX-884912")

#Question 9
print("\n====Question 9====")
class SmartDevice:
    def __init__(self, device_id, location):
        self.device_id = device_id
        self.location = location
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"[{self.location} - {self.device_id}] Powered ON.")

    def turn_off(self):
        self.is_on = False
        print(f"[{self.location} - {self.device_id}] Powered OFF.")


class SmartLight(SmartDevice):
    def __init__(self, device_id, location):
        super().__init__(device_id, location)
        self.brightness = 100

    def adjust_brightness(self, level):
        if not self.is_on:
            print(f"Cannot adjust brightness. {self.device_id} is turned off.")
            return

        self.brightness = max(0, min(100, level))
        print(f"[{self.location} - {self.device_id}] Brightness set to {self.brightness}%.")


class SmartThermostat(SmartDevice):
    def __init__(self, device_id, location, current_temp = 22.0):
        super().__init__(device_id, location)
        self.target_temperature = current_temp

    def set_temperature(self, degrees):
        if not self.is_on:
            print(f"Cannot adjust temperature. {self.device_id} is turned off.")
            return

        self.target_temperature = degrees
        print(f"[{self.location} - {self.device_id}] Target temperature set to {self.target_temperature}°C.")

print("--- Initializing Smart Home Ecosystem ---")
living_room_light = SmartLight("LGT-01", "Living Room")
hallway_thermostat = SmartThermostat("TMS-02", "Hallway")

print("\n--- Reusing Power Management ---")
living_room_light.turn_on()
hallway_thermostat.turn_on()

print("\n--- Executing Device-Specific Logic ---")
living_room_light.adjust_brightness(75)
hallway_thermostat.set_temperature(24.5)

print("\n--- Safety State Enforcement Check ---")
living_room_light.turn_off()
living_room_light.adjust_brightness(50)

#Question 10
print("\n====Question 10====")
class Driver:
    def __init__(self, name, vehicle_reg, initial_rating = 5.0):
        self.name = name
        self.vehicle_reg = vehicle_reg
        self.rating = initial_rating

    def calculate_earnings(self):
        pass


class TaxiDriver(Driver):
    def __init__(self, name, vehicle_reg, commission_rate = 0.80):
        super().__init__(name, vehicle_reg)
        self.commission_rate = commission_rate  # Percentage kept by driver
        self.total_fares_collected = 0.0

    def record_trip(self, fare_amount):
        if fare_amount > 0:
            self.total_fares_collected += fare_amount

    def calculate_earnings(self):
        return self.total_fares_collected * self.commission_rate


class DeliveryDriver(Driver):
    def __init__(self, name, vehicle_reg, base_rate_per_delivery = 4.50):
        super().__init__(name, vehicle_reg)
        self.base_rate_per_delivery = base_rate_per_delivery
        self.deliveries_completed = 0

    def record_delivery(self, count = 1):
        if count > 0:
            self.deliveries_completed += count

    def calculate_earnings(self):
        return self.deliveries_completed * self.base_rate_per_delivery


driver_one = TaxiDriver("Peter Mukasa", "UBL 123A",0.85)
driver_two = DeliveryDriver("Sarah Namubiru", "UEM 789B",5.00)

driver_one.record_trip(25000.0)
driver_one.record_trip(18000.0)

driver_two.record_delivery(8)


active_fleet = [driver_one, driver_two]
total_payout_pool = 0.0

print("--- Fleet Earnings Ledger Payout ---")
for driver in active_fleet:
    payout = driver.calculate_earnings()
    total_payout_pool += payout
    print(f"Driver: {driver.name:<15} Reg: {driver.vehicle_reg:<10} Payout Amount: UGX {payout:,.2f}")

print(f"\nTotal Platform Payout Commitment: UGX {total_payout_pool:,.2f}")
