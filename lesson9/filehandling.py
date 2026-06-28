#File Opening
# file = open('student.txt','r')
# content = file.read()
#
# print(content)
# file.close()

# New File Method
# with open('student.txt', 'r') as file:
#     content = file.read()
#     print(content)

'''
r - read
w - write
a - append
'''
import csv

# with open('report.txt', 'w') as file:
#     file.write('I love Python Programming\n')
#     file.write('I am becoming a data Scientist')
#
#
# with open('report.txt', 'a') as file:
#     file.write('Every Data Scientist Must learn python')
#     print('file appended')

# CSV files

#Reading
# with open ('students.csv', 'r') as file:
#     reader = csv.reader(file)
#
#     for row in reader:
#         print(row)

#Writing
# data = [
#     ['24/U/07423/PS','MUSINGUZI MARK', 'MALE', 22, 'BSSE', '90']
# ]
#
# with open('students.csv', 'w', newline= "") as file:
#     writer = csv.writer(file)
#     writer.writerow(data)

#Appending
# data = [
#     '24/U/07423/PS','MUSINGUZI MARK', 'MALE', 22, 'BSSE', 90
# ]
#
# with open('students.csv', 'a', newline= "") as file:
#     writer = csv.writer(file)
#     writer.writerow(data)
#     print("Done Appending")

#JSON


