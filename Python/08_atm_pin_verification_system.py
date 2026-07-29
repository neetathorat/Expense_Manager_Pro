correct_pin = "2580"
attempt = 3
while True:
    pin = input("Enter ATM Pin : ")
    if pin == correct_pin:
        print("Access Granted")
        break
    elif pin == "":
        print("PIN cannot be empty")
        continue
    else:
        print("Incorrect Pin")
        attempt -= 1
        if attempt == 0:
            print("Account Locked")
            break
        print(f"Remaining attempt is {attempt} ")