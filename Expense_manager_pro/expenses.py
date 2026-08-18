import database
class ExpenseManager:
    def __init__(self):
        self.expense_list = database.load_expenses()

    def add_expense(self):
        try:
            expense_id = int(input(" Enter id :"))
            for expense in self.expense_list:
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
        self.expense_list.append(new_expense)
        database.save_expenses(self.expense_list)

    def view_expenses(self):
        if not self.expense_list:
            print("No expense found.")
            return
        for expense in self.expense_list:
            print(f"expense_id   : {expense['id']}")           
            print(f"name         : {expense['name']}")
            print(f"Amount       : {expense['amount']}") 
            print(f"Category     : {expense['category']}") 
            print("-"*30)

    def calculate_total(self):
        total = 0
        for expense in self.expense_list:
            total += expense["amount"]
        return total









         
