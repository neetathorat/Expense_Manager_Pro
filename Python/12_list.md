# 📘 Day 12 – Lists in Python

## 🎯 Learning Objective

Learn how to store, access, modify, and manage multiple values using **Lists** in Python.

---

# 1. What is a List?

A **list** is an ordered and mutable collection that stores multiple values under a single variable.

### Syntax

```python
numbers = [10, 20, 30, 40]
```

### Example

```python
employees = ["John", "Alice", "Mike"]
```

---

# 2. Characteristics of Lists

- Ordered collection
- Mutable (can be modified)
- Stores multiple values
- Allows duplicate values
- Supports heterogeneous data (different data types)

### Example

```python
data = ["Neeta", 20, 5.5, True]
```

---

# 3. Creating Lists

```python
numbers = [10, 20, 30]

names = ["John", "Alice", "Mike"]

empty_list = []

another_list = list()
```

---

# 4. Indexing

Lists use **zero-based indexing**.

```python
names = ["John", "Alice", "Mike", "Sara"]
```

| Index | Value |
|------:|-------|
| 0 | John |
| 1 | Alice |
| 2 | Mike |
| 3 | Sara |

### Example

```python
print(names[0])
print(names[2])
print(names[-1])
```

**Output**

```text
John
Mike
Sara
```

---

# 5. Negative Indexing

Negative indexing starts from the end.

```python
names = ["John", "Alice", "Mike", "Sara"]
```

| Index | Value |
|------:|-------|
| -1 | Sara |
| -2 | Mike |
| -3 | Alice |
| -4 | John |

### Example

```python
print(names[-2])
```

**Output**

```text
Mike
```

---

# 6. Slicing

### Syntax

```python
list[start:end]
```

### Rule

- Start index is **included**.
- End index is **excluded**.

### Example

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

**Output**

```text
[20, 30, 40]
```

Indexes used:

```
1 ✅
2 ✅
3 ✅
4 ❌
```

---

# 7. Modifying Elements

Lists are mutable.

```python
numbers = [10, 20, 30]

numbers[1] = 200

print(numbers)
```

**Output**

```text
[10, 200, 30]
```

---

# 8. Common List Methods

## append()

Adds an element to the end of the list.

```python
numbers = [10, 20]

numbers.append(30)

print(numbers)
```

**Output**

```text
[10, 20, 30]
```

---

## remove()

Removes an element by value.

```python
names = ["John", "Alice", "Mike"]

names.remove("Alice")

print(names)
```

**Output**

```text
['John', 'Mike']
```

---

# 9. Finding Length

```python
numbers = [10, 20, 30]

print(len(numbers))
```

**Output**

```text
3
```

---

# 10. Traversing a List

```python
employees = ["John", "Alice", "Mike"]

for employee in employees:
    print(employee)
```

**Output**

```text
John
Alice
Mike
```

---

# 11. List References

```python
numbers = [10, 20, 30]

a = numbers

a.append(40)

print(numbers)
```

**Output**

```text
[10, 20, 30, 40]
```

### Memory Representation

```
numbers ───┐
           ▼
      [10,20,30,40]
           ▲
a ─────────┘
```

**Important:** `a = numbers` does **not** create a new list. Both variables refer to the same list object.

---

# 12. Copying Lists

## Using copy()

```python
numbers = [10, 20, 30]

a = numbers.copy()

a.append(40)

print(numbers)
print(a)
```

**Output**

```text
[10, 20, 30]
[10, 20, 30, 40]
```

---

## Using Slicing

```python
numbers = [10, 20, 30]

a = numbers[:]
```

This also creates a new list.

---

# 13. Reference vs Copy

## Reference

```python
a = numbers
```

- One list object
- Changes affect both variables

## Copy

```python
a = numbers.copy()
```

or

```python
a = numbers[:]
```

- Two separate list objects
- Changes affect only the copied list

---

# 14. Common Errors

## IndexError

```python
numbers = [10, 20]

print(numbers[5])
```

**Reason:** Index does not exist.

---

## ValueError

```python
numbers = [10, 20]

numbers.remove(30)
```

**Reason:** Value is not present in the list.

---

## TypeError

```python
number = 10

number[0]
```

**Reason:** Integer objects cannot be indexed.

---

# 15. List vs String

| List | String |
|------|--------|
| Mutable | Immutable |
| Stores multiple values | Stores characters |
| Can modify elements | Cannot modify characters |

---

# 16. Coding Challenges Completed

### Challenge 1
Student Marks Analyzer

### Challenge 2
Shopping Cart System

### Challenge 3
Employee Name Manager

### Challenge 4
Number Processing System

### Challenge 5
Duplicate Detector

Pattern learned:

```python
checked = []
duplicates = []
```

Remember previously seen values to detect duplicates.

---

# 17. Mini Project

## Library Book Management System

### Features

- Display Books
- Add Book
- Remove Book
- Search Book
- Menu-driven program
- Duplicate validation
- Function-based design

---

# 18. Master Project Integration

Extended **AI Automation Assistant** with Task Management.

### Added Features

- Add Task
- View Tasks
- Remove Task
- Search Task
- Menu-driven interface
- Duplicate task validation

---

# 19. Interview Points

Be able to explain:

- What is a list?
- Why are lists mutable?
- Difference between indexing and append()
- Difference between `a = numbers` and `a = numbers.copy()`
- Difference between `[]` and `list()`
- Why slicing excludes the ending index
- Difference between reference and copy

---

# 20. Key Takeaways

- Lists store multiple values under one variable.
- Lists are ordered and mutable.
- Indexing starts from **0**.
- Negative indexing starts from **-1**.
- Slicing follows **start inclusive, end exclusive**.
- `append()` adds an element at the end.
- `remove()` removes an element by value.
- `len()` returns the total number of elements.
- `a = numbers` creates a reference to the same list.
- `copy()` and `[:]` create a new list.
- Validate user input before modifying a list.
- Break programs into functions for better readability and maintainability.

---

# ✅ Day 12 Summary

## Theory Covered

- Lists
- Indexing
- Negative Indexing
- Slicing
- Mutability
- List References
- List Copying

## Practical Covered

- Output Prediction
- Debugging
- Interview Questions
- Tricky Questions
- 5 Coding Challenges
- Library Book Management System
- AI Automation Assistant Task Management

## Status

✅ Day 12 Completed

**Next Topic:** Strings in Python