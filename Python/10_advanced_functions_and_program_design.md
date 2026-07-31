# Day 10 - Advanced Functions & Program Design

## Topics Covered

- Function Scope
- Local Variables
- Global Variables
- Parameters vs Arguments
- Default Arguments
- Keyword Arguments
- Keyword-only Arguments (*)
- Returning Multiple Values
- Program Design
- Function Responsibilities
- main() Function

---

# 1. Variable Scope

Variable scope defines where a variable can be accessed.

## Local Variable

A local variable is created inside a function and exists only within that function.

Example:

```python
def greet():
    message = "Hello"
    print(message)

greet()
```

Output:

```
Hello
```

Trying to access `message` outside the function results in an error.

---

## Global Variable

A global variable is declared outside all functions.

Example:

```python
company = "AutoMate AI"

def show_company():
    print(company)

show_company()
```

Output:

```
AutoMate AI
```

---

# 2. Local vs Global Variables

| Local Variable | Global Variable |
|----------------|-----------------|
| Created inside a function | Created outside functions |
| Accessible only inside that function | Accessible throughout the program |
| Destroyed after function execution | Exists until the program ends |

---

# 3. Parameters vs Arguments

## Parameter

A variable defined in the function definition.

```python
def greet(name):
    print(name)
```

`name` is a parameter.

---

## Argument

The value passed while calling the function.

```python
greet("Neeta")
```

`"Neeta"` is an argument.

---

# 4. Default Arguments

A default argument provides a value if no argument is supplied.

Example:

```python
def employee(name, department="AI"):
    print(name)
    print(department)

employee("Neeta")
employee("Rahul", "Python")
```

Output:

```
Neeta
AI

Rahul
Python
```

---

## Rule

Default parameters must always come after non-default parameters.

Correct:

```python
def show(state, city="Pune"):
    pass
```

Wrong:

```python
def show(city="Pune", state):
    pass
```

Error:

```
SyntaxError:
non-default argument follows default argument
```

---

# 5. Keyword Arguments

Arguments can be passed using parameter names.

Example:

```python
def employee(name, age):
    print(name, age)

employee(age=20, name="Neeta")
```

Keyword arguments improve readability.

---

# 6. Keyword-only Arguments

Using `*` forces all following parameters to be passed using keywords.

Example:

```python
def profile(*, name, age):
    print(name)
    print(age)

profile(name="Neeta", age=20)
```

Wrong:

```python
profile("Neeta", 20)
```

Error:

```
TypeError
```

---

# 7. Returning Multiple Values

A function can return more than one value.

Example:

```python
def calculate_salary(monthly_salary):
    yearly = monthly_salary * 12
    bonus = yearly * 0.10

    return yearly, bonus

annual, bonus = calculate_salary(50000)
```

---

# 8. Function Responsibilities

Each function should perform only one task.

Good Example:

```
login()
```

→ Only authenticates user.

```
collect_user_data()
```

→ Only collects user input.

```
calculate_salary()
```

→ Only performs calculations.

```
show_profile()
```

→ Only displays information.

---

# 9. main() Function

The `main()` function controls the overall program flow.

Example:

```python
def main():
    display_header()

    if login():
        data = collect_user_data()
        show_profile()

main()
```

Benefits:

- Easy to read
- Better organization
- Easier debugging
- Professional program structure

---

# 10. Common Errors

## 1. UnboundLocalError

```python
company = "ABC"

def update():
    company = company + " Pvt Ltd"
```

Reason:

Python treats `company` as a local variable because of assignment.

---

## 2. SyntaxError

```python
def login(username="Admin", password):
```

Reason:

Default parameter before non-default parameter.

---

## 3. IndentationError

```python
def hello():
print("Hello")
```

Reason:

Python expects an indented block after a function definition.

---

## 4. NameError

```python
employee_report(
    department=department
)
```

If `department` was never created:

```
NameError:
name 'department' is not defined
```

---

## 5. Unexpected Keyword Argument

```python
def employee(name):
    pass

employee(name="Neeta", company="ABC")
```

Error:

```
TypeError:
got an unexpected keyword argument
```

---

# 11. Design Principles Learned

- One function → One responsibility.
- Use `return` instead of printing calculated values.
- Keep calculations separate from display logic.
- Validate user input where it is collected.
- Use meaningful function names.
- Pass data using parameters instead of relying on global variables.
- Use `main()` to coordinate program execution.

---

# Mini Project

Food Ordering System

Functions:

- display_menu()
- take_order()
- calculate_bill()
- generate_receipt()
- main()

Concepts used:

- Functions
- Conditions
- Loops
- Return values
- Default arguments
- Program flow
- Input validation

---

# Master Project Integration

Refactored AI Automation Assistant:

- Added `main()` function.
- Converted `show_profile()` to keyword-only arguments.
- Renamed `age_analysis()` to `get_age_category()`.
- Passed configuration values as parameters instead of relying on globals.
- Improved function responsibilities.

---

# Key Takeaways

- Functions should have a single responsibility.
- Use `return` to make functions reusable.
- Prefer passing data through parameters instead of using global variables.
- `main()` should coordinate the program, not perform all the work.
- Default arguments reduce repeated code.
- Keyword arguments improve readability.
- Keyword-only arguments prevent incorrect function calls.
- Good program design is as important as writing correct syntax.