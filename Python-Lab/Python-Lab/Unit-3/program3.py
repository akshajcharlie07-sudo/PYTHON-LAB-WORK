# Program 3: Contact book using a dictionary

contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        contacts[name] = input("Enter phone number: ")
        print("Contact added successfully!")

    elif choice == "2":
        if not contacts:
            print("No contacts found.")
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")

    elif choice == "3":
        name = input("Enter name to search: ")
        if name in contacts:
            print(f"Name: {name}, Phone: {contacts[name]}")
        else:
            print("Contact not found.")

    elif choice == "4":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Try again.")
