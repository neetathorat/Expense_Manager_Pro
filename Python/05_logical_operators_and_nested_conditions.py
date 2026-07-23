# 01
age = int(input("Enter your age :"))
if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible")

# 02
user_name = input("Enter User Name :")
password = input("Enter Password : ")
if user_name == "admin" and password == "python123":
    print("Login Successful")
else:
    print("Invalid Credential")

#02 as per my knowledge from day01 to today
user_name = input("Enter User Name :")
password = input("Enter Password : ")
if user_name == "admin" and password == "python123":
    print("Login Successful")
elif user_name == "admin" and password != "python123":
    print("Invalid password")
elif user_name != "admin" and password == "python123":
    print("Invalid User Name")
else:
    print("Invalid Credentials")

# 03
number = int(input("Enter a number : "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# 04
age = int(input("Enter your age : "))
aadhaar = input("Enter you have Adhaar or not(yes/no) : ")

if age >= 18 and aadhaar.lower() == "yes":
    print("Eligible for government scheme")
else:
    print("Not Eligible")

# 05
atm_pin = int(input("Enter your atm pin :"))
if atm_pin == 1234:
    balance = float(input("Enter balance :"))
    if balance >= 500:
        print("Transaction Allowed")
    else:
        print("Insufficient balance")
else:
    print("Invalid pin")

# 06
age = int(input("Enter age : "))
experience = int(input("Enter experience in year : "))
degree = input("you completed your degree or not(yes/no)")
if age >= 21 and experience >= 2 and degree.lower() == "yes":
    print("Selected")
else:
    print("Rejected")
