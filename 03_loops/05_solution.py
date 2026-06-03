
# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.


text = "sweet"

non_repeated_char = ""

length = len(text)

for i in range(length):
    count = 0
    non_repeated_char = text[i]
    for x in range(length):
        if text[i] == text[x]:
            count += 1
    if count == 1:
        break

print(non_repeated_char)

#Method 2
for char in text:
    if text.count(char) == 1:
        non_repeated_char = char
        break

print(non_repeated_char)