# 9. Leap Year Checker
# Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

year = int(input("Enter year: \n"))

isLeapYear = False

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            isLeapYear = True
    else:
        isLeapYear = True

print(year, "is a","Leap Year" if isLeapYear else "not a Leap Year")
