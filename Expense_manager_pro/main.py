def project_heading(project_name,version):
    print("=" * 60)
    print(project_name.center(60))
    print(version.center(60))
    print("=" * 60)

def display_menu():
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Exit")   
    
def add_expense():
    expense_name = input("Enter name of expense : ")
    amount = float(input("Enter amount : "))
    category = input("Enter category : ")
    print("Expense added successfully.")
    print(f"Expense Name : {expense_name}")
    print(f"Amount       : {amount}")
    print(f"Category     : {category}")

def view_expenses():
    print("No expense available.")

def main():
    project_name = "Expense Manager Pro"
    version = "0.2"
    project_heading(project_name,version)
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_expense()
        elif choice == 2:
            view_expenses()
        elif choice == 3:
            print(f"Thank you for using {project_name} !!!")
            break
        else:
            print("Please enter right choice between(1 to 3) :")

main()