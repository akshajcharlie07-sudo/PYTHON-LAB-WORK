# Program 2: Simple calculator using functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return "Cannot divide by zero" if b == 0 else a / b

def floor_divide(a, b):
    return "Cannot divide by zero" if b == 0 else a // b

def modulus(a, b):
    return "Cannot divide by zero" if b == 0 else a % b

def power(a, b):
    return a ** b


operations = {
    "1": ("Addition", add),
    "2": ("Subtraction", subtract),
    "3": ("Multiplication", multiply),
    "4": ("Division", divide),
    "5": ("Floor Division", floor_divide),
    "6": ("Modulus", modulus),
    "7": ("Exponent", power),
}

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\nChoose an operation:")
for key, (label, _) in operations.items():
    print(f"{key}. {label}")

choice = input("Enter choice (1-7): ")

if choice in operations:
    label, func = operations[choice]
    print(f"{label} result: {func(a, b)}")
else:
    print("Invalid choice")
