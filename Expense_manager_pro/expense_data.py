import json
def add_expense():
    try:
        expense_id = int(input(" Enter id :"))
    except ValueError:
        print("Invalid ID")
        return
    name = input("Enter name of expense : ")
    try:
        amount = float(input("Enter amount : "))
    except ValueError:
        print("Invalid amount")
        return
    category = input("Enter category : ")
    new_expense = {"id":expense_id, "name": name, "amount":amount, "category":category}
    return new_expense
def save_expenses(expenses):
    with open("data/expenses.json", "w") as file:
        json.dump(expenses,file)

def load_expenses():
    with open("data/expenses.json", "r") as file:
        return json.load(file)
    
