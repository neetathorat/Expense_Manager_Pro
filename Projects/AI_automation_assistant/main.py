# AI Automation Assistant

assistant_name = "AutoMate AI"
version = "0.6"

print("=" * 15 + " AI AUTOMATION ASSISTANT " + "=" * 15)
print(f"Assistant : {assistant_name}")
print(f"Version   : {version}")

name = input("Enter name : ")
age = int(input("Enter age : "))
height = float(input("Enter height : "))
city = input("Enter city : ")


if age < 18:
    category = "Minor"
else:
    category = "Adult"
    


print("=" * 15 + " USER PROFILE " + "=" * 15)

print(f"Name         : {name}")
print(f"Age          : {age}")
print(f"Age Category : {category}")
print(f"Height       : {height}")
print(f"City         : {city}")


print("=" * 15 + " DATA TYPES " + "=" * 15)

print(f"Name   : {type(name)}")
print(f"Age    : {type(age)}")
print(f"Height : {type(height)}")
print(f"City   : {type(city)}")

print("=" * 15 + " AGE ANALYSIS " + "=" * 15)
print(f"Current Age : {age}")
print(f"After 5 years : {age + 5}")
print(f"5 years ago : {age - 5}")
if age % 2 == 0:
    print("Age Type : Even")
else:
    print("Age Type : Odd")
print(f"Age Square : {age ** 2}")

print("=" * 15 + " ACCESS VERIFICATION " + "=" * 15)

if category == "Adult":
    print("Age Verified")
    department = input("Enter department(IT or AI): ")
    years_of_experience = int(input("Enter experience: "))

    if department in ("IT" , "AI"):
        print("Department Verified")

        if years_of_experience >= 2:
            print("Access Granted")
            print(f"Welcome {name}")
        else:
            print("Access Denied: Experience Required")
    else:
        print("Access Denied: Invalid Department")
else:
    print("Access Denied: Underage")

print("=" * 15 + " USER STATUS " + "=" * 15)
verified = input("Are you verified? (yes/no) : ").lower()
if age >= 18 and verified =='yes':
    print(f"Name  : {name}")
    print(f"Age   : {age}")
    print(f"City  : {city}\n")
    print("Status : Verified User")
elif age < 18:
    print(f"Name  : {name}")
    print(f"Age   : {age}")
    print(f"City  : {city}\n")
    print("Status : Not Verified User")
    print("Reason : Age below 18")
else:
    print(f"Name  : {name}")
    print(f"Age   : {age}")
    print(f"City  : {city}\n")
    print("Status : Not Verified User")
    print("Reason : Verification is pending")

print("=" * 15 + " TASK GENERATOR " + "=" * 15)

task_count = int(input("How many task IDs should AutoMate AI generate?"))
for i in range(1,task_count+1):
    print(f"TASK-{i:03d}")



print("=" * 50)