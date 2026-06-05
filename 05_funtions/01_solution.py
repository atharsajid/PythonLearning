# 1. Basic Function Syntax
# Problem: Write a function to calculate and return the square of a number.

#Function Definition 

def squareOfNumber(num):
    return num**2

input = int(input("Enter Number: \n"))

result = squareOfNumber(input)

print("Square of", input, "is:", result)