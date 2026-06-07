# 10. Recursive Function
# Problem: Create a recursive function to calculate the factorial of a number.

def factorial(number, ans = 1):
    if number <= 1:
        print("Ans:", ans)
        return ans
    ans = number * ans
    return factorial(number = number - 1, ans=ans)



ans = factorial(5)

print(ans)

#Method 2
def factorial(n):
    if n <= 1:
        return n
    return n * factorial(n-1)


print("Method 2: ", factorial(5))