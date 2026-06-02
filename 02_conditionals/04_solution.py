
color = input("Enter color: \n")
fruit = input("Enter fruit: \n")

fruits = {
    "Banana" : {
        "Green" : "Unripe", "Yellow" : "Ripe", "Brown" : "Overripe"
    },
    "Mango": {
        "Green" : "Unripe", "Yellow" : "Ripe", "Brown" : "Overripe"
    },
}

print(fruits[fruit][color])