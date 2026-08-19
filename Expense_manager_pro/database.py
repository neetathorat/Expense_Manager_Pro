import json
"""Handle saving and loading expenses using JSON."""
def save_expenses(expenses):
    """Save expenses to the JSON file."""
    with open("data/expenses.json", "w") as file:
        json.dump(expenses,file)

def load_expenses():
    """Load expenses from the JSON file."""
    with open("data/expenses.json", "r") as file:
        return json.load(file)
