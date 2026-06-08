# Problem 2: Debugging Function Calls
# Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.


def debugger(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{k} = {v}" for k, v in kwargs.items())
        print(f"calling {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        # print(f"{func.__name__} called with", *args , *kwargs , "arguments")
        result = func(*args, **kwargs)
        return result
    
    return wrapper

@debugger
def sum(a, b):
    return a+b


print(sum(2,8))
