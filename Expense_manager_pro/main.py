import expenses

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

def main():
    project_name = "Expense Manager Pro"
    version = "1.0"
    project_heading(project_name,version)
    manager = expenses.ExpenseManager()
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
            print("-" * 30)
        except ValueError:
            print("Invalid Choice")
            continue
        if choice == 1:
            manager.add_expense()
            print("Expense added successfully..!")
        elif choice == 2:
            manager.view_expenses()
        elif choice == 3:
            total = manager.calculate_total()
            print(f"Total Amount Spent : ₹ {total}")  #\u20b9 is unicode for indian rupee symbol
        elif choice == 4:
            print(f"Thank you for using {project_name} !!!")
            break
        else:
            print("Invalid Choice. Please enter right choice between(1 to 4) :")

main()