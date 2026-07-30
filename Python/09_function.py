#challenge 1 welcome function
def welcome():
    print("Welcome to Automate AI")

welcome()

#challenge2 employee function
def employee(name):
    print(f"Employee : {name}")
employee("Rahul")

#challenge 3 salary function
def salary(amount):
    print(f"Monthly Salary : {amount}")
salary(45000)

#challenge 4 multiply function with return
def multiply(num1,num2):
    return num1 * num2
result = multiply(8,6)
print(result)

#challenge5 even number checker
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(is_even(8))
print(is_even(5))

#challenge 6 even number checker oneline
def is_even_one_line(number):
    return number % 2 == 0
print(is_even_one_line(3))
print(is_even_one_line(8))