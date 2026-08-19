# Expense Manager Pro

## Overview

Expense Manager Pro is a Python-based expense management application built to manage and track personal expenses.

This project is developed step by step using real-world software development practices, focusing on clean code, problem-solving, data modeling, file organization, file handling, and application design.

---

## Project Goal

The goal of this project is to build a complete expense management system while improving Python programming skills and learning real project development workflow.

---

## Current Version

**Version: 2.0**

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
- Separate expense logic into `expenses.py`
- Separate JSON storage logic into `database.py`
- Importing and using functions from project modules
- Module-based project organization
- Object-Oriented Programming structure
- Created ExpenseManager class
- Converted expense functions into methods
- Added instance attribute for expense data
- Integrated ExpenseManager with JSON database operations
- Updated main.py to control the application through an ExpenseManager object
- Edit expense feature
- Remove expense feature
- Update expense name, amount, and category
- Find expenses by expense ID
- Validate edited expense name
- Validate edited expense amount
- Validate edited expense category
- Save edited expenses to JSON
- Save removed expenses to JSON
- Handle invalid expense IDs during edit and remove operations


### Planned
- Automatic expense IDs
- Expense categories and category-based operations
- Monthly expense summary
- Budget tracking
- Data analysis
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
├── data/
│   └── expenses.json
│
├── main.py
├── expenses.py
├── database.py
├── README.md
└── PROJECT_LOG.md    
    ```

---


```
## Module Responsibilities

### `main.py`

Controls the application flow.

- Displays the project heading
- Displays the menu
- Gets the user's choice
- Controls which operation is executed

### `expenses.py`

Contains the `ExpenseManager` class and expense-related operations.

- `ExpenseManager`
- `add_expense()`
- `view_expenses()`
- `edit_expense()`
- `remove_expense()`
- `calculate_total()`
- Maintains the expense data
- Uses `database.py` for loading and saving JSON data

### `database.py`

Handles JSON data storage.

- `save_expenses()`
- `load_expenses()`


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

### Day 08 — 13 & 14 August 2026

- Created `expenses.py` for expense-related operations
- Created `database.py` for JSON data storage
- Kept `main.py` as the application controller
- Moved `add_expense()`, `view_expenses()`, and `calculate_total()` into `expenses.py`
- Moved `save_expenses()` and `load_expenses()` into `database.py`
- Imported project modules into `main.py`
- Used `module.function()` to call functions from modules
- Learned the difference between `import module` and `from module import function`
- Separated application control, expense logic, and data storage responsibilities
- Fixed a naming collision between the `expenses` module and the expense list by using `expenses`
- Tested the application after the module refactor
- Verified Add Expense, View Expenses, Calculate Total, and JSON persistence

### Day 10 — Object-Oriented Programming — 15 August 2026

- Learned the basic concepts of Object-Oriented Programming in Python
- Learned class, object, constructor, `self`, instance attributes, and methods
- Created the `ExpenseManager` class
- Created an `ExpenseManager` object from `main.py`
- Added `__init__()` to initialize the object's expense data
- Converted `add_expense()` into a method
- Converted `view_expenses()` into a method
- Converted `calculate_total()` into a method
- Replaced passing `expense_list` between functions with `self.expenses`
- Connected `ExpenseManager` with `database.py`
- Loaded existing expenses through the `ExpenseManager` constructor
- Saved newly added expenses through `database.save_expenses()`
- Updated `main.py` to use the `ExpenseManager` object
- Updated `add_expense()` to return `True` on success and `False` on validation failure
- Tested adding, viewing, calculating totals, saving, and loading expenses after the OOP refactor

### Day 11 & 12 — CRUD Operations — 16 & 17 August 2026

- Implemented CRUD operations in the `ExpenseManager` class
- Added `edit_expense()` method
- Added `remove_expense()` method
- Used expense ID to find a specific expense
- Used a `for` loop to search through `self.expenses`
- Updated expense name, amount, and category
- Removed expenses from `self.expenses`
- Saved edited expenses to JSON
- Saved removed expenses to JSON
- Added validation for edited expense name
- Added validation for edited expense amount
- Added validation for edited expense category
- Added invalid ID handling for Edit and Remove
- Updated the main menu with Edit Expense and Remove Expense options
- Corrected menu control flow to call the appropriate methods
- Tested Add, View, Edit, Remove, and Calculate Total operations
- Tested persistence of edited and removed expenses after restarting the application

---
### Day 13 — Code Quality — 18 August 2026

- Improved naming consistency
- Added module documentation and function docstrings
- Removed unnecessary comments
- Improved code formatting and spacing
- Fixed the expense list insertion in `add_expense()`
- Updated `main.py` to use the Boolean result returned by `add_expense()`
- Reviewed separation of responsibilities between project modules

### Day 14 — Version 2.0 Release — 19 August 2026

- Reviewed the complete project structure
- Verified separation of responsibilities between `main.py`, `expenses.py`, and `database.py`
- Reviewed the Git commit history
- Updated project documentation for Version 2.0
- Reviewed README and PROJECT_LOG before the release
- Verified the application after the previous refactoring and CRUD changes
- Prepared the project for the Version 2.0 release

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
### OOP Data Flow

```text
main.py
    ↓
ExpenseManager object
    ↓
self.expenses
    ↓
add_expense()
view_expenses()
calculate_total()
    ↓
database.py
    ↓
expenses.json

---
```
## Current Menu

```text
1. Add Expense
2. View Expenses
3. Edit Expense
4. Remove Expense
5. Show Total
6. Exit

```
## Known Limitations

- Expense IDs are currently entered manually.
- Expense search and filtering are not implemented yet.
- Monthly summaries and reports are not implemented yet.
- Expense categories are stored but category-based operations are not implemented yet.
- Automated tests are not implemented yet.


## Next Development Step

- Improve validation design
- Review and reduce duplicated validation logic
- Improve expense ID management
- Add automated testing
- Improve application architecture before adding larger features

## Git Progress

- Version 1.0 released
- Project refactored into modules
- OOP refactor completed
- CRUD operations implemented
- Code quality improvements completed
- Version 2.0 released

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
- Python modules
- Creating modules
- `import module`
- `from module import function`
- Module responsibilities
- Basic module dependency
- Object-Oriented Programming
- Classes
- Objects
- Constructors
- `__init__()`
- `self`
- Instance attributes
- Methods
- Object state
- Basic encapsulation
- OOP-based project refactoring
- Code quality
- Naming conventions
- Docstrings
- Useful comments
- Code formatting
- Function responsibility
- Code readability
- Maintainable code structure
