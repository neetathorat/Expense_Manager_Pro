# Challenge 01
def welcome():
    print("Welcome to AutoMate AI")

welcome()

# Challenge 02
def employee(name, department = "AI"):
    print(f"Name       : {name}")
    print(f"Department : {department}")

employee("Neeta")
employee("Geeta","Computer")

# Challenge 03
def salary(monthly_salary):
    return 12 * monthly_salary

monthly_salary = int(input("Enter Monthly Salary of Employee : "))
annual_salary = salary(monthly_salary)
print(f"Annual Salary : {annual_salary}")

# Challenge 04
def calculate_salary(month_salary, bonus_percent = 10, tax_percent = 5):
    yearly_salary = month_salary * 12
    bonus = (yearly_salary * bonus_percent)/100
    tax = (yearly_salary * tax_percent)/100
    final_salary = yearly_salary + bonus - tax
    return yearly_salary, bonus, final_salary

month_salary = int(input("Enter Monthly Salary : "))
yearly, bonus, final_salary = calculate_salary(month_salary)
print(f"Annual Salary : {yearly}")
print(f"bonus         : {bonus}")
print(f"Final Salary  : {final_salary}")
