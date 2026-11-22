# Program 1: Frequency of elements in a list using a dictionary

numbers = [1, 2, 3, 2, 4, 1, 3, 3, 2]

frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

print("List     :", numbers)
print("Frequency:", frequency)
