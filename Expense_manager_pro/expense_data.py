# expenses = []
# expense = {"id" : 1 ,"name": "Apple", "amount" : 100, "category" : "Food"}
# expenses.append(expense)
# print(expenses)
# print(expense)

def add_expense():
    expense_id = int(input(" Enter id :"))
    expense_name = input("Enter name of expense : ")
    amount = float(input("Enter amount : "))
    category = input("Enter category : ")
    expense = {"id":expense_id, "expense_name": expense_name, "amount":amount, "category":category}
    return expense
