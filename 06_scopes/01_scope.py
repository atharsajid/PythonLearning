#Scope is refer to where a variable can be used.
#Global Scope
#Local Scope
#Enclosing Scope

x = 99 #Global Scope

def func(y):
    z = x + y
    return z

result = func(11)
print(result)

a = 100 

def func():
    global a #to change global variable other wise it will change to global variable, avoid to change global variable
    a = 50

func()

print(a)

x = 99
#closure
def f1():
    x = 22
    def f2():
        print(x)

    return f2 #This is the closure which returns the definition of function and also return the associated variable references

result = f1()
result();


def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2)
g = chaicoder(3)

print(f(3))
print(g(3))