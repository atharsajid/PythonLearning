# 3. Polymorphism in Functions
# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

def multiply(valueOne, valueTwo):
    if valueOne.isdigit():
        valueOne = int(valueOne)

    if valueTwo.isdigit():
        valueTwo = int(valueTwo)
    return valueOne * valueTwo

inputOne = input("Enter Value 1: \n")
inputTwo = input("Enter Value 2: \n")

print(multiply(inputOne, inputTwo))