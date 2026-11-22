# Program 2: Student grading system

subjects = int(input("Enter number of subjects: "))

total = 0
for i in range(1, subjects + 1):
    total += float(input(f"Enter marks for subject {i}: "))

average = total / subjects

if average >= 90:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "Fail"

print("Total   :", total)
print("Average :", round(average, 2))
print("Grade   :", grade)
