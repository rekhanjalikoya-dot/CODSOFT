contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print("\nContact added successfully.\n")


def view_contacts():
    if not contacts:
        print("\nNo contacts found.\n")
        return

    print("\nContact List:")
    print("-" * 30)
    for name, info in contacts.items():
        print(f"Name   : {name}")
        print(f"Phone  : {info['phone']}")
        print(f"Email  : {info['email']}")
        print(f"Address: {info['address']}")
        print("-" * 30)
    print()


def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        info = contacts[name]
        print("\nContact Found:")
        print(f"Name   : {name}")
        print(f"Phone  : {info['phone']}")
        print(f"Email  : {info['email']}")
        print(f"Address: {info['address']}\n")
    else:
        print("\nContact not found.\n")


def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        print("Enter new details:")
        phone = input("New phone: ")
        email = input("New email: ")
        address = input("New address: ")

        contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print("\nContact updated successfully.\n")
    else:
        print("\nContact not found.\n")


def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("\nContact deleted successfully.\n")
    else:
        print("\nContact not found.\n")


# Main loop
while True:
    print("CONTACT BOOK MENU")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("\nExiting program...")
        break
    else:
        print("\nInvalid choice, try again.\n")