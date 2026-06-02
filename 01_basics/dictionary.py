chai_types = {
    "Masala": "Spicy",
    "Ginger": "Zesty",
    "Green": "Mild"
}

#Copy
chai_types_copy = chai_types.copy()

print(chai_types["Masala"]) #To Get value but will throw error if key not found
print(chai_types.get("Green")) #To Get value, return None if key not found

chai_types["Doodh Patti"] = "Sweet"

print(chai_types)

#Loop
for chai in chai_types:
    print(chai, " : ", chai_types[chai])

for key, value in chai_types.items():
    print(key, value)

print(chai_types.items())

#Check Keys
if "Masala" in chai_types:
    print("Dictionary have Masala Tea")

print(len(chai_types))

#Remove
chai_types.pop("Green")
chai_types.popitem() #Will remove last element
del chai_types["Masala"]

print(chai_types)


#Nested Dictionary
tea_shop = {
    "chai" :  {
        "Masala": "Spicy",
        "Ginger": "Zesty",
    },
    "tea" : {
        "Green": "Mild",
        "Black": "Strong"
    }
}

print(tea_shop["chai"]["Ginger"])

squared_nums = {x:x**2 for x in range(10)}

print(squared_nums)

#Clear all items
squared_nums.clear()

keys = ["Masala", "Ginger", "Lemon"]
default_value = "Delicious"

new_dict = {x:default_value for x in keys}
print(new_dict)

new_dict = dict.fromkeys(keys, default_value)

print(new_dict)