# 8. Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = input("Enter Password: \n")

if not password:
    print("You have not entered a correct password")
    exit()

length = len(password)

if length > 10:
    strength = "Strong"
elif length > 5:
    strength = "Medium"
else:
    strength = "Weak"

print("Your Password is", strength)
