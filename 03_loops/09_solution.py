# 9. List Uniqueness Checker
# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

items = ["apple", "banana", "orange", "banana", "mango"]

for item in items:
    if items.count(item) > 1:
        print("Duplicate", item)
        break


#Method
unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate", item)
        break
    unique_item.add(item)