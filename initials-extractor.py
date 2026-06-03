full_name = input("Enter your full name? ")
names = full_name.split()
initials = ".".join([names[0].upper() for names in names])
print(f"Your initials are: {initials}")
