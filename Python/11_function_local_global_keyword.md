# Day 11 – Advanced Functions

## 🎯 Objective

Learn how to write clean, reusable, and modular code using advanced function concepts.

---

# Topics Covered

- Local Variables
- Global Variables
- Variable Scope
- Variable Shadowing
- `global` Keyword
- Function Parameters
- Positional Arguments
- Keyword Arguments
- Default Parameters
- `return` vs `print`
- Function Design Principles
- Clean Coding Practices

---

# 1. Local Variable

A local variable is declared inside a function.

- Exists only while the function is executing.
- Cannot be accessed outside the function.

### Syntax

```python
def greet():
    name = "Neeta"
    print(name)
```

### Example

```python
def greet():
    name = "Neeta"
    print(name)

greet()
```

### Output

```
Neeta
```

Trying to access `name` outside the function:

```python
print(name)
```

Output:

```
NameError
```

---

# 2. Global Variable

A global variable is created outside all functions.

It can be accessed inside any function unless a local variable with the same name exists.

### Example

```python
company = "OpenAI"

def show():
    print(company)

show()
```

### Output

```
OpenAI
```

---

# 3. Variable Shadowing

When a local variable has the same name as a global variable, the local variable takes priority inside the function.

### Example

```python
company = "TCS"

def show():
    company = "Infosys"
    print(company)

show()
print(company)
```

### Output

```
Infosys
TCS
```

---

# 4. Variable Lookup Order (LEGB)

Python searches variables in the following order:

```
Local
↓

Global
↓

Built-in
```

Always remember:

**Local variables have higher priority than global variables.**

---

# 5. global Keyword

The `global` keyword allows a function to modify a global variable.

### Example

```python
count = 0

def increase():
    global count
    count += 1

increase()
print(count)
```

### Output

```
1
```

> **Best Practice:** Avoid using global variables unless absolutely necessary. Prefer passing values as parameters and returning results.

---

# 6. Function Parameters

Parameters receive values when a function is called.

### Example

```python
def employee(name, age):
    print(name)
    print(age)
```

---

# 7. Positional Arguments

Arguments are matched based on their position.

### Example

```python
employee("Neeta", 21)
```

Mapping:

```
name → "Neeta"
age  → 21
```

> Order matters.

---

# 8. Keyword Arguments

Arguments are passed using parameter names.

### Example

```python
employee(age=21, name="Neeta")
```

Output is the same.

> Order does not matter.

---

# 9. Default Parameters

A parameter can have a default value.

If no value is passed, Python uses the default.

### Example

```python
def display_header(
    assistant_name="AutoMate AI",
    version="1.1"
):
    print(assistant_name)
    print(version)
```

Calling:

```python
display_header()
```

or

```python
display_header(version="1.2")
```

---

# 10. return vs print

## Using print()

```python
def square(num):
    print(num ** 2)

result = square(5)

print(result)
```

Output

```
25
None
```

Reason:

`print()` only displays the value.

It does **not** return it.

---

## Using return

```python
def square(num):
    return num ** 2

result = square(5)

print(result)
```

Output

```
25
```

`return` sends the value back to the caller.

---

# 11. Function Design Principles

A good function should:

- Perform only one responsibility.
- Receive data through parameters.
- Return results when needed.
- Avoid unnecessary global variables.
- Have meaningful names.

Good Example:

```python
def calculate_bonus():
```

Avoid:

```python
def calculate_bonus_and_print_report():
```

**One Function = One Responsibility**

---

# 12. Clean Coding Practices

## ✅ Use meaningful function names

Good:

```python
add()
calculate_price()
display_receipt()
determine_age_category()
```

Avoid:

```python
abc()
test()
employee1()
```

---

## ✅ Use meaningful variable names

Good:

```python
final_price
discount
category
original_price
```

Avoid:

```python
a
b
x
temp
```

---

## ✅ Return values instead of printing

Good:

```python
return final_price
```

Avoid:

```python
print(final_price)
```

if another function needs that value.

---

## ✅ Avoid duplicate calculations

Good:

```python
final_price = original_price - discount
```

Avoid:

```python
final_price = quantity * standard_price - discount
```

when `original_price` is already available.

---

# 13. Common Mistakes

❌ Accessing local variables outside the function.

❌ Using global variables unnecessarily.

❌ Forgetting to return values.

❌ Using `print()` instead of `return`.

❌ Giving variables the same name as functions.

Bad:

```python
addition = addition(num1, num2)
```

Better:

```python
addition_result = add(num1, num2)
```

---

# 14. Coding Challenges

Practiced:

- Local vs Global Variables
- Calculator using Functions
- Positional & Keyword Arguments
- Default Parameters
- Return vs Print

---

# 15. Mini Project

## Movie Ticket Booking System

Concepts applied:

- Function Design
- Parameters
- Return Values
- Default Parameters
- Local Variables
- Keyword Arguments
- Single Responsibility Principle

---

# 16. Master Project Integration

Project: **AI Automation Assistant**

Improvements made:

- Refactored into reusable functions.
- Added default parameters to `display_header()`.
- Renamed `get_age_category()` to `determine_age_category()`.
- Removed unnecessary advanced syntax.
- Improved program structure using `main()`.

---

# Key Takeaways

- Local variables exist only inside their function.
- Global variables should be avoided unless necessary.
- Pass information using parameters.
- Return results instead of printing whenever possible.
- Keyword arguments improve readability.
- Default parameters reduce repeated code.
- Keep every function focused on one responsibility.
- Think about program structure, not just syntax.

---

# Day 11 Summary

✅ Learned Advanced Functions

✅ Understood Variable Scope

✅ Practiced Parameters and Return Values

✅ Learned Default & Keyword Arguments

✅ Built Multiple Coding Challenges

✅ Completed Movie Ticket Booking System Mini Project

✅ Refactored AI Automation Assistant using clean function design