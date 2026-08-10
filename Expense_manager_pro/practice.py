import json
expenses = [
    {
        "id": 1,
        "name": "Apple",
        "amount": 100,
        "category": "Food"
    }
]
file = open("data/expenses.json", "w")
json.dump(expenses,file)
file.close()

file = open("data/expenses.json", "r")
expenses = json.load(file)
file.close()
print(expenses)