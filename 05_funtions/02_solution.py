# 2. Function with Multiple Parameters
# Problem: Create a function that takes two numbers as parameters and returns their sum.

def sumNumber(num1, num2):
    return num1 + num2


num1 = int(input("Enter Number 1: \n"))
num2 = int(input("Enter Number 2: \n"))

result = sumNumber(num1, num2)

print("Result:", result)

