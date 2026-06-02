# 10. Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

species =input("What do you have Cat or Dog? \n").lower()
age = int(input("How old are your {}? \n".format("Cat" if species == "cat" else "Dog")))

if species == "cat":
    if age > 5 :
        print("Senior cat food")
    else:
        print("Junior cat food")
elif species == "dog":
    if age> 2:
        print("Dog Food")
    else:
        print("Puppy Food")