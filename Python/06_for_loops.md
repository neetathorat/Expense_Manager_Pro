# Day 06 – Python `for` Loop Notes

## Topics Covered

* Introduction to loops
* `for` loop
* `range()` function
* Loop variable
* Memory model of loops
* Accumulator pattern
* Output prediction
* Debugging loops
* FizzBuzz problem
* Employee/Task ID Generator
* Number formatting using `:03d`

---

# 1. What is a Loop?

A loop is used to execute the same block of code multiple times.

Instead of writing:

```python
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
```

Use:

```python
for i in range(5):
    print("Hello")
```

---

# 2. Types of Loops

Python has two loops:

* `for` loop → Used when the number of iterations is known.
* `while` loop → Used when the number of iterations depends on a condition.

Today we studied only the **for loop**.

---

# 3. Syntax of `for` Loop

```python
for variable in iterable:
    statements
```

Example:

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

---

# 4. The `range()` Function

### `range(stop)`

```python
range(5)
```

Output:

```text
0
1
2
3
4
```

> The **stop value is excluded**.

---

### `range(start, stop)`

```python
range(2, 7)
```

Output:

```text
2
3
4
5
6
```

---

### `range(start, stop, step)`

```python
range(2, 11, 2)
```

Output:

```text
2
4
6
8
10
```

---

### Negative Step

```python
range(5, 0, -1)
```

Output:

```text
5
4
3
2
1
```

---

# 5. Loop Variable

```python
for i in range(5):
    print(i)
```

The value of `i` changes automatically.

```text
Iteration 1 → i = 0
Iteration 2 → i = 1
Iteration 3 → i = 2
Iteration 4 → i = 3
Iteration 5 → i = 4
```

---

# 6. Memory Model

Example:

```python
total = 0

for i in range(1, 5):
    total = total + i
    print(i, total)

print(total)
```

Memory Table:

| Iteration | i | total |
| --------- | - | ----- |
| Start     | - | 0     |
| 1         | 1 | 1     |
| 2         | 2 | 3     |
| 3         | 3 | 6     |
| 4         | 4 | 10    |

Output:

```text
1 1
2 3
3 6
4 10
10
```

---

# 7. Accumulator Pattern

An accumulator stores a running total.

Example:

```python
total = 0

for i in range(1, 6):
    total += i

print(total)
```

Output:

```text
15
```

---

# 8. Common Mistakes

### Missing Colon

```python
for i in range(5)
```

Correct:

```python
for i in range(5):
```

---

### Wrong Indentation

Wrong:

```python
for i in range(5):
print(i)
```

Correct:

```python
for i in range(5):
    print(i)
```

---

### Expecting Stop Value

Wrong assumption:

```python
range(5)
```

Output is **not**

```text
0 1 2 3 4 5
```

Correct output:

```text
0 1 2 3 4
```

---

### Forgetting Negative Step

```python
range(5, 0, -1)
```

Output:

```text
5
4
3
2
1
```

---

# 9. FizzBuzz

```python
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

### Important Rule

Always check the **most specific condition first**.

Correct:

```python
if i % 3 == 0 and i % 5 == 0:
```

before

```python
elif i % 3 == 0:
```

---

# 10. Employee/Task ID Generator

Example:

```python
task_count = int(input("How many task IDs? "))

for i in range(1, task_count + 1):
    print(f"TASK-{i:03d}")
```

Output:

```text
TASK-001
TASK-002
TASK-003
TASK-004
TASK-005
```

---

# 11. Number Formatting

```python
f"{i:03d}"
```

Examples:

```text
1   → 001
9   → 009
10  → 010
99  → 099
100 → 100
```

Meaning:

* `0` → Fill with zeros.
* `3` → Minimum width is 3 digits.
* `d` → Decimal integer.

---

# 12. Interview Questions

### Output

```python
for i in range(5, 0, -1):
    print(i)
```

Output:

```text
5
4
3
2
1
```

---

### Output

```python
for i in range(2, 12, 3):
    print(i)
```

Output:

```text
2
5
8
11
```

---

# 13. Best Practices

* Use meaningful variable names.
* Keep indentation consistent.
* Don't hardcode repeated values.
* Use `range(1, n + 1)` when counting from 1.
* Use `range(n)` when repeating something `n` times.
* Use `+=` for accumulators.
* Simulate loop execution mentally before running the program.

---

# Key Points to Remember

* A `for` loop repeats code.
* `range()` generates numbers.
* Start is included.
* Stop is excluded.
* Step controls increment or decrement.
* Negative step counts backwards.
* The loop variable changes automatically.
* Variables declared outside the loop keep their values.
* `:03d` formats numbers with leading zeros.
* Check the most specific condition first in `if-elif` chains.
* Always predict output before executing the program.

---

# Day 06 Summary

By the end of Day 06, you can:

* Write `for` loops confidently.
* Use all forms of `range()`.
* Trace loop execution using a memory model.
* Debug loop-related syntax and logic errors.
* Solve the FizzBuzz interview problem.
* Generate formatted IDs using loops.
* Integrate loop-based features into a real project.
