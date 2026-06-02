# 1. Age Group Categorization
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult

userinput = input("Please enter Age: \n")

userinput_in_int = int(userinput)

if userinput_in_int < 13:
    print("Your Age is", userinput_in_int, ". You are a Child")
elif userinput_in_int < 20:
    print("Your Age is", userinput_in_int, ". You are a Teenage")
elif userinput_in_int < 60:
    print("Your Age is", userinput_in_int, ". You are a Adult")
else:
    print("Your Age is", userinput_in_int, ". You are a Senior")

