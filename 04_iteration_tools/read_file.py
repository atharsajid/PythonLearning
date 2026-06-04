

for line in open("file.py"):
    print(line)


f = open("file.py")
print(f.readline()) #Method 1 empty when file complete
print(f.__next__()) #Method 2 but exception throw when file complete

f = open("file.py")

while True:
    line = f.readline()
    print(line)
    if(line == ""): #or if not line
        break