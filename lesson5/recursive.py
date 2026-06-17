#Recursive Functions

#Lab Activity 3
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

def factorial2(n):
    if n == 1:
        return 1

    return n * factorial2(n-1)

print(factorial2(5))

#Count down
def count_down(n):
    if n == 0:
        print("Finished")
    else:
        print(n)
        count_down(n-1)

count_down(5)

#Fibonacci
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print([fibonacci(n) for n in range(6)])

#Example 5 Binary Search using a recursive
def binary_search(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)

my_list = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(my_list, 5, 0, len(my_list)))
