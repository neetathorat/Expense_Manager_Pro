def display_menu():
    print("=" * 20 + " MENU " + "=" * 20)
    print("Panipuri      :  40rs")
    print("Shevpuri      :  60rs")
    print("Bhelpuri      :  80rs")
    print("Ragadapuri    :  100rs")
    print("Chutneypuri   :  120rs")

def take_order():
    name = input("Enter your name : ")
    while True:
        food_item = input("Enter food item you want to order? ").lower()
        if food_item == "panipuri":
            price = 40
            break
        elif food_item == "shevpuri":
            price = 60
            break
        elif food_item == "bhelpuri":
            price = 80
            break
        elif food_item == "ragadapuri":
            price = 100
            break
        elif food_item == "chutneypuri":
            price = 120
            break
        else:
            print("Invalid food item")
    while True: 
        quantity = int(input("Enter quantity : "))
        if quantity <= 0:
            print("Enter the positive number")
        else:
            break
    
    return name,food_item,quantity,price

def calculate_bill(quantity,price,discount_percent = 10):
    discount = 0
    original_amount = quantity * price
    if original_amount > 500:
        discount = (original_amount * discount_percent)/100
        final_amount = original_amount - discount
    else:
        final_amount = original_amount
    return original_amount, discount, final_amount

def generate_receipt(name, food_item, quantity, original_amount, discount, final_amount):
    print("=" * 25 + " ORDER RECEIPT " + "=" * 25)
    print(f"Customer     : {name}")
    print(f"Food Item    : {food_item}")
    print(f"Quantity     : {quantity}")    
    print(f"Price        : {original_amount}")
    print(f"Discount     : {discount}")
    print(f"Final_amount : {final_amount}")
    print("=" * 50)
    


def main():
    display_menu()
    name, food_item, quantity,price = take_order()
    original_amount, discount, final_amount = calculate_bill(quantity,price)
    generate_receipt(name, food_item, quantity, original_amount, discount, final_amount)

main()