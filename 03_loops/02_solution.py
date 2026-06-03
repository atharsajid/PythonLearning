# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

number = int(input("Enter a number: \n"))

sum = 0

for x in range(number+1):
    if(x % 2 == 0):
        sum += x

print(sum)