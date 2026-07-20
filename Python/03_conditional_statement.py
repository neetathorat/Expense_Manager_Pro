print("########### IF Condition ##############")
age = int(input("Enter age : "))
if age >= 18:
    print("Adult")

############################################################################

print("########### IF-ELSE Condition ##############")
age = int(input("Enter age : "))
if age >= 18:
    print("Adult")
else:
    print("Minor")

############################################################################

print("########### IF-ELIF-ELSE Condition ##############")
age = int(input("Enter age : "))
if 0 <= age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior Citizen")