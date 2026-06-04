# 7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.

# number = -1

# while number < 1 or number > 10:
#     number = int(input("Guess Number: \n"))

# print("Correct Guess")

#Method 2
while True:
    number = int(input("Enter value between 1 and 10: \n"))
    if 1 <= number <= 10:
        break

