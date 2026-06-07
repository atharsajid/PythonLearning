# 9. Generator Function with yield
# Problem: Write a generator function that yields even numbers up to a specified limit.

def generate_even(limit):
    for x in range(2, limit + 1, 2): #2 is for step by 1 like 2,4,6
        yield x # return a iterable object and save position in memory like <generator object generate_even at 0x1026ec580>
        

for even in generate_even(10):
    print(even)