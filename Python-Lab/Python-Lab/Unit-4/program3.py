# Program 3: Payroll system using a CSV file

import csv

try:
    n = int(input("Enter number of employees: "))

    with open("payroll.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Employee ID", "Name", "Basic Salary",
                         "Allowance", "Deduction", "Net Salary"])

        for i in range(1, n + 1):
            print(f"\nEmployee {i}")
            emp_id = input("Employee ID: ")
            name = input("Name: ")
            basic = float(input("Basic Salary: "))
            allowance = float(input("Allowance: "))
            deduction = float(input("Deduction: "))
            writer.writerow([emp_id, name, basic, allowance,
                             deduction, basic + allowance - deduction])

    print("\n--- Payroll Report ---")
    with open("payroll.csv", "r") as file:
        for row in csv.reader(file):
            print(" | ".join(row))

except ValueError:
    print("Invalid input. Please enter numbers where required.")
