file = open("youtube.txt", "w")

#Method 1
try:
    file.write("Hello World")
finally:
    file.close()

file = open("youtube.txt")

print(file.readlines())

#Method 2
with open("database", "w") as file:
    file.write("Hello World")
