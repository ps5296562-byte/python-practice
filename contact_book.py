contacts = {
     "Poonam":"9483564421",
     "Rahul":"1289767854"
     }
while True:
     print("\nContact Book")
     print("1. Add Contact")
     print("2. View Contacts")
     print("3. Search Contact")
     print("4. Update Contact")
     print("5. Delete Contact")
     print("6. Exit")
     choice = input("Enter your choice:")
     if choice == "1":
        name = input("Enter name:")
        phone = input("Enter phone number:")
        contacts[name] = phone
        print("Contact added successfully.")
     elif choice == "2":
          if contacts:
            for name, phone in contacts.items():
               print(name,":",phone)
          else:
               print("No contacts found.")
     elif choice == "3":
           name = input("Enter name to search:")
           if name in  contacts:
              print("Phone Number:", contacts[name] )
           else:
                print("Contact not found")
     elif choice == "4":
           name = input("Enter name to update:")
           if name in contacts:
              new_phone = input("Enter new phone number:")
              contacts[name] = new_phone
              print("Contact updated.")
           else:
                print("Contact not found.")
     elif choice == "5":
           name = input("Enter name to delete:")
           if name in contacts:
              del contacts[name]
              print("Contact deleted.")
           else:
                print("contact not found.")
     elif choice == "6":
          print("Thank you for using Contact Book.")
          break
     else:
          print("Invalid choice:")
    