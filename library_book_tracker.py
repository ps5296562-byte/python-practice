library = {
    "Python": "Available",
    "Java": "Borrowed",
    "C++": "Available"
}

while True:
    print("\nLibrary Book Tracker")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")

        if book in library:
            print("Book already exists.")

        else:
            library[book] = "Available"
            print("Book added successfully.")

    elif choice == "2":

        if len(library) == 0:
            print("No books available.")

        else:
            for book, status in library.items():
                print(book, "-", status)

    elif choice == "3":

        book = input("Enter book name: ")

        if book in library:
            print(book, "-", library[book])

        else:
            print("Book not found.")

    elif choice == "4":

        book = input("Enter book name: ")

        if book in library:

            if library[book] == "Available":
                library[book] = "Borrowed"
                print("Book borrowed successfully.")

            else:
                print("Book is already borrowed.")

        else:
            print("Book not found.")

    elif choice == "5":

        book = input("Enter book name: ")

        if book in library:

            if library[book] == "Borrowed":
                library[book] = "Available"
                print("Book returned successfully.")

            else:
                print("Book is already available.")

        else:
            print("Book not found.")

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")