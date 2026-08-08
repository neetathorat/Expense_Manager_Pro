# Expense Manager Pro

## Overview

Expense Manager Pro is a Python-based expense management application built to manage and track personal expenses.

This project is developed step by step using real-world software development practices, focusing on clean code, problem-solving, data modeling, file organization, and application design.

---

## Project Goal

The goal of this project is to build a complete expense management system while improving Python programming skills and learning real project development workflow.

---

## Current Version

**Version: 0.3**

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

### Planned

* Input validation
* Exception handling
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

* Invalid menu input can currently cause a `ValueError`.
* Expense IDs are currently entered manually.
* Expenses are currently stored only while the program is running.
* Permanent file storage is not implemented yet.
* Exception handling is not implemented yet.

---

## Next Development Step

Implement exception handling to prevent the application from crashing when invalid user input is entered.

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
