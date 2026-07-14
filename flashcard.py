flashcards = {
    "What is Python?": "Python is a high-level programming language.",
    "What is a variable?": "A variable stores data.",
    "What is a list?": "A list is an ordered, mutable collection.",
    "What is a tuple?": "A tuple is an ordered, immutable collection.",
    "What is a dictionary?": "A dictionary stores data in key-value pairs.",
    "What does len() do?": "It returns the number of items.",
    "What does input() do?": "It takes input from the user.",
    "What does print() do?": "It displays output on the screen.",
    "What is a function?": "A function is a reusable block of code.",
    "What does break do?": "It exits the current loop."
}

while True:
    print("\n----- Flashcard Program -----")
    print("1. Study Flashcards")
    print("2. Add Flashcard")
    print("3. View All Flashcards")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        for question in flashcards:
            print("\nQuestion:")
            print(question)
            input("Press Enter to see the answer...")
            print("Answer:")
            print(flashcards[question])
            input("Press Enter for next flashcard...")

    elif choice == "2":
        question = input("Enter the question: ")
        answer = input("Enter the answer: ")
        flashcards[question] = answer
        print("Flashcard added successfully.")

    elif choice == "3":
        if len(flashcards) == 0:
            print("No flashcards available.")
        else:
            print("\nAll Flashcards:")
            for question, answer in flashcards.items():
                print("Question:", question)
                print("Answer:", answer)
                print()

    elif choice == "4":
        print("Thank you for using the Flashcard Program!")
        break

    else:
        print("Invalid choice. Please try again.")