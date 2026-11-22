# Program 4: Log analysis using JSON

import json

logs = [
    {"event": "Login", "status": "Success"},
    {"event": "Payment", "status": "Failed"},
    {"event": "Logout", "status": "Success"},
]

with open("logs.json", "w") as file:
    json.dump(logs, file, indent=4)

with open("logs.json", "r") as file:
    data = json.load(file)

success = sum(1 for log in data if log["status"] == "Success")
failed = len(data) - success

print("Total Logs        :", len(data))
print("Successful Events :", success)
print("Failed Events     :", failed)
