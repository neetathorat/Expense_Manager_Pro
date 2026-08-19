import expenses

def project_heading(project_name, version):
    """Display the project name and version."""
    print("=" * 60)
    print(project_name.center(60))
    print(version.center(60))
    print("=" * 60)

def display_menu():
    """Display the main menu options."""
    print("-" * 30)
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Edit Expense")
    print("4. Remove Expense")
    print("5. Show Total")
    print("6. Exit")      

def main():
    """Run the Expense Manager Pro application."""
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
            result = manager.add_expense()
            if result:
                print("Expense added successfully..!")
        elif choice == 2:
            manager.view_expenses()
        elif choice == 3:
            manager.edit_expense()
        elif choice == 4:
            manager.remove_expense()
        elif choice == 5:
            total = manager.calculate_total()
            print(f"Total Amount Spent : ₹ {total}")  
        elif choice == 6:
            print(f"Thank you for using {project_name} !!!")
            break
        else:
            print("Invalid Choice. Please enter right choice between(1 to 6) :")

main()