students = {}

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        sid = int(input("Enter ID: "))
        if sid in students:
            print("ID already exists!")
        else:
            name = input("Name: ")
            age = int(input("Age: "))
            course = input("Course: ")
            marks = float(input("Marks: "))
            students[sid] = {"name": name, "age": age,
                             "course": course, "marks": marks}
            print("Student added successfully.")

    elif choice == "2":
        if len(students) == 0:
            print("No records found.")
        else:
            for sid, info in students.items():
                print(f"ID: {sid} | Name: {info['name']} | Age: {info['age']} "
                      f"| Course: {info['course']} | Marks: {info['marks']}")

    elif choice == "3":
        sid = int(input("Enter ID to search: "))
        if sid in students:
            print(sid, students[sid])
        else:
            print("Student not found.")

    elif choice == "4":
        sid = int(input("Enter ID to update: "))
        if sid in students:
            students[sid]["name"] = input("New name: ")
            students[sid]["age"] = int(input("New age: "))
            students[sid]["course"] = input("New course: ")
            students[sid]["marks"] = float(input("New marks: "))
            print("Updated successfully.")
        else:
            print("Student not found.")

    elif choice == "5":
        sid = int(input("Enter ID to delete: "))
        if sid in students:
            del students[sid]
            print("Deleted successfully.")
        else:
            print("Student not found.")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")