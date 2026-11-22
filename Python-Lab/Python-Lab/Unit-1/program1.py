# Program 1: Student details, total and average marks

name = input("Enter student name: ")
usn = input("Enter USN: ")
branch = input("Enter branch: ")
semester = int(input("Enter semester: "))

marks = []
for i in range(1, 4):
    marks.append(float(input(f"Enter marks in subject {i}: ")))

total = sum(marks)
average = total / len(marks)

print("\n--- Student Report ---")
print(f"Name     : {name}")
print(f"USN      : {usn}")
print(f"Branch   : {branch}")
print(f"Semester : {semester}")
print(f"Total    : {total}")
print(f"Average  : {average:.2f}")
