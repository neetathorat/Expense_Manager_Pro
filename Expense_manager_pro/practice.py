def add_expense(expense_list):
    try:
        expense_id = int(input(" Enter id :"))
        for expense in expense_list:
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

def view_expenses(expense_list):
    if not expense_list:
        print("No expense found.")
        return
    for expense in expense_list:
        print(f"expense_id   : {expense['id']}")           
        print(f"name         : {expense['name']}")
        print(f"Amount       : {expense['amount']}") 
        print(f"Category     : {expense['category']}") 
        print("-"*30)

def calculate_total(expense_list):
    total = 0
    for expense in expense_list:
        total += expense["amount"]
    return total
