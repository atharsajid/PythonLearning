# 3. Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but

number = int(input("Enter number: \n"))

for i in range(1, 10 +1):
    if i == 5:
        continue
    print("{} X {} = {}".format(number, i , number * i))



