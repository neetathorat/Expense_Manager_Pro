def login(correct_password):
    attempt = 3
    while True:
        password = input("Enter password : ")
        if password == correct_password:
            print("Login Successful!")
            return True
        elif not password:
            print("EMPTY Password not allowed")
            continue
        else:
            attempt -= 1
            print("Wrong password! Try Again")
            print(f"Remaining attempts {attempt}")
            if attempt == 0:
                print("Too many failed attempts")
                print("Access Denied")
                return False

def display_header(assistant_name = "AutoMate AI", version = "1.1"):
    print(f"Welcome")
    print(f"Assistant : {assistant_name}")
    print(f"Version   : {version}")

def collect_user_data():
    name = input("Enter name : ")
    age = int(input("Enter age : "))
    height = float(input("Enter height : "))
    city = input("Enter city : ")
    department = input("Enter department : ")
    years_of_experience = int(input("Enter years of experience : "))
    return name, age, height, city, department, years_of_experience

def show_profile(name, age, category, height,city,department, years_of_experience):
    print("=" * 15 + " USER PROFILE " + "=" * 15)
    print(f"Name         : {name}")
    print(f"Age          : {age}")
    print(f"Age Category : {category}")
    print(f"Height       : {height}")
    print(f"City         : {city}")
    print(f"Department   : {department}")
    print(f"Experience   : {years_of_experience}")

def determine_age_category(age):
    if age < 18:
        return "Minor"
    else:
        return "Adult"  
    
def add_task(tasks):
    task = input("Add new task :")
    if task in tasks:
        print(" task is already present")
    else:
        tasks.append(task)
        print("New task added successfully")

def view_tasks(tasks):
    for task in tasks:
        print(task)

def remove_task(tasks):
    task = input("Enter task name to remove : ")
    if task in tasks:
        tasks.remove(task)
        print("Task is removed successfully")
    else:
        print("Task is not present")

def search_task(tasks):
    task = input("Enter task name to search : ")
    if task in tasks:
        print("task is found")
    else:
        print("task is not found")
    

def menu():
    print("=" * 5 + " AI Automation Assistant " + "=" * 5)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Search Task")
    print("5. Exit")

def main():      
    print("=" * 15 + " AI AUTOMATION ASSISTANT " + "=" * 15)
    correct_password = "python123"
    tasks = ["Learn Python","Build Portfolio","Complete Project"]
    if login(correct_password):

        display_header()

        name, age, height, city, department, years_of_experience = collect_user_data()

        category = determine_age_category(age)

        show_profile(
        name=name,
        age=age,
        category=category,
        height=height,
        city=city,
        department=department,
        years_of_experience=years_of_experience)
        while True:
            menu()
            choice = int(input("Enter your choice :"))
            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                view_tasks(tasks)
            elif choice == 3:
                remove_task(tasks)
            elif choice == 4:
                search_task(tasks)
            elif choice == 5:
                print("Thank you for using")
                break
            else:
                print("Enter choice between (1 to 5) : ")

main()