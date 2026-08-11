# Expense Manager Pro - Project Log


## Day 01 - Project Setup

### Status:
Completed


### Completed:
- Created Expense Manager Pro project structure
- Created main.py
- Created README.md
- Created PROJECT_LOG.md
- Designed the basic application workflow
- Built a menu-driven program structure
- Added project heading with project name and version
- Created functions:
  - project_heading()
  - display_menu()
  - add_expense()
  - view_expenses()


### Concepts Learned:
- Real project workflow
- Breaking problems into smaller functions
- Function responsibility
- Program planning before coding
- Menu-driven application design
- Using main() as the controller of program flow
- Improving user interface with formatted output


### Problems Discovered:
- Menu input can crash when invalid data type is entered
- Some functions still need better separation of responsibilities
- Expense data is not stored permanently yet


### Decisions Made:
- Keep project structure simple
- Add new files only when required
- Build features step by step
- Avoid unnecessary complexity in early versions


### Next:
- Improve expense handling system
- Start storing expense data
- Refine application structure

# Day 02 — 07 August 2026
## Data Modeling

### Objective
Design the data structure for storing expenses.

### Learned
- Dictionary
- List
- List of dictionaries
- Data modeling
- Dictionary references and `.copy()`

### Built
Created `expense_data.py` with:
- `expenses` list
- `expense` dictionary
- Expense fields: `id`, `name`, `amount`, `category`
- Added the expense dictionary to the expenses list

### Data Structure
One expense is represented as a dictionary.

Multiple expenses are stored in a list of dictionaries.

### Testing
Successfully tested:
- Creating an expense dictionary
- Adding the expense to the expenses list
- Printing the stored expense data

### Important Concept
`append()` stores a reference to the dictionary.
A copy is required only when the same dictionary object is reused and independent entries are needed.

### Status
Day 02 completed.

# Project Log — Day 03

## Date
07 August 2026

## Focus
Data Modeling + File Organization + Expense Storage

## Completed

- Created `expense_data.py` for expense-related logic.
- Imported `add_expense()` into `main.py`.
- Created an expense dictionary using user input.
- Added four expense fields:
  - `id`
  - `expense_name`
  - `amount`
  - `category`
- Used `return` to send the expense dictionary from `add_expense()`.
- Received the returned dictionary in `main.py`.
- Stored multiple expense dictionaries inside the `expenses` list.
- Connected `add_expense()` with the menu system.
- Implemented `view_expenses()`.
- Used a `for` loop to process each expense dictionary.
- Accessed dictionary values using keys.
- Added handling for an empty expenses list.
- Added separators between displayed expenses.

## Concepts Learned

- Importing functions between Python files
- Functions returning dictionaries
- List of dictionaries
- Dictionary key-value access
- `for` loop through a list of dictionaries
- Passing data between functions
- `return` without a value to stop a function
- Basic separation of responsibilities between files

## Current Data Model

```text
expenses → list
    ↓
expense → dictionary
    ├── id
    ├── expense_name
    ├── amount
    └── category
```

# Project Log — Day 04

## Date

09 August 2026

## Focus

Exception Handling + Input Error Handling

## Completed

* Added exception handling using `try` and `except`.
* Used `ValueError` to handle invalid numeric input.
* Added error handling for invalid expense IDs.
* Added error handling for invalid expense amounts.
* Added error handling for non-numeric menu choices.
* Used `continue` to return to the menu after an invalid menu choice.
* Used `return` to stop `add_expense()` when ID or amount is invalid.
* Prevented `None` from being added to the `expenses` list.
* Updated `main.py` to check whether `add_expense()` returned a valid expense before storing it.
* Tested valid and invalid user inputs.

## Concepts Learned

* `try`
* `except`
* `ValueError`
* `finally`
* Exception handling
* Input validation
* Difference between exceptions and validation
* Using `continue` inside a loop
* Using `return` to stop a function
* Handling `None` returned from a function
* Specific exception handling instead of using a bare `except`

## Important Concept

Exception handling and input validation are different.

Example:

"abc" → int("abc") → ValueError

This is an exception.

-100 → float("-100") → -100

This is a valid number, but it may fail the application's validation rules.

## Files Updated

* `main.py`
* `expense_data.py`

## Testing

Successfully tested:

* Valid menu choice
* Non-numeric menu choice
* Invalid expense ID
* Invalid expense amount
* Valid expense creation
* Invalid expense not being added to the `expenses` list
* Viewing expenses after invalid input

## Version

0.4

## Status

Day 04 completed.

# Project Log — Day 05

## Date

10 August 2026

## Focus

File Handling + JSON Data Storage

## Completed

* Created the `data` folder for persistent application data.
* Created `expenses.json` for storing expense data.
* Learned how to open files using `open()`.
* Learned read mode (`"r"`) and write mode (`"w"`).
* Used `json.dump()` to save Python data into a JSON file.
* Used `json.load()` to read JSON data back into Python.
* Created `save_expenses()` in `expense_data.py`.
* Created `load_expenses()` in `expense_data.py`.
* Connected JSON storage with the Expense Manager.
* Loaded existing expenses when the program starts.
* Saved updated expenses after adding a new expense.
* Refactored file handling to use `with open()`.
* Tested that expenses remain available after closing and restarting the program.
* Fixed a data-model inconsistency between `"name"` and `"expense_name"`.
* Learned that an empty JSON file is invalid and that an empty list should be represented as `[]`.

## Concepts Learned

* File handling
* `open()`
* Read mode (`"r"`)
* Write mode (`"w"`)
* JSON
* `json.dump()`
* `json.load()`
* `with open()`
* Relative file paths
* Persistent data storage
* Reading data from a file into Python
* Writing Python data to a file
* Context managers
* Keeping stored data consistent with the application's data model

## Data Flow

```text
Python Data
    ↓
json.dump()
    ↓
expenses.json
```

```text
expenses.json
    ↓
json.load()
    ↓
Python Data
```

## Current Data Structure

```text
expenses → list
    ↓
expense → dictionary
    ├── id
    ├── name
    ├── amount
    └── category
```

## Files Updated

* `main.py`
* `expense_data.py`
* `data/expenses.json`

## Storage Functions

```text
add_expense()
    ↓
Creates one expense dictionary

save_expenses(expenses)
    ↓
Saves expenses list to JSON

load_expenses()
    ↓
Loads expenses list from JSON
```

## Testing

Successfully tested:

* Creating `expenses.json`
* Writing expense data to JSON
* Reading existing JSON data
* Adding new expenses and saving them
* Viewing stored expenses
* Closing and restarting the program
* Confirming previously stored expenses remain available
* Handling an initially empty JSON data set using `[]`
* Correcting the file path when PowerShell was running from the wrong directory

## Important Lessons

* Data stored only in Python variables is lost when the program closes.
* JSON provides persistent storage for the application.
* `"w"` mode creates a file if it does not exist but replaces existing contents.
* `"r"` mode requires the file to already exist.
* `json.dump()` converts Python data into JSON and writes it to a file.
* `json.load()` reads JSON data and converts it back into Python data.
* `with open()` automatically closes the file after the operation.
* Stored data and the current Python data model must use consistent dictionary keys.

## Version

0.4

## Status

Day 05 completed.

# Project Log — Day 06

## Date

11 August 2026

## Focus

Debugging + Input Validation

## Completed

* Tested the existing Expense Manager Pro application with invalid inputs.
* Debugged the `add_expense()` function.
* Fixed empty expense name validation.
* Added validation to reject zero and negative expense amounts.
* Added duplicate expense ID validation.
* Updated `add_expense()` to receive the existing `expenses` list as a parameter.
* Tested invalid ID input.
* Tested invalid amount input.
* Tested empty name input.
* Tested duplicate ID input.
* Confirmed invalid expenses are not added to the expenses list.
* Confirmed duplicate IDs are rejected even when existing expenses are loaded from JSON.
* Tested the application after making debugging changes.

## Bugs Found and Fixed

### Bug 1 — Empty Expense Name

**Problem:**

An empty expense name was accepted and the program continued.

**Fix:**

Added validation using:

```python
if not name:
    print("Invalid name")
    return
```

### Bug 2 — Zero and Negative Amounts

**Problem:**

Values such as `0` and `-500` were accepted because they are valid `float` values.

**Fix:**

Added value validation:

```python
if amount <= 0:
    print("Invalid amount")
    return
```

### Bug 3 — Duplicate Expense IDs

**Problem:**

The application allowed multiple expenses with the same ID.

**Fix:**

Checked the existing `expenses` list before creating a new expense.

```python
for expense in expenses:
    if expense["id"] == expense_id:
        print("Invalid ID")
        return
```

Updated the function to receive the existing expense list:

```python
def add_expense(expenses):
```

And passed the list from `main.py`:

```python
add_expense(expenses)
```

## Concepts Learned

* Debugging
* Finding the difference between expected and actual behavior
* Input validation
* Type validation vs value validation
* Testing invalid inputs
* Checking existing data before creating new data
* Passing a list to a function as a parameter
* Understanding `return` during validation
* Debugging data flow between `main.py` and `expense_data.py`

## Testing

Successfully tested:

* Non-numeric ID
* Non-numeric amount
* Empty expense name
* Empty category
* Zero amount
* Negative amount
* Valid positive amount
* Duplicate expense ID
* Invalid data not being added
* Duplicate ID detection against JSON-loaded expenses

## Important Lessons

* A value can have the correct data type but still be invalid for the application.
* `try/except` handles conversion errors, while conditions handle business rules.
* `return` stops `add_expense()` when validation fails.
* A function should receive the data it needs through parameters.
* Debugging requires testing actual application behavior instead of assuming the code works.

## Version

0.6

## Status

Day 06 completed.

