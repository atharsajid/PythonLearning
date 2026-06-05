# 7. Function with *args
# Problem: Write a function that takes variable number of arguments and returns their sum.

def sum_all(*args): #To Take multiple arguments, args are Tuple like (1,2,3), it can be iterate, it can also be written like *chai
    return sum(args)


print(sum_all(1,2))
print(sum_all(1,2,3,4,5))
print(sum_all(1,2,3,4,5,6,7,8))