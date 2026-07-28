# Day 07 - While Loop

## 📚 Topics Covered

- Introduction to `while` loop
- Difference between `for` loop and `while` loop
- Structure of a `while` loop
- Memory model of a `while` loop
- Infinite loops
- User-controlled repetition
- Multiplication table using `while`
- Login authentication using `while`
- Integrating `while` loop into the Master Project

---

# 1. What is a While Loop?

A `while` loop executes a block of code repeatedly **as long as a condition is True**.

Syntax:

```python
while condition:
    # code
```

Example:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```
1
2
3
4
5
```

---

# 2. Three Parts of a While Loop

## Initialization

Create the starting value.

```python
count = 1
```

---

## Condition

Python checks this before every iteration.

```python
while count <= 5:
```

---

## Update

Change the variable so the condition eventually becomes False.

```python
count += 1
```

---

# 3. Execution Flow

```
Initialize variable
        ↓
Check condition
        ↓
Condition True?
     /        \
   Yes         No
    ↓           ↓
Execute Code   Stop Loop
    ↓
Update Variable
    ↓
Back to Condition
```

---

# 4. Difference Between for and while

| for Loop | while Loop |
|----------|------------|
| Used when number of iterations is known | Used when iterations depend on a condition |
| Loop variable is managed automatically | Programmer manages initialization and update |
| Less chance of infinite loop | More chances of infinite loop if update is missing |
| Best for sequences and ranges | Best for user-controlled or condition-based repetition |

---

# 5. Infinite Loop

Example:

```python
count = 1

while count <= 5:
    print(count)
```

Problem:

- Variable never changes.
- Condition always remains True.

Output:

```
1
1
1
1
1
...
```

Fix:

```python
count += 1
```

---

# 6. Printing Numbers

Ascending:

```python
number = 1

while number <= 10:
    print(number)
    number += 1
```

Descending:

```python
number = 10

while number >= 1:
    print(number)
    number -= 1
```

---

# 7. Even Numbers

```python
number = 2

while number <= 20:
    print(number)
    number += 2
```

Output:

```
2
4
6
8
10
12
14
16
18
20
```

---

# 8. Multiplication Table

```python
number = int(input("Enter a number: "))

i = 1

while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1
```

---

# 9. Login Authentication

```python
correct_password = "python123"

flag = True

while flag:
    password = input("Enter password: ")

    if password == correct_password:
        print("Login Successful!")
        flag = False
    else:
        print("Wrong Password! Try Again.")
```

---

# 10. Common Mistakes

❌ Forgetting initialization

```python
while count <= 5:
```

---

❌ Forgetting update

```python
count += 1
```

Missing update causes an infinite loop.

---

❌ Wrong update direction

```python
count = 5

while count >= 1:
    count += 1
```

The loop never ends because the variable moves away from the stopping condition.

---

# 11. Important Interview Points

- `for` loop is used when iterations are known.
- `while` loop is used when iterations depend on a condition.
- A `while` loop requires:
  - Initialization
  - Condition
  - Update
- Missing update can cause an infinite loop.

---

# 12. Mini Project

Login Authentication System

Features:

- Ask for password.
- Keep asking until correct password is entered.
- Display success message after successful login.

---

# 13. Master Project Update (Version 0.7)

Added Login Authentication before accessing AutoMate AI.

Flow:

```
Start
   ↓
Login Authentication
   ↓
User Profile
   ↓
Age Analysis
   ↓
Access Verification
   ↓
User Status
   ↓
Task Generator
```

---

# 14. Key Takeaways

- `while` loops are condition-driven.
- Always remember:
  - Initialize
  - Check Condition
  - Update
- Think about whether the update moves the variable toward the stopping condition.
- Trace variable values mentally before executing the program.
- Write the simplest solution that satisfies the requirements.

---

# Day 07 Summary

✅ While Loop

✅ Memory Model

✅ Output Prediction

✅ Debugging

✅ Coding Challenges

✅ Interview Questions

✅ Login Authentication Project

✅ Master Project Integration (Version 0.7)