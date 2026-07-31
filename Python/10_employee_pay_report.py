def collect_data():
    name = input("Enter Employee Name : ")
    age = int(input("Enter Age : "))
    city = input("Enter City : ")
    monthly_salary = int(input("Enter monthly salary : "))
    return name, age, city, monthly_salary

def calculate_salary(monthly_salary, bonus_percent = 10, tax_percent = 5):
    yearly_salary = monthly_salary * 12
    bonus = (yearly_salary * bonus_percent)/100
    tax = (yearly_salary * tax_percent)/100
    final_salary = yearly_salary + bonus - tax
    return yearly_salary, bonus, tax, final_salary

def employee_report(*, name, age, city, monthly_salary, department="AI"):
    yearly_salary, bonus, tax, final_salary = calculate_salary(monthly_salary)
    print("=" * 20 + " EMPLOYEE REPORT " + "=" * 20)
    print(f"Name          : {name}")
    print(f"Age           : {age}")
    print(f"City          : {city}")
    print(f"Department    : {department} ")
    print()
    print(f"Annual Salary : {yearly_salary}")
    print(f"Bonus         : {bonus}")
    print(f"Tax           : {tax}")
    print(f"Final Salary  : {final_salary}")
    print("="*50)

def main():
    name, age, city, monthly_salary = collect_data()    
    employee_report(
    name=name,
    age=age,
    city=city,
    monthly_salary=monthly_salary)

main()








