# Expense Manager Pro

## Overview

Expense Manager Pro is a Python-based expense management application built to manage and track personal expenses.

This project is developed step by step using real-world software development practices, focusing on clean code, problem-solving, data modeling, file organization, file handling, and application design.

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
* JSON-based expense storage
* Save expenses to `expenses.json`
* Load existing expenses when the program starts
* Persistent expense data after closing the program
* Safe file handling using `with open()`

### Planned

* Automatic expense IDs
* Expense history
* Expense categories and category-based operations
* Monthly expense summary
* Budget tracking
* Data analysis
* Object-Oriented Programming structure
* AI-based spending insights

---

## Technologies Used

* Python
* JSON

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
    └── expenses.json
```

---

## Project Progress

### Day 01 — Project Setup

* Created project structure
* Created `data` folder
* Created initial application structure
* Designed basic application menu
* Created project heading and version display
* Created functions:

  * `project_heading()`
  * `display_menu()`
  * `add_expense()`
  * `view_expenses()`

### Day 02 — Data Modeling

* Created expense data model
* Added `expense_data.py`
* Designed one expense as a dictionary
* Designed the expense collection as a list of dictionaries
* Added fields:

  * `id`
  * `name`
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

### Day 04 — Exception Handling

* Added `try` and `except` for risky operations
* Used `ValueError` for invalid numeric input
* Added invalid menu choice handling
* Added invalid expense ID handling
* Added invalid expense amount handling
* Used `continue` to keep the menu running after invalid input
* Prevented `None` from being added to the `expenses` list
* Tested valid and invalid user inputs

### Day 05 — File Handling & JSON Storage

* Created `data/expenses.json`
* Learned file handling using `open()`
* Learned read mode (`"r"`)
* Learned write mode (`"w"`)
* Used `json.dump()` to save Python data to JSON
* Used `json.load()` to load JSON data into Python
* Created `save_expenses()` function
* Created `load_expenses()` function
* Loaded existing expenses when the application starts
* Saved new expenses after they are added
* Refactored file handling using `with open()`
* Tested persistent storage by closing and restarting the application
* Fixed inconsistent dictionary keys between existing JSON data and new expenses
* Learned that an empty JSON file should contain `[]` instead of being completely blank

---

## Current Data Structure

### One Expense

```python
{
    "id": 1,
    "name": "Apple",
    "amount": 100.0,
    "category": "Food"
}
```

### Multiple Expenses

```python
expenses = [
    {
        "id": 1,
        "name": "Apple",
        "amount": 100.0,
        "category": "Food"
    },
    {
        "id": 2,
        "name": "Bus Ticket",
        "amount": 50.0,
        "category": "Travel"
    }
]
```

---

## JSON Storage

Expenses are permanently stored in:

```text
data/expenses.json
```

### Save Flow

```text
Python expenses list
        ↓
json.dump()
        ↓
expenses.json
```

### Load Flow

```text
expenses.json
        ↓
json.load()
        ↓
Python expenses list
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

* Empty input validation is not implemented yet.
* Expense IDs are currently entered manually.
* Negative expense values are not validated yet.
* Expense editing and deletion are not implemented yet.
* Expense search and filtering are not implemented yet.
* Monthly summaries and reports are not implemented yet.

---

## Next Development Step

Improve expense input validation and continue expanding the expense management features.

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
* File handling
* JSON
* `json.dump()`
* `json.load()`
* `with open()`
* Persistent data storage
* Relative file paths
* Real-world project development workflow
