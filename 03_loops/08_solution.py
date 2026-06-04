# 8. Prime Number Checker
# Problem: Check if a number is prime.

number = int(input("Enter Number: \n"))

divide_by = 2

if number <=1:
    print(number, "is not a Prime Number")
    exit()

while (number % divide_by) != 0:
    divide_by += 1

if number == divide_by:
    print(number, "is a Prime Number")
else:
    print(number, "is not a Prime Number")


# Method 2

is_prime = True

for i in range(2, number):
    if (number % i )== 0:
        is_prime = False
        break

if number == divide_by:
    print(number, "is a Prime Number")
else:
    print(number, "is not a Prime Number")