# Program 1: Check whether a number is prime

n = int(input("Enter a number: "))

is_prime = n > 1
i = 2
while i * i <= n and is_prime:
    if n % i == 0:
        is_prime = False
    i += 1

print(f"{n} is a Prime Number" if is_prime else f"{n} is not a Prime Number")
