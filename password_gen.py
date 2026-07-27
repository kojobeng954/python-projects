import string
import random


def new_password():
    characters = list(string.ascii_uppercase + string.ascii_lowercase + string.digits)

    num = int(input("Number of letters for your password: "))
    generated = ""

    for _ in range(num):
        generated += random.choice(characters)
    return generated


print(new_password())
