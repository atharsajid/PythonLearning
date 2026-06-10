import turtle
import time
import random

turtle.bgcolor("black")


def get_random_hex():
    # Generates a random integer and formats it as a 6-digit hex code with leading zeros
    return f"#{random.randint(0, 0xFFFFFF):06x}"

t = turtle.Turtle()
t.color('white', 'white')
for i in range(50):
    t.forward(10+ (i*10))
    t.right(90)
    t.color(get_random_hex(), get_random_hex())

turtle.done()
