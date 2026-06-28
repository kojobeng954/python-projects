numbers = [3, 5, 3, 1, 1, 4, 1, 4, 4, 2]
unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)

print(unique)
