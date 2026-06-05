# 8. Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.


def print_kwargs(**kwargs): #To takes multiple arguments with named parameters
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name = "Spiderman", power = " Web Shooting", enemy = "Dr. Octopus")

print_kwargs(name = "IronMan", power = "Rich",)

print_kwargs(power = "Rich",)