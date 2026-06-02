# 6. Transportation Mode Selection
# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

distance = float(input("Enter distance: \n"))
print(type(distance))
if not isinstance(distance, float):
    print("Please enter correct distance")
    exit()

if distance > 15:
    activity = "Car"
    
elif distance >= 3:
    activity = "Bike"
else:
    activity = "Walk"

print(activity)