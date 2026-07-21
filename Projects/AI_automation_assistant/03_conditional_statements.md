# Day 03 - Conditional Statements

## Objective

Learn how Python makes decisions using conditional statements.

---

# Why Conditional Statements?

Conditional statements allow a program to make decisions based on conditions.

Example:

```python
age = 20

if age >= 18:
    print("Adult")
```

Output:

```
Adult
```

---

# Syntax of if

```python
if condition:
    statement
```

Example:

```python
age = 18

if age >= 18:
    print("Adult")
```

---

# Flow of if

1. Python checks the condition.
2. If condition is True:
   - Execute the if block.
3. If condition is False:
   - Skip the if block.
4. Continue with the remaining program.

Example:

```python
age = 15

if age >= 18:
    print("Adult")

print("Done")
```

Output:

```
Done
```

---

# if-else Statement

Used when there are only two possible outcomes.

Syntax:

```python
if condition:
    statement
else:
    statement
```

Example:

```python
age = 17

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Output:

```
Minor
```

---

# if-elif-else Statement

Used when multiple conditions exist.

Syntax:

```python
if condition1:
    statement

elif condition2:
    statement

else:
    statement
```

Example:

```python
marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")
```

Output:

```
Grade B
```

---

# Multiple elif Example

```python
age = 35

if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior Citizen")
```

---

# Comparison Operators Used in Conditions

| Operator | Meaning |
|----------|---------|
| == | Equal to |
| != | Not Equal to |
| > | Greater than |
| < | Less than |
| >= | Greater than or Equal |
| <= | Less than or Equal |

Example:

```python
if age >= 18:
    print("Adult")
```

---

# Indentation

Python uses indentation instead of braces.

Correct:

```python
if True:
    print("Hello")
```

Wrong:

```python
if True:
print("Hello")
```

Error:

```
IndentationError
```

---

# One-Line if Statement

Python allows an if statement on one line when there is only one statement.

Syntax:

```python
if condition: statement
```

Example:

```python
if age >= 18: print("Adult")
```

Avoid using this for complex logic.

---

# Conditional Expression (Ternary Operator)

Normal:

```python
if age >= 18:
    category = "Adult"
else:
    category = "Minor"
```

Short Form:

```python
category = "Adult" if age >= 18 else "Minor"
```

Used when assigning one of two values.

---

# Program Flow

```
Start
   │
   ▼
Check Condition
   │
 ┌─┴─────┐
 │        │
True    False
 │        │
 ▼        ▼
if Block Skip Block
 │        │
 └───┬────┘
     ▼
 Continue Program
```

---

# Interview Questions

### Difference between if and if-else

**if**
- Executes only when condition is True.

**if-else**
- Executes one block if True.
- Executes another block if False.

---

### Difference between if and elif

- if starts a condition.
- elif checks another condition only if previous conditions were False.

---

# Common Errors

## Missing Colon

Wrong:

```python
if age >= 18
    print("Adult")
```

Error:

```
SyntaxError
```

Correct:

```python
if age >= 18:
    print("Adult")
```

---

## Wrong Indentation

Wrong:

```python
if age >= 18:
print("Adult")
```

Error:

```
IndentationError
```

---

# Best Practices

- Keep input, processing, and output separate.
- Use meaningful variable names.
- Use proper indentation.
- Use one-line if only for simple statements.
- Prefer readable code over short code.

---

# Real-World Example

```python
age = int(input("Enter Age: "))

if age < 18:
    category = "Minor"
else:
    category = "Adult"

print(f"Age Category : {category}")
```

---

# Memory Tips

- `if` → One decision.
- `if-else` → Two paths.
- `if-elif-else` → Multiple paths.
- Indentation defines the block.
- Condition must return `True` or `False`.
- Python executes only one matching branch in an `if-elif-else` chain.

---

# Day 03 Summary

✅ if Statement

✅ if-else Statement

✅ if-elif-else Statement

✅ Comparison Operators

✅ Indentation

✅ Program Flow

✅ One-Line if Statement

✅ Conditional Expression (Introduction)

✅ Common Errors

✅ Best Practices
