chai = "Lemon Tea"
first_char = chai[0]
print(first_char)
slice_chai = chai[0:5]
print(slice_chai)
print(chai.lower())
print(chai.upper())
print(chai.strip()) #Trim
print(chai.replace("Lemon", "Ginger"))
chai = "Lemon, Green, Masala, Mint"
print(chai.split(", "))
chai = "Lemon Tea"
print(chai.find("Tea"))
print(chai.count("e"))



#Slicing
slicing = "0123456789"
print(slicing[:])
print(slicing[:3]) #Start with 0
print(slicing[3:]) #End to the last index
print(slicing[0:7:2]) #Steps by 2 or skip by 2
print(slicing[-5:-3])


#Order Formatting
chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai" # {} means placeholder
print(order.format(quantity, chai_type))

#Join
chai_variety = ["Lemon", "Green", "Ginger"]
print(", ".join(chai_variety))
print(" - ".join(chai_variety))
print(len(chai))

#Raw Strings
chai = "Lemon\nTea"
print(chai) #It will go to the next line
chai = r"Lemon\nTea"
print(chai) #It will print same as it is written

#Contains
chai = "Lemon Tea"
print("Lemon" in chai) #check Lemon is contains in chai
