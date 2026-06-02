tea_type = ("Masala", "Green", "Oolong")
print(tea_type[0])
print(tea_type[1:])
print(tea_type[-1])
print(len(tea_type))

more_tea = ("Herbal","Earl Grey")
all_tea = more_tea + tea_type
print(all_tea)

if "Herbal" in all_tea:
    print("Yes we have Herbal Tea")

#Count check
print(all_tea.count("Green"))