def calculate_total(expenses):
    """Calculate total amount for expenses """
    total = 0
    for expense in expenses:
        total += expense['amount']
    return total

def calculate_category_total(expenses):
    """Expenses for each category"""
    category_totals = {}
    for expense in expenses:
        if expense['category'] not in category_totals:
            category_totals[expense['category']] = expense['amount']
        else:
            category_totals[expense['category']] += expense['amount']
    return category_totals

def filter_expenses(expenses, category):
    """Filtered expenses according to given category"""
    filtered_expenses = []
    for expense in expenses:
        if expense['category'] == category:
            filtered_expenses.append(expense)
    return filtered_expenses

def get_amount(expense):
    return expense["amount"]

def sort_expenses_by_amount(expenses, reverse = False):
    """Expenses in ascending or descending order according to amount spend"""
    sorted_expenses = sorted(expenses, key= get_amount, reverse = reverse)
    return sorted_expenses

def get_category_total(item):
    return item[1]


def sort_category_total(category_total, reverse=False):
    """Categories in ascending or descending order according to amount spend"""
    sorted_category = sorted(category_total.items(), key=get_category_total, reverse=reverse)
    return sorted_category

