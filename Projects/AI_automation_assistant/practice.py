def login():
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

def display_header():
    print(f"Welcome to {assistant_name}")
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

def age_analysis(age):
    if age < 18:
        return "Minor"
    else:
        return "Adult"         

print("=" * 15 + " AI AUTOMATION ASSISTANT " + "=" * 15)
assistant_name = "AutoMate AI"
version = "0.7"
correct_password = "python123"
if login():

    display_header()

    name, age, height, city, department, years_of_experience = collect_user_data()

    category = age_analysis(age)

    show_profile(name, age, category, height, city)

