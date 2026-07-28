correct_password = "python123"
flag = True
while flag:
    password = input("Enter password : ")
    if correct_password == password:
        print("Login Successful")
        flag = False
    else:
        print("Wrong password")
    