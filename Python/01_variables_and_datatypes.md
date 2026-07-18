# 01 Variables and Data Types

## Objective

Learn how Python stores data using variables and understand the basic built-in data types.

---

# What is a Variable?

A variable is a name that refers to a value stored in memory.

Syntax:

variable_name = value

Example:

name = "Neeta"
age = 25
height = 5.8

---

# Variable Naming Rules

## Allowed

- Letters (a-z, A-Z)
- Numbers (0-9) but not at the beginning
- Underscore (_)

Examples:

user_name
age1
total_marks

## Not Allowed

1name
user-name
class

---

# Naming Convention

Python follows snake_case naming style.

Good examples:

first_name
student_age
total_marks

Avoid:

FirstName
studentAge

---

# Python Data Types

## int

Stores integer values.

Example:

age = 25


## float

Stores decimal values.

Example:

height = 5.8


## str

Stores text values.

Example:

name = "Python"


## bool

Stores True or False values.

Example:

is_active = True

---

# Input Function

The input() function takes data from the user.

Example:

name = input("Enter name: ")

Important:

input() always returns a string (str).

---

# Type Conversion

Convert data types when required.

Examples:

age = int(input("Enter age: "))

height = float(input("Enter height: "))


Common conversion functions:

int()
float()
str()
bool()

---

# Checking Data Type

Use the type() function.

Example:

age = 25

print(type(age))


Output:

<class 'int'>

---

# f-Strings

f-strings are used for clean string formatting.

Example:

name = "Neeta"

print(f"Hello {name}")


Advantages:

- Easy to read
- Cleaner syntax
- Recommended Python style

---

# Comments

Comments explain code.

Single line comment:

# This is a comment


Use comments to explain why something is done.

---

# Common Beginner Mistakes

- Forgetting that input() returns a string
- Not converting numeric input
- Using invalid variable names
- Confusing = with ==
- Using unclear variable names

---

# Interview Points

Q: What is a variable?

A: A variable is a name that references a value stored in memory.


Q: Does Python require variable declaration?

A: No. Variables are created automatically when values are assigned.


Q: What does input() return?

A: It returns a string (str).


Q: How do you check data type?

A: Using the type() function.


Q: What naming convention is used in Python?

A: snake_case.

---

# Revision Summary

- Variables store values.
- Python is dynamically typed.
- Basic data types:
  - int
  - float
  - str
  - bool

- input() returns string data.
- Use type conversion when needed.
- Use type() to inspect data types.
- Prefer f-strings for formatting.