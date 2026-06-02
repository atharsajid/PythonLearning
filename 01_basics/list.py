chai_varities = ["Masala", "Green", "Lemon", "Mint"]
print(chai_varities[0])
print(chai_varities[:])
print(chai_varities[:3])
print(chai_varities[0:3:2])

chai_varities[1:2] = ["Black"]
print(chai_varities)

chai_varities[1:1] = ["White"] #Insert
print(chai_varities)

chai_varities[1:2] = [] #Insert Nothing or Delete 
print(chai_varities)

#For In Loop
for tea in chai_varities:
    print(tea, end = " - ")

print("")
#Append / Add in list
chai_varities.append("Oolong")


if "Oolong" in chai_varities :
    print("List have Oolong tea")

#Remove Last Element
chai_varities.pop()

#Remove element
chai_varities.remove("Lemon")

#Insert
chai_varities.insert(1, "Blue")

#Copy List
chai_varities_copy = chai_varities.copy()

#Comprehensive Loop
squared_list = [x**2 for x in range(10)]
print(squared_list)

cube_list = [y**3 for y in range(10)]
print(cube_list)