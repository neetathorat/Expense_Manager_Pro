# Day 09 - Functions (def, Parameters, Arguments, Return)

## Objective

Learn how to organize code using functions to make programs reusable, readable, and easier to maintain.

---

# What is a Function?

A function is a reusable block of code that performs a specific task.

Instead of writing the same code multiple times, write it once inside a function and call it whenever needed.

Example:

```python
def welcome():
    print("Welcome to AutoMate AI")

welcome()
```

---

# Function Syntax

```python
def function_name():
    # Code
```

Example:

```python
def greet():
    print("Hello")
```

Call the function:

```python
greet()
```

---

# Functions with Parameters

Parameters allow us to send data into a function.

Example:

```python
def greet(name):
    print(f"Hello {name}")

greet("Neeta")
```

Output:

```
Hello Neeta
```

---

# Multiple Parameters

```python
def profile(name, age):
    print(name)
    print(age)

profile("Neeta", 20)
```

---

# Return Statement

The `return` keyword sends a value back to the caller.

Example:

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

Output:

```
30
```

---

# Difference Between print() and return

## print()

* Displays output on the screen.
* Used to show information to the user.
* Does not send data back to the caller.

Example:

```python
print(10 + 20)
```

Output:

```
30
```

---

## return

* Sends a value back to the caller.
* Can be stored in a variable.
* Can be reused later in the program.

Example:

```python
def square(num):
    return num * num

answer = square(5)

print(answer)
```

Output:

```
25
```

---

# Function Execution

A function does **not** execute when Python reads its definition.

It executes **only when it is called**.

Example:

```python
def demo():
    print("A")

print("B")
demo()
print("C")
```

Output:

```
B
A
C
```

---

# Variable Scope

Variables created inside a function exist only inside that function.

Example:

```python
def data():
    name = "Neeta"

data()

print(name)
```

Output:

```
NameError
```

To use data outside the function, return it.

Example:

```python
def data():
    name = "Neeta"
    return name

name = data()

print(name)
```

---

# Returning Multiple Values

Python allows returning multiple values.

Example:

```python
def user():
    return "Neeta", 20

name, age = user()

print(name)
print(age)
```

---

# Functions Used in AutoMate AI

Today the project was refactored into functions.

Functions created:

```python
login()

display_header()

collect_user_data()

age_analysis()

show_profile()
```

Benefits:

* Cleaner code
* Easier debugging
* Reusable functions
* Better program organization
* Easier to add new features

---

# Important Rules

✔ A function must be defined before it is called.

✔ A function executes only when called.

✔ Parameters receive values.

✔ Arguments are the actual values passed to a function.

✔ Use `return` when another part of the program needs the result.

✔ Use `print()` only to display information.

✔ Keep each function focused on one responsibility.

---

# Common Mistakes

❌ Forgetting `()` when calling a function.

❌ Missing `:` after the function definition.

❌ Incorrect indentation.

❌ Confusing `print()` with `return`.

❌ Using variables outside their scope.

❌ Forgetting to capture returned values.

---

# Real-World Uses of Functions

* Login systems
* Calculator applications
* Banking software
* AI chatbots
* Automation scripts
* APIs
* Data processing
* Web applications

---

# Day 09 Summary

Today I learned:

* Creating functions using `def`
* Calling functions
* Parameters and arguments
* Returning values with `return`
* Difference between `print()` and `return`
* Variable scope
* Returning multiple values
* Refactoring a large program into reusable functions
* Organizing code using single-responsibility functions

---

# Key Takeaway

> "A good programmer doesn't write more code—they write reusable code."

Functions make programs cleaner, reusable, easier to debug, and easier to maintain. They are one of the most important building blocks of Python and are essential for automation and AI development.
