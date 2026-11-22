# Program 4: Attendance tracker using nested dictionaries

attendance = {}
STUDENTS = 4

while True:
    print("\n1. Mark Attendance")
    print("2. Search Attendance")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        date = input("Enter date (YYYY-MM-DD): ")
        present = absent = 0
        for i in range(1, STUDENTS + 1):
            status = input(f"Student {i} (p/a): ").lower()
            if status == "p":
                present += 1
            elif status == "a":
                absent += 1
            else:
                print("Invalid input, counted as absent.")
                absent += 1
        attendance[date] = {"present": present, "absent": absent}
        print(f"Present: {present}, Absent: {absent}")

    elif choice == "2":
        date = input("Enter date to search: ")
        print(attendance.get(date, "No record found for this date."))

    elif choice == "3":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Try again.")
