# Day 05 - Logical Operators and Nested Conditions

## Topics Covered

* Logical Operators (`and`, `or`, `not`)
* Operator Precedence
* Short-Circuit Evaluation
* Nested `if`
* Compound Conditions
* Boolean Operations
* Debugging Logical Errors
* Real-World Decision Making

---

# 1. Logical Operators

Logical operators combine multiple conditions.

## `and`

Returns `True` only when **both** conditions are `True`.

### Syntax

```python
if condition1 and condition2:
    print("Both are True")
```

### Example

```python
age = 20
verified = True

if age >= 18 and verified:
    print("Access Granted")
```

Output

```
Access Granted
```

---

## `or`

Returns `True` if **at least one** condition is `True`.

### Example

```python
age = 16
parent_permission = True

if age >= 18 or parent_permission:
    print("Allowed")
```

Output

```
Allowed
```

---

## `not`

Reverses a boolean value.

### Example

```python
verified = False

if not verified:
    print("Verification Required")
```

Output

```
Verification Required
```

---

# 2. Operator Precedence

Python evaluates logical operators in this order:

```
()
not
and
or
```

### Example

```python
print(True or False and False)
```

Python evaluates:

```python
False and False
```

↓

```
False
```

Then:

```python
True or False
```

↓

```
True
```

Output

```
True
```

---

# 3. Short-Circuit Evaluation

Python stops evaluating an expression as soon as the final result is known.

### Example (`and`)

```python
x = 10

if x < 5 and x / 0 == 1:
    print("Hello")
```

`x / 0` is **never executed** because the first condition is already `False`.

---

### Example (`or`)

```python
x = 10

if x > 5 or x / 0 == 1:
    print("Hello")
```

Output

```
Hello
```

Python does not evaluate `x / 0` because the first condition is already `True`.

---

# 4. Nested `if`

A nested `if` is an `if` statement inside another `if`.

### Syntax

```python
if condition1:
    if condition2:
        print("Success")
```

### Example

```python
age = 22
experience = 3

if age >= 18:
    if experience >= 2:
        print("Eligible")
```

Output

```
Eligible
```

---

# 5. Compound Conditions

Multiple conditions can be combined into a single decision.

### Example

```python
age = 25
salary = 50000

if age >= 21 and salary >= 50000:
    print("Selected")
```

---

# 6. Truth Table

## AND

| A     | B     | Result |
| ----- | ----- | ------ |
| True  | True  | True   |
| True  | False | False  |
| False | True  | False  |
| False | False | False  |

---

## OR

| A     | B     | Result |
| ----- | ----- | ------ |
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |

---

## NOT

| A     | Result |
| ----- | ------ |
| True  | False  |
| False | True   |

---

# 7. Common Mistakes

### Mistake 1

```python
if age = 18:
```

Correct

```python
if age == 18:
```

---

### Mistake 2

Missing colon

```python
if logged_in == True
```

Correct

```python
if logged_in == True:
```

---

### Mistake 3

Wrong indentation

```python
if age >= 18:
print("Adult")
```

Correct

```python
if age >= 18:
    print("Adult")
```

---

### Mistake 4

Incomplete logical expression

```python
if x > 5 and:
```

Correct

```python
if x > 5 and x < 20:
```

---

# 8. Boolean and Integer Relationship

Python treats booleans as integers in arithmetic.

```
True  = 1
False = 0
```

Examples

```python
print(True + True)
```

Output

```
2
```

```python
print(False * 100)
```

Output

```
0
```

Comparison examples

```python
print(True == 1)
```

Output

```
True
```

```python
print(False == 0)
```

Output

```
True
```

---

# 9. Interview Notes

### Difference between `=` and `==`

* `=` assigns a value.
* `==` compares two values.

---

### Difference between multiple `if` and `if-elif-else`

Multiple `if` statements are checked independently.

`if-elif-else` is a single decision chain. Once one condition is `True`, the remaining branches are skipped.

---

### Preferred Boolean Style

Instead of

```python
if verified == True:
```

Prefer

```python
if verified:
```

Instead of

```python
if verified == False:
```

Prefer

```python
if not verified:
```

---

# 10. Real-World Applications

* Login systems
* ATM verification
* Employee eligibility
* Government scheme verification
* Membership approval
* AI automation workflows
* Access control systems

---

# Key Takeaways

* Use `and` when every condition must be `True`.
* Use `or` when at least one condition must be `True`.
* Use `not` to reverse a boolean value.
* Remember the precedence order:

  * `()`
  * `not`
  * `and`
  * `or`
* Understand short-circuit evaluation.
* Use nested `if` only when decisions depend on previous conditions.
* Prefer clean, readable conditions over duplicated logic.
* Think about the logic and design before writing code.

---

# Master Project Progress

## AutoMate AI v0.5

### Features Added

* User profile
* Age category
* Data type display
* Age analysis
* Department verification
* Experience verification
* Access verification
* User verification status
* Structured output sections

---

# Day 05 Summary

Today I learned how to combine multiple conditions using logical operators, understand operator precedence and short-circuit evaluation, write nested decision logic, debug logical errors, and integrate these concepts into the AutoMate AI master project by adding access verification and user status features.
