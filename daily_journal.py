def write_journal():
    entry = input("Write your journal: ")

    with open("journal.txt", "a") as file:
        file.write(entry + "\n")

    print("Journal saved successfully!")


def view_journal():
    try:
        with open("journal.txt", "r") as file:
            data = file.read()

            if data:
                print("\n----- Daily Journal -----")
                print(data)
            else:
                print("Journal is empty.")

    except FileNotFoundError:
        print("No journal found.")


while True:
    print("\nDaily Journal")
    print("1. Write Journal")
    print("2. View Journal")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        write_journal()

    elif choice == "2":
        view_journal()

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")