# Program 4: Retail sales report with CSV and a bar chart
# Requires: pip install matplotlib

import csv
import matplotlib.pyplot as plt

sales = {
    "Laptop": 50000,
    "Mobile": 30000,
    "Tablet": 20000,
    "Headphones": 10000,
}

with open("sales.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Product", "Sales"])
    writer.writerows(sales.items())

print("--- Retail Sales Report ---")
for product, amount in sales.items():
    print(f"{product}: {amount}")
print("Total Sales:", sum(sales.values()))

plt.bar(sales.keys(), sales.values())
plt.title("Retail Sales Dashboard")
plt.xlabel("Products")
plt.ylabel("Sales Amount")
plt.savefig("sales_chart.png")
plt.show()
