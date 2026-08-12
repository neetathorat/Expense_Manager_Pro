# Expense Manager Pro

## Overview

Expense Manager Pro is a Python-based expense management application built to manage and track personal expenses.

This project is developed step by step using real-world software development practices, focusing on clean code, problem-solving, data modeling, file organization, file handling, and application design.

---

## Project Goal

The goal of this project is to build a complete expense management system while improving Python programming skills and learning real project development workflow.

---

## Current Version

**Version: 1.0**

---

## Features

### Completed

- Project structure setup
- Menu-driven application
- Application heading with project name and version
- Add expense feature
- View expenses feature
- Store multiple expenses using a list of dictionaries
- Display message when no expenses exist
- Separate expense logic into `expense_data.py`
- Import functions between Python files
- Display expenses individually using a `for` loop
- Exception handling for invalid numeric input
- Invalid menu choice handling
- Invalid expense ID handling
- Invalid expense amount handling
- Prevent invalid expenses from being added
- JSON-based expense storage
- Save expenses to `expenses.json`
- Load existing expenses when the program starts
- Persistent expense data after closing the program
- Safe file handling using `with open()`
- Empty expense name validation
- Zero and negative amount validation
- Duplicate expense ID validation
- Calculate total expenses
- Display total amount spent
- Display total using the Indian Rupee symbol (₹)

### Planned

- Automatic expense IDs
- Expense categories and category-based operations
- Monthly expense summary
- Budget tracking
- Data analysis
- Object-Oriented Programming structure
- AI-based spending insights
---

## Technologies Used

- Python
- JSON

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

- Created project structure
- Created `data` folder
- Created initial application structure
- Designed basic application menu
- Created project heading and version display
- Created functions:

  - `project_heading()`
  - `display_menu()`
  - `add_expense()`
  - `view_expenses()`

### Day 02 — Data Modeling

- Created expense data model
- Added `expense_data.py`
- Designed one expense as a dictionary
- Designed the expense collection as a list of dictionaries
- Added fields:

  - `id`
  - `name`
  - `amount`
  - `category`

### Day 03 — Expense Creation & Viewing

- Created `add_expense()` function
- Took expense information from user input
- Converted `id` to `int`
- Converted `amount` to `float`
- Created an expense dictionary using user input
- Returned the expense dictionary from `add_expense()`
- Imported `add_expense()` into `main.py`
- Added returned expenses to the `expenses` list
- Implemented `view_expenses()`
- Used a `for` loop to display each expense
- Accessed dictionary values using dictionary keys
- Added handling for an empty expense list
- Added visual separation between expenses

### Day 04 — Exception Handling

- Added `try` and `except` for risky operations
- Used `ValueError` for invalid numeric input
- Added invalid menu choice handling
- Added invalid expense ID handling
- Added invalid expense amount handling
- Used `continue` to keep the menu running after invalid input
- Prevented `None` from being added to the `expenses` list
- Tested valid and invalid user inputs

### Day 05 — File Handling & JSON Storage

- Created `data/expenses.json`
- Learned file handling using `open()`
- Learned read mode (`"r"`)
- Learned write mode (`"w"`)
- Used `json.dump()` to save Python data to JSON
- Used `json.load()` to load JSON data into Python
- Created `save_expenses()` function
- Created `load_expenses()` function
- Loaded existing expenses when the application starts
- Saved new expenses after they are added
- Refactored file handling using `with open()`
- Tested persistent storage by closing and restarting the application
- Fixed inconsistent dictionary keys between existing JSON data and new expenses
- Learned that an empty JSON file should contain `[]` instead of being completely blank

### Day 06 — Debugging & Input Validation

- Tested the application with invalid and unexpected inputs
- Fixed empty expense name validation
- Added validation to reject zero and negative expense amounts
- Added duplicate expense ID validation
- Updated `add_expense()` to receive the existing `expenses` list
- Tested invalid ID input
- Tested invalid amount input
- Tested empty name input
- Tested duplicate ID input
- Confirmed invalid expenses are not added to the `expenses` list
- Confirmed duplicate IDs are rejected, including IDs already loaded from JSON
- Tested the application after debugging changes

### Day 07 — Version 1.0 Release

- Added `calculate_total()` function
- Calculated total amount from all expenses
- Added menu option to display total expenses
- Added Indian Rupee symbol (`₹`) to total display
- Tested total calculation with multiple expenses
- Tested expense persistence after restarting the application
- Verified saved expenses and calculated total after restart
- Completed core Version 1.0 functionality


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
2. View Expenses
3. Show Total
4. Exit
```

---

## Known Limitations

- Expense IDs are currently entered manually.
- Expense editing and deletion are not implemented yet.
- Expense search and filtering are not implemented yet.
- Monthly summaries and reports are not implemented yet.
- Expense categories are stored but category-based operations are not implemented yet.

---

## Next Development Step

Begin implementing expense management operations such as editing, deleting, and searching expenses.

---

## Learning Focus

This project is being used to learn and practice:

- Python functions
- Lists and dictionaries
- List of dictionaries
- User input
- Return values
- Loops
- Conditional statements
- Function imports
- File organization
- Data modeling
- Exception handling
- File handling
- JSON
- `json.dump()`
- `json.load()`
- `with open()`
- Persistent data storage
- Relative file paths
- Real-world project development workflow
- Debugging
- Testing invalid inputs
- Type validation vs value validation
- Data validation
- Debugging function data flow
- Calculating values from a list of dictionaries
- Testing data persistence