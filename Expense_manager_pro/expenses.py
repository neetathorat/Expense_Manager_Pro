import database
class ExpenseManager:
    """Manage expenses and perform expense operations."""
    def __init__(self):
        self.expenses = database.load_expenses()

    def add_expense(self):
        """Add a new expense and save it to the database."""
        try:
            expense_id = int(input(" Enter id :"))
            for expense in self.expenses:
                if expense["id"] == expense_id:
                    print("Duplicate ID")
                    return False
        except ValueError:
            print("Invalid ID")
            return False
        name = input("Enter name of expense : ").strip()
        if not name:
            print("Invalid name")
            return False
        try:
            amount = float(input("Enter amount : "))
            if amount <= 0:
                print("Invalid amount")
                return False
        except ValueError:
            print("Invalid amount")
            return False
        category = input("Enter category : ").strip()
        if not category:
            print("Invalid Category")
            return False
        new_expense = {"id":expense_id, "name": name, "amount":amount, "category":category}
        self.expenses.append(new_expense)
        database.save_expenses(self.expenses)
        return True

    def view_expenses(self):
        """Display all stored expenses."""
        if not self.expenses:
            print("No expense found.")
            return
        for expense in self.expenses:
            print(f"expense_id   : {expense['id']}")           
            print(f"name         : {expense['name']}")
            print(f"Amount       : {expense['amount']}") 
            print(f"Category     : {expense['category']}") 
            print("-"*30)

    def edit_expense(self):
        """Edit an existing expense and save the changes."""
        try:
            expense_id = int(input("Enter expense ID to edit: "))

            expense_to_edit = None

            for expense in self.expenses:
                if expense["id"] == expense_id:
                    expense_to_edit = expense
                    break

            if expense_to_edit is None:
                print("Expense ID not found.")
                return

            print("Current Expense:")
            print(f"Name: {expense_to_edit['name']}")
            print(f"Amount: {expense_to_edit['amount']}")
            print(f"Category: {expense_to_edit['category']}")

            name = input("Enter new name: ").strip()
            if not name:
                print("Invalid name")
                return False
            try:
                amount = float(input("Enter amount : "))
                if amount <= 0:
                    print("Invalid amount")
                    return False
            except ValueError:
                print("Invalid amount")
                return False
            category = input("Enter category : ").strip()
            if not category:
                print("Invalid Category")
                return False
            expense_to_edit["name"] = name
            expense_to_edit["amount"] = amount
            expense_to_edit["category"] = category

            database.save_expenses(self.expenses)

            print("Expense updated successfully.")

        except ValueError:
            print("Invalid input.")

    def remove_expense(self):
        """Remove an existing expense and save the changes."""
        try:
            expense_id = int(input("Enter expense ID to remove: "))

            expense_to_remove = None

            for expense in self.expenses:
                if expense["id"] == expense_id:
                    expense_to_remove = expense
                    break

            if expense_to_remove is None:
                print("Expense ID not found.")
                return

            self.expenses.remove(expense_to_remove)
            database.save_expenses(self.expenses)

            print("Expense removed successfully.")

        except ValueError:
            print("Invalid ID. Please enter a number.")       



    def calculate_total(self):
        """Calculate and return the total expense amount."""
        total = 0
        for expense in self.expenses:
            total += expense["amount"]
        return total









         
