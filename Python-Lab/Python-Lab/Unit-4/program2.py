# Program 2: Student records stored in a text file

def add_student():
    usn = input("Enter USN: ")
    name = input("Enter student name: ")
    marks = input("Enter marks: ")
    with open("students.txt", "a") as file:
        file.write(f"{usn},{name},{marks}\n")
    print("Record saved.")


def display_students():
    try:
        with open("students.txt", "r") as file:
            records = file.readlines()
        if not records:
            print("No student records found.")
        else:
            print("\n--- Student Records ---")
            for record in records:
                print(record.strip())
    except FileNotFoundError:
        print("No student records found.")


while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")
