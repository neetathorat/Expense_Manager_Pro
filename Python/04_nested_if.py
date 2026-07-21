# ##############################################################
# age = int(input("Enter age : "))
# salary = float(input("Enter salary : "))
# year_of_experience = float(input("Enter experience in years : "))

# if age >= 18:
#     if salary >= 30000:
#         if year_of_experience >= 2:
#             print("Selected")
#         else:
#             print("Rejected: Experience Required")
#     else:
#         print("Rejected: Salary Too Low")
# else:
#     print("Rejected: Underage")
        
#######################################################################################            
print("********* Employee Access Verification System ********")

employee_name = input("Enter employee name: ")
age = int(input("Enter age: "))
department = input("Enter department: ")
years_of_experience = int(input("Enter experience: "))

if age >= 18:
    print("Age Verified")

    if department == "IT":
        print("Department Verified")

        if years_of_experience >= 2:
            print("Access Granted")
            print(f"Welcome {employee_name}")
        else:
            print("Access Denied: Experience Required")

    else:
        if department == "AI":
            print("Department Verified")

            if years_of_experience >= 2:
                print("Access Granted")
                print(f"Welcome {employee_name}")
            else:
                print("Access Denied: Experience Required")

        else:
            print("Access Denied: Invalid Department")

else:
    print("Access Denied: Underage")