def add_expense():
    try:
        expense_id = int(input(" Enter id :"))
    except ValueError:
        print("Invalid ID")
        return
    expense_name = input("Enter name of expense : ")
    try:
        amount = float(input("Enter amount : "))
    except ValueError:
        print("Invalid amount")
        return
    category = input("Enter category : ")
    new_expense = {"id":expense_id, "expense_name": expense_name, "amount":amount, "category":category}
    return new_expense

