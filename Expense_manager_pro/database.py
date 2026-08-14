import json
def save_expenses(expense_list):
    with open("data/expenses.json", "w") as file:
        json.dump(expense_list,file)

def load_expenses():
    with open("data/expenses.json", "r") as file:
        return json.load(file)
