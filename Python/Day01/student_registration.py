# Expected output
# ========== STUDENT REGISTRATION ==========
# Enter Student ID      : 101
# Enter Student Name    : Rahul Sharma
# Enter Age             : 15
# Enter Gender          : Male
# Enter Standard        : 10
# Enter Division        : A
# Enter School Name     : ABC School
# Enter Mobile Number   : 9876543210
# Enter City            : Ahmedabad

# ========== REGISTRATION DETAILS ==========
# Student ID      : 101
# Student Name    : Rahul Sharma
# Age             : 15
# Gender          : Male
# Standard        : 10
# Division        : A
# School Name     : ABC School
# Mobile Number   : 9876543210
# City            : Ahmedabad
# ==========================================
print("="*45)
print("STUDENT REGISTRATION")
print("="*45)
student_id = int(input("Enter Student ID    : "))
student_name = input("Enter Student Name  : ")
student_age = int(input("Enter Age           : "))
student_gender = input("Enter Gender        : ")
student_standard = input("Enter Standard      : ")
student_division = input("Enter Division      : ")
school_name = input("Enter School Name   : ")
mobile_number = input("Enter Mobile number : ")
city = input("Enter City          : ")
print("="*45)
print("REGISTRATION DETAILS")
print("="*45)
print(f"Student Id    : {student_id}")
print(f"Student Name  : {student_name}")
print(f"Age           : {student_age}")
print(f"Gender        : {student_gender}")
print(f"Standard      : {student_standard}")
print(f"Division      : {student_division}")
print(f"School Name   : {school_name}")
print(f"Mobile Number : {mobile_number}")
print(f"City          : {city}")
print("="*45)
