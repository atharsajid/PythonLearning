#2. Movie Ticket Pricing
#Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on

#Method 1
age = int(input("How old are you: \n"))
isWednesday = False
price = 12

if age < 18:
    price = 8

if isWednesday:
    price = price - 2

print("Ticket price is", price)

#Method 2

age = int(input("How old are you: \n"))
isWednesday = False
price = 12 if age >= 18 else 8

if isWednesday :
    price -= 2

print("Ticket price is ${}".format(price))

