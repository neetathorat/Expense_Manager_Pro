# Challenge 1 — Local vs Global Variable
def display_local():
    company_name = "INFOSYS"
    print(company_name)

def display_global():
    print(company_name)

company_name = "TCS"
display_local()
display_global()
print(company_name)

#Challenge 2 — Build Your Own Calculator Functions
def add(num1, num2):
    return num1 + num2    

def sub(num1, num2):
    return num1 - num2    

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1/num2

num1 = 15
num2 = 3
addition = add(num1, num2)
subtraction = sub(num1, num2)
multiplication = mult(num1, num2)
division = div(num1, num2)
print(f"Addition : {addition}")
print(f"Subtraction : {subtraction}")
print(f"Multiplication : {multiplication}")
print(f"Division : {division}")

# Challenge 3 — Employee Information
def employee(name, age, city, department):
    print(f"Name : {name}")
    print(f"Age : {age}")
    print(f"City : {city}")
    print(f"Department : {department}")

employee("Neeta", 21, "Pune", "Computer") # positional argument
employee(city="Pune", name="Neeta", department="Computer", age=21) # keyword argument

# Challenge 4 — Default Parameter Challenge
def employee_default(name, city = "Pune", department = "Computer"):
    print(f"Name : {name}")
    print(f"City : {city}")
    print(f"Department : {department}")

employee_default("Neeta")
employee_default("Geeta", "Mumbai")
employee_default("Seeta", "Pimpari", "IT")

# Challenge 5 — Return vs Print
def square(num):
    return num ** 2
    
def psquare(num):
    print(num ** 2)

square1 = square(5)
square2 = psquare(5)

print(square1)
print(square2) # function not return any value to store 
