def display_header():
    print("="*30)
    print("Employee Salary Calculator")
    print("="*30)

def annual_salary(m_salary):
    return m_salary * 12

def bonus(salary):
    return (salary * 10)/100

def calculate(annual,bonus):
    return annual + bonus

def display_report(employee_name, monthly_salary,a_salary,bonus1,total):
    print("Employee Salary Report")
    print("-"*28)
    print(f"Employee Name   : {employee_name}\n")
    print(f"Monthly Salary  : {monthly_salary}")
    print(f"Annual Salary   : {a_salary}")
    print(f"Bonus           : {bonus1}")
    print(f"Total Salary    : {total}")

display_header()
employee_name = input("Enter Employee Name : ")
monthly_salary = int(input("Enter monthly salary of employee : "))
a_salary = annual_salary(monthly_salary)
bonus1 = bonus(a_salary)
total = calculate(a_salary,bonus1)
display_report(employee_name, monthly_salary,a_salary,bonus1,total)
