# Printing letter F
numbers = [5, 2, 5, 2, 2]


for items in numbers:
    new = ""
    for count in range(items):
        new += "X"
    print(new)

# Printing letter L
letters = [0, 0, 0, 0, 2, 2, 2, 2, 5]

for letter in letters:
    old = ""
    for counter in range(letter):
        old += "X"
    print(old)
