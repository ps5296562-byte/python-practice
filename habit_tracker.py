habits = []

while True:
    print("\nHabit Tracker")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Mark Habit as Completed")
    print("4. Delete Habit")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        habit = input("Enter habit name: ")
        habits.append({"name": habit, "status": "Pending"})
        print("Habit added successfully.")

    elif choice == "2":
        if len(habits) == 0:
            print("No habits found.")
        else:
            print("\nYour Habits:")
            for i in range(len(habits)):
                print(f"{i + 1}. {habits[i]['name']} - {habits[i]['status']}")

    elif choice == "3":
        if len(habits) == 0:
            print("No habits to update.")
        else:
            for i in range(len(habits)):
                print(f"{i + 1}. {habits[i]['name']} - {habits[i]['status']}")

            number = int(input("Enter habit number to mark as completed: "))

            if 1 <= number <= len(habits):
                habits[number - 1]["status"] = "Completed"
                print("Habit marked as completed.")
            else:
                print("Invalid habit number.")

    elif choice == "4":
        if len(habits) == 0:
            print("No habits to delete.")
        else:
            for i in range(len(habits)):
                print(f"{i + 1}. {habits[i]['name']} - {habits[i]['status']}")

            number = int(input("Enter habit number to delete: "))

            if 1 <= number <= len(habits):
                deleted = habits.pop(number - 1)
                print(f"{deleted['name']} deleted successfully.")
            else:
                print("Invalid habit number.")

    elif choice == "5":
        print("Thank you for using Habit Tracker.")
        break

    else:
        print("Invalid choice. Please try again.")