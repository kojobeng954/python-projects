first_name = input("What is your first name? ")
birth_year = int(input("WHich year were you born? "))

username = f"{first_name[0:].lower()}_{birth_year}"
print(f"Your username is {username}.")
