# Day 08 - While Loop, Break, Continue

## Topics Covered

* `while` loop
* Infinite loop
* `break`
* `continue`
* Password login system
* ATM PIN verification system
* Loop debugging
* Loop tracing
* Master project integration

---

# 1. while Loop

A `while` loop repeatedly executes a block of code as long as the condition is `True`.

### Syntax

```python
while condition:
    # code
```

### Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

### Output

```
1
2
3
4
5
```

---

# 2. Infinite Loop

An infinite loop never stops because its condition always remains `True`.

### Example

```python
while True:
    print("Running...")
```

The program keeps executing until it is stopped manually or a `break` statement is executed.

---

# 3. break Statement

`break` immediately terminates the nearest loop.

### Syntax

```python
break
```

### Example

```python
while True:
    password = input("Enter Password: ")

    if password == "python123":
        print("Login Successful")
        break
```

When the correct password is entered, the loop ends immediately.

---

# 4. continue Statement

`continue` skips the remaining statements of the current iteration and starts the next iteration.

### Example

```python
for i in range(1, 6):

    if i == 3:
        continue

    print(i)
```

### Output

```
1
2
4
5
```

The value `3` is skipped.

---

# 5. Difference Between break and continue

| break                               | continue                                     |
| ----------------------------------- | -------------------------------------------- |
| Ends the entire loop immediately.   | Skips only the current iteration.            |
| Execution continues after the loop. | Execution continues with the next iteration. |

---

# 6. Common Mistake

### Infinite Loop

```python
x = 1

while x <= 5:

    if x == 3:
        continue

    print(x)
    x += 1
```

Problem:

When `x` becomes `3`, `continue` executes before `x += 1`.

The value of `x` never changes.

Result:

* Prints:

```
1
2
```

* Then enters an infinite loop.

### Correct Version

```python
x = 1

while x <= 5:

    if x == 3:
        x += 1
        continue

    print(x)
    x += 1
```

---

# 7. Login System

Features implemented:

* Password authentication
* Maximum attempts
* Empty password validation
* Successful login using `break`
* Retry using `continue`

Example:

```python
correct_password = "python123"
attempt = 3

while True:
    password = input("Enter Password: ")

    if password == "":
        print("Password cannot be empty.")
        continue

    if password == correct_password:
        print("Login Successful")
        break

    attempt -= 1
    print(f"Remaining attempts: {attempt}")

    if attempt == 0:
        print("Access Denied")
        break
```

---

# 8. ATM PIN Verification Project

Features:

* Correct PIN verification
* Three maximum attempts
* Empty PIN validation
* Account lock after failed attempts
* Uses `while`, `break`, and `continue`

---

# 9. Master Project Integration

Integrated the login system into the **AutoMate AI** project.

Flow:

```
Program Start
      │
      ▼
Project Header
      │
      ▼
Password Login
      │
      ▼
User Profile
      │
      ▼
Age Analysis
      │
      ▼
Access Verification
      │
      ▼
User Status
      │
      ▼
Task Generator
      │
      ▼
Program End
```

---

# 10. Key Points

* Use `while` when the number of iterations is unknown.
* Use `while True` when the program should keep running until a specific condition occurs.
* `break` exits the loop immediately.
* `continue` skips the current iteration.
* Always ensure loop variables are updated to avoid infinite loops.
* Validate user input before processing it.
* Think about edge cases such as empty input and maximum attempts.

---

# Interview Questions

### Q1. What is the difference between `break` and `continue`?

**Answer:**

* `break` terminates the loop immediately.
* `continue` skips the current iteration and starts the next iteration.

---

### Q2. Why is `while True` commonly used in automation?

**Answer:**

Automation programs often do not know in advance how many times they need to run. They continue executing until a specific event or condition occurs, then `break` is used to exit the loop.

---

# Common Mistakes

* Forgetting the `:` after `while`.
* Using `=` instead of `==` in conditions.
* Forgetting to update loop variables.
* Creating accidental infinite loops.
* Misusing `continue`.
* Not handling empty user input.

---

# Day 08 Summary

Today I learned:

* `while` loop
* Infinite loops
* `break`
* `continue`
* Loop tracing
* Loop debugging
* Login system
* ATM PIN verification
* Master project integration
* Writing safer and more reliable loops
