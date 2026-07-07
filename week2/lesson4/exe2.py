def student_info(name,age,course,std_number):
    print("Student Info".center(30,"*"))
    print(f"Name: {name}\nAge: {age}\nCourse: {course}\nStudy Number: {std_number}")


#Input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
course = input("Enter your course: ")
std_number = input("Enter your std_number: ")


student_info(name, age, course, std_number)