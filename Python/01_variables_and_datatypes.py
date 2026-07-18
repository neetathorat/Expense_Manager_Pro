# 01 Variables and Data Types

# Variables

name = "Neeta"
age = 25
height = 5.8
is_student = True


print("=" * 10 + " VARIABLES " + "=" * 10)

print(f"Name : {name}")
print(f"Age : {age}")
print(f"Height : {height}")
print(f"Student : {is_student}")


# Data Types

print("=" * 10 + " DATA TYPES " + "=" * 10)

print(f"Type of name : {type(name)}")
print(f"Type of age : {type(age)}")
print(f"Type of height : {type(height)}")
print(f"Type of student : {type(is_student)}")


# User Input

print("=" * 10 + " USER INPUT " + "=" * 10)

user_name = input("Enter your name : ")
user_age = int(input("Enter your age : "))
user_height = float(input("Enter your height : "))


print("=" * 10 + " USER PROFILE " + "=" * 10)

print(f"Name : {user_name}")
print(f"Age : {user_age}")
print(f"Height : {user_height}")


# Type Checking

print("=" * 10 + " INPUT DATA TYPES " + "=" * 10)

print(type(user_name))
print(type(user_age))
print(type(user_height))


# f-string Practice

print("=" * 10 + " F STRING " + "=" * 10)

print(f"{user_name} is {user_age} years old and height is {user_height}")