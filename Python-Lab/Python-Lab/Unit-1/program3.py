# Program 3: Number operations using the math module

import math

n = float(input("Enter a number: "))

print("\n1. Square")
print("2. Cube")
print("3. Square root")
print("4. Ceiling")
print("5. Floor")
print("6. Absolute value")
print("7. Data type")
print("8. Memory address")

choice = input("Enter choice (1-8): ")

if choice == "1":
    print("Square:", n ** 2)
elif choice == "2":
    print("Cube:", n ** 3)
elif choice == "3":
    if n < 0:
        print("Square root of a negative number is not real")
    else:
        print("Square root:", math.sqrt(n))
elif choice == "4":
    print("Ceiling:", math.ceil(n))
elif choice == "5":
    print("Floor:", math.floor(n))
elif choice == "6":
    print("Absolute value:", abs(n))
elif choice == "7":
    print("Type:", type(n))
elif choice == "8":
    print("Address:", id(n))
else:
    print("Invalid choice")
