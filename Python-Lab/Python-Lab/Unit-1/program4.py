# Program 4: Electricity bill calculation

name = input("Enter consumer name: ")
consumer_id = input("Enter consumer ID: ")
previous = float(input("Enter previous meter reading: "))
current = float(input("Enter current meter reading: "))
rate = float(input("Enter cost per unit: "))

units = current - previous
energy_charge = units * rate
duty = 0.05 * energy_charge        # 5% electricity duty
fixed_charge = 100                 # fixed meter charge
net_amount = energy_charge + duty + fixed_charge

print("\n--- Electricity Bill ---")
print("Consumer Name      :", name)
print("Consumer ID        :", consumer_id)
print("Units Consumed     :", units)
print("Energy Charge      :", round(energy_charge, 2))
print("Electricity Duty   :", round(duty, 2))
print("Fixed Meter Charge :", fixed_charge)
print("Net Bill Amount    :", round(net_amount, 2))
