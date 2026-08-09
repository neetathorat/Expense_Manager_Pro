# Expense Manager Pro

## Overview

Expense Manager Pro is a Python-based expense management application built to manage and track personal expenses.

This project is developed step by step using real-world software development practices, focusing on clean code, problem-solving, data modeling, file organization, and application design.

---

## Project Goal

The goal of this project is to build a complete expense management system while improving Python programming skills and learning real project development workflow.

---

## Current Version

**Version: 0.4**

---

## Features

### Completed

* Project structure setup
* Menu-driven application
* Application heading with project name and version
* Add expense feature
* View expense feature
* Store multiple expenses using a list of dictionaries
* Display message when no expenses exist
* Separate expense logic into `expense_data.py`
* Import functions between Python files
* Display expenses individually using a `for` loop
* Exception handling for invalid numeric input
* Invalid menu choice handling
* Invalid expense ID handling
* Invalid expense amount handling
* Prevent invalid expenses from being added

### Planned

* Automatic expense IDs
* Store expenses permanently
* Expense history
* Expense categories
* Monthly expense summary
* Budget tracking
* Data analysis
* Object-Oriented Programming structure
* AI-based spending insights

---

## Technologies Used

* Python

---

## Project Structure

```text
Expense_Manager_Pro/
│
├── main.py
├── expense_data.py
├── README.md
├── project_log.md
│
└── data/
    └── expense.txt
```

---

## Project Progress

### Day 01 — Project Setup

* Created project structure
* Created `data` folder
* Created initial expense storage file
* Designed basic application menu
* Created project heading and version display

### Day 02 — Data Modeling

* Created expense data model
* Added `expense_data.py`
* Designed one expense as a dictionary
* Designed the expense collection as a list of dictionaries
* Added fields:

  * `id`
  * `expense_name`
  * `amount`
  * `category`

### Day 03 — Expense Creation & Viewing

* Created `add_expense()` function
* Took expense information from user input
* Converted `id` to `int`
* Converted `amount` to `float`
* Created an expense dictionary using user input
* Returned the expense dictionary from `add_expense()`
* Imported `add_expense()` into `main.py`
* Added returned expenses to the `expenses` list
* Implemented `view_expenses()`
* Used a `for` loop to display each expense
* Accessed dictionary values using dictionary keys
* Added handling for an empty expense list
* Added visual separation between expenses

---

### Day 04 — Exception Handling

- Added `try` and `except` for risky operations
- Used `ValueError` for invalid numeric input
- Added invalid menu choice handling
- Added invalid expense ID handling
- Added invalid expense amount handling
- Used `continue` to keep the menu running after invalid input
- Prevented `None` from being added to the `expenses` list
- Tested valid and invalid user inputs

## Current Data Structure

### One Expense

```python
{
    "id": 1,
    "expense_name": "Apple",
    "amount": 100.0,
    "category": "Food"
}
```

### Multiple Expenses

```python
expenses = [
    {
        "id": 1,
        "expense_name": "Apple",
        "amount": 100.0,
        "category": "Food"
    },
    {
        "id": 2,
        "expense_name": "Bus Ticket",
        "amount": 50.0,
        "category": "Travel"
    }
]
```

---

## Current Menu

```text
1. Add Expense
2. View Expense
3. Exit
```

---

## Known Limitations

- Empty input validation is not implemented yet.
- Expense IDs are currently entered manually.
- Negative expense values are not validated yet.
- Expenses are currently stored only while the program is running.
- Permanent file storage is not implemented yet.
---

## Next Development Step

Implement input validation for empty and invalid expense data.

---

## Learning Focus

This project is being used to learn and practice:

* Python functions
* Lists and dictionaries
* List of dictionaries
* User input
* Return values
* Loops
* Conditional statements
* Function imports
* File organization
* Data modeling
* Exception handling
* Real-world project development workflow
