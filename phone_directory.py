phone_directory = {}

while True:
    print("\nPhone Directory")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")

        if name in phone_directory:
            print("Contact already exists!")
        else:
            phone_directory[name] = phone
            print("Contact added successfully!")

    elif choice == "2":
        if len(phone_directory) == 0:
            print("No contacts found.")
        else:
            print("\nContact List")
            for name, phone in phone_directory.items():
                print(name, ":", phone)

    elif choice == "3":
        name = input("Enter Name to Search: ")

        if name in phone_directory:
            print("Phone Number:", phone_directory[name])
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter Name to Update: ")

        if name in phone_directory:
            new_phone = input("Enter New Phone Number: ")
            phone_directory[name] = new_phone
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    elif choice == "5":
        name = input("Enter Name to Delete: ")

        if name in phone_directory:
            del phone_directory[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    elif choice == "6":
        print("Thank you for using Phone Directory!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")