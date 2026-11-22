# Program 1: Read a log file and count ERROR messages

try:
    count = 0
    with open("log.txt", "r") as file:
        for line in file:
            print(line.strip())
            if "ERROR" in line:
                count += 1
    print("Total ERROR messages:", count)
except FileNotFoundError:
    print("Error: log.txt does not exist.")
