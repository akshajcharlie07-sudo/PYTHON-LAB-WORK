# Program 3: Fibonacci series using a loop

n = int(input("Enter number of terms: "))

first, second = 0, 1
for _ in range(n):
    print(first, end=" ")
    first, second = second, first + second
print()
