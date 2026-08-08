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