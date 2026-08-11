import json
def add_expense(expenses):
    try:
        expense_id = int(input(" Enter id :"))
        for expense in expenses:
            if expense["id"] == expense_id:
                print("Duplicate ID")
                return
    except ValueError:
        print("Invalid ID")
        return
    name = input("Enter name of expense : ")
    if not name:
        print("Invalid name")
        return
    try:
        amount = float(input("Enter amount : "))
        if amount <= 0:
            print("Invalid amount")
            return
    except ValueError:
        print("Invalid amount")
        return
    category = input("Enter category : ")
    if not category:
        print("Invalid Category")
        return
    new_expense = {"id":expense_id, "name": name, "amount":amount, "category":category}
    return new_expense
def save_expenses(expenses):
    with open("data/expenses.json", "w") as file:
        json.dump(expenses,file)

def load_expenses():
    with open("data/expenses.json", "r") as file:
        return json.load(file)
    
