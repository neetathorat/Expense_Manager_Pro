import expenses
import reports

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
    print("6. Category Report")
    print("7. Filter by Category")
    print("8. Sort Expenses by Amount")
    print("9. Sort Categories by Total")
    print("10. Exit")      

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
            total = reports.calculate_total(manager.expenses)
            print(f"Total Amount Spent : ₹ {total}")  
        elif choice == 6:
            category_totals = reports.calculate_category_total(manager.expenses)
            if not category_totals:
                print("No expenses found.")
            else:
                for category, total in category_totals.items():
                    print(f"{category} : ₹ {total}")
        elif choice == 7:
            category = input("Enter category: ").strip()
            filtered_expenses = reports.filter_expenses(manager.expenses, category)
            if not filtered_expenses:
                print("No expenses found for this category.")
            else:
                for expense in filtered_expenses:
                    print(f"Expense ID : {expense['id']}")
                    print(f"Name       : {expense['name']}")
                    print(f"Amount     : ₹ {expense['amount']}")
                    print(f"Category   : {expense['category']}")
                    print("-" * 30)
        elif choice == 8:
            if not manager.expenses:
                print("No expenses found.")
                continue
            sort_choice = input("Enter 1 for lowest to highest or 2 for highest to lowest: ").strip()
            if sort_choice == "1":
                sorted_expenses = reports.sort_expenses_by_amount(manager.expenses)
            elif sort_choice == "2":
                sorted_expenses = reports.sort_expenses_by_amount(manager.expenses, reverse = True)             
            else:
                print("Invalid sorting choice.")
                continue
            for expense in sorted_expenses:
                print(f"Expense ID : {expense['id']}")
                print(f"Name       : {expense['name']}")
                print(f"Amount     : ₹ {expense['amount']}")
                print(f"Category   : {expense['category']}")
                print("-" * 30)
        elif choice == 9:
            sort_choice = input("Enter 1 for lowest to highest or 2 for highest to lowest: ").strip()
            category_totals = reports.calculate_category_total(manager.expenses)
            if not category_totals:
                print("No expenses found.")
                continue
            if sort_choice == "1":
                sorted_categories = reports.sort_category_total(category_totals)
            elif sort_choice == "2":
                sorted_categories = reports.sort_category_total(category_totals,reverse=True)
            else:
                print("Invalid sorting choice.")
                continue
            for category, total in sorted_categories:
                print(f"{category} : ₹ {total}")
        elif choice == 10:
            print(f"Thank you for using {project_name} !!!")
            break
        else:
            print("Invalid Choice. Please enter right choice between(1 to 10) : ")

main()