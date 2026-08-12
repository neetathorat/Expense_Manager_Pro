from expense_data import add_expense, save_expenses, load_expenses
def project_heading(project_name,version):
    print("=" * 60)
    print(project_name.center(60))
    print(version.center(60))
    print("=" * 60)

def display_menu():
    print("-" * 30)
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Show Total")
    print("4. Exit")   
    
def view_expenses(expenses):
    if not expenses:
        print("No expense found.")
        return
    for expense in expenses:
        print(f"expense_id   : {expense['id']}")           
        print(f"name         : {expense['name']}")
        print(f"Amount       : {expense['amount']}") 
        print(f"Category     : {expense['category']}") 
        print("-"*30)
         
def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


def main():
    project_name = "Expense Manager Pro"
    version = "1.0"
    project_heading(project_name,version)
    expenses = load_expenses()
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
            print("-" * 30)
        except ValueError:
            print("Invalid Choice")
            continue
        if choice == 1:
            new_expense = add_expense(expenses)
            if new_expense is not None:
                expenses.append(new_expense)
                save_expenses(expenses)
                print("Expense added successfully..!")
        elif choice == 2:
            view_expenses(expenses)
        elif choice == 3:
            total = calculate_total(expenses)
            print(f"Total Amount Spent : ₹ {total}")  #\u20b9 is unicode for indian rupee symbol
        elif choice == 4:
            print(f"Thank you for using {project_name} !!!")
            break
        else:
            print("Invalid Choice. Please enter right choice between(1 to 4) :")

main()