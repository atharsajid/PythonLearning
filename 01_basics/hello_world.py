import math
import random
print("Hello World")

def func1(n):
    print(n)

func1(5)

variable1 = "Variable 1"
variable2 = "Variable 2"
variable3 = "Variable 3"

#Copy Reference
h1 = [1, 2, 3, 4]
h2 = h1[:]
h1[0] = 55

print(h1)
print(h2)


#Check value is same
n1 = [1, 2, 3, 4]
n2 = [1, 2, 3, 4]
print(n1 == n2) #True


#Check Reference is same
n1 = [1, 2, 3, 4]
n2 = [1, 2, 3, 4]
print(n1 is n2) #False

#numbers
x = 2
y = 3
z = 4

print(x + y)
print((x + y) * z)

x = 40
y = 2.25
print(x+y)

x = float(x)
y = float(y)

print(x+y)

x = int(x)
y = int(y)

print(x+y)

x = float("10.5")

print(x)

def factorial(n):
    ans = 1
    while n > 1:
        ans = ans * n
        n = n -1

    print(ans)
 

factorial(300)

math.floor(3.5) #3 
math.floor(-3.5) #4
math.trunc(2.5) #2
math.trunc(-2.5) #2 Nearest to 0

x = random.random()
y = random.randint(1, 100)
print(x)
print(y)
random.choice([1,2,3,4])
random.shuffle([1,2,3,4])

