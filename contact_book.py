def display_contacts(users):
    if not users:
        print("No contacts yet.")
        return
    for name, info in users.items():
        print(f"Name: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
        print("-" * 20)


def add_contact(users):
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    users[name] = {"phone": phone, "email": email}
    print("Contact added.")


def remove_contact(users):
    name = input("Name to remove: ")
    if name in users:
        del users[name]
        print("Contact removed.")
    else:
        print("Contact not found.")


def main():
    users = {}
    while True:
        print("Contact Book Menu:")
        print("1. Display contacts")
        print("2. Add contact")
        print("3. Remove contact")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_contacts(users)
        elif choice == "2":
            add_contact(users)
        elif choice == "3":
            remove_contact(users)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
