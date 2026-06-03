# 4. Reverse a String
# Problem: Reverse a string using a loop.

text = "Hello"
reversed = ""

for char in text:
    reversed = char + reversed
    

print(reversed)