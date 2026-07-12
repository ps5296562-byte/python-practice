students = {}
while True:
    print("\nStudent Grade Manager ")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    choice = input("Enter your choice:")
    if choice == "1":
        name = ("Enter students name:")
        marks = int(input("Enter marks:"))
        if marks >= 90:
           grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        elif marks >= 40:
            grade = "D"
        else:
            grade = "Fail"
        students[name] = grade
        print("Student added successfully!")
    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            for name, grade in students.items():
                print(name, ":" , grade)
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")