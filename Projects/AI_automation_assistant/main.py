# AI Automation Assistant

assistant_name = "AutoMate AI"
version = "0.1"

print("=" * 15 + " AI AUTOMATION ASSISTANT " + "=" * 15)
print(f"Assistant : {assistant_name}")
print(f"Version   : {version}")

name = input("Enter name : ")
age = int(input("Enter age : "))
height = float(input("Enter height : "))
city = input("Enter city : ")

print("=" * 15 + " USER PROFILE " + "=" * 15)

print(f"Name   : {name}")
print(f"Age    : {age}")
print(f"Height : {height}")
print(f"City   : {city}")


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

print("=" * 50)