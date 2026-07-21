# Day 04 - Nested `if` Statements

## What is a Nested `if`?

A nested `if` is an `if` statement inside another `if` statement.

The inner `if` is executed only when the outer `if` condition is `True`.

---

# Syntax

```python
if condition1:
    # Outer if

    if condition2:
        # Inner if
```

---

# Flow

```
Outer Condition
       |
   True / False
      |
      V
Inner Condition
      |
  True / False
```

The inner `if` is checked only if the outer condition is `True`.

---

# Example

```python
age = 20
has_license = True

if age >= 18:
    if has_license:
        print("Drive Allowed")
```

Output

```
Drive Allowed
```

---

# Nested `if` with `else`

```python
age = 20
has_license = False

if age >= 18:
    if has_license:
        print("Drive Allowed")
    else:
        print("Apply for License")
else:
    print("Underage")
```

Possible outputs

* Drive Allowed
* Apply for License
* Underage

Only one execution path is followed.

---

# Execution Rule

Python always checks the outer condition first.

If the outer condition is `False`, the inner `if` is never executed.

---

# Nested `if` vs `and`

Nested `if`

```python
if age >= 18:
    if has_license:
        print("Drive")
```

Using `and`

```python
if age >= 18 and has_license:
    print("Drive")
```

### Difference

Use nested `if` when:

* Different actions are required after each condition.
* Each condition has its own message or processing.

Use `and` when:

* All conditions must be `True` for one action.

---

# Common Mistakes

### 1. Wrong indentation

```python
if age >= 18:
if has_license:
    print("Drive")
```

Incorrect.

---

### 2. Missing colon

```python
if age >= 18
```

Incorrect.

Correct

```python
if age >= 18:
```

---

### 3. Comparing wrong data types

```python
experience = input("Enter experience: ")

if experience >= 2:
```

This raises a `TypeError` because `input()` returns a string.

Correct

```python
experience = int(input("Enter experience: "))
```

---

### 4. Asking unnecessary input

Bad design

```text
Ask Age
Ask Department
Ask Experience
Reject Underage
```

Better design

```text
Ask Age

↓

If Adult

↓

Ask Department

↓

Ask Experience
```

Collect information only when it is actually needed.

---

# Interview Questions

### What is a nested `if`?

A nested `if` statement is an `if` statement inside another `if` statement. The inner `if` executes only when the outer `if` condition is `True`.

---

### Can every nested `if` be replaced with `and`?

No.

Nested `if` allows different actions after each condition, while `and` is suitable only when all conditions must be `True` for a single action.

---

### Why use nested `if` instead of multiple `and` operators?

* Different actions after each condition.
* Better readability for complex logic.
* More specific feedback when a condition fails.

---

# Mini Project

Employee Access Verification System

Inputs

* Employee Name
* Age
* Department
* Years of Experience

Conditions

1. Verify age.
2. Verify department.
3. Verify experience.
4. Grant or deny access.

---

# Master Project Update

Project: AI_Automation_Assistant

Added:

* Access Verification section.
* Department validation.
* Experience validation.
* Welcome message after successful verification.
* Better user flow by asking department and experience only after verifying age.

---

# Best Practices Learned

* Use meaningful variable names.
* Keep one responsibility per section.
* Reuse existing variables when appropriate.
* Convert user input to the correct data type.
* Follow indentation carefully.
* Keep program flow logical.
* Avoid asking for unnecessary input.
* Separate display logic from decision-making logic whenever possible.

---

# Key Takeaways

* Nested `if` creates multi-level decision making.
* Indentation defines code blocks.
* The outer `if` controls entry to the inner `if`.
* Program design is as important as correct syntax.
* Readability and user experience matter in addition to working code.
