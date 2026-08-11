from expense_data import add_expense, save_expenses, load_expenses
def project_heading(project_name,version):
    print("=" * 60)
    print(project_name.center(60))
    print(version.center(60))
    print("=" * 60)

def display_menu():
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Exit")   
    
def view_expenses(expenses):
    if not expenses:
        print("No expense found.")
        return
    for expense in expenses:
        print("-"*30)
        print(f"expense_id   : {expense['id']}")           
        print(f"name         : {expense['name']}")
        print(f"Amount       : {expense['amount']}") 
        print(f"Category     : {expense['category']}") 
         

def main():
    project_name = "Expense Manager Pro"
    version = "0.6"
    project_heading(project_name,version)
    expenses = load_expenses()
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
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
            print(f"Thank you for using {project_name} !!!")
            break
        else:
            print("Invalid Choice. Please enter right choice between(1 to 3) :")

main()