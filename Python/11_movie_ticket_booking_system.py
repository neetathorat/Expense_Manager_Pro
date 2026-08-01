def display_header():
    print("=" * 40)
    print("MOVIE TICKET BOOKING")
    print("=" * 40)

def collect_information():
    customer_name = input("Enter Customer Name : ")
    while True:
        movie_name = input("Enter Movie Name : ")
        if not movie_name:
            print("Empty movie name is invalid.")
        else:
            break
    while True:
        quantity = int(input("Enter No of Tickets required : "))
        if quantity <= 0:
            print("Enter valid number of tickets")
        else:
            break
    return customer_name, movie_name, quantity

def booking_category(quantity):
    if quantity <= 5:
        category = "Regular Booking"
    else:
        category = "Group Booking"
    return category

def calculate_price(quantity, standard_price = 200):
    discount = 0
    original_price = quantity * standard_price
    if quantity > 5:
        discount_percent = 10
        discount = (original_price * discount_percent) / 100
        final_price = original_price - discount
    else:
        final_price = original_price
    return original_price, discount, final_price  

def display_receipt(customer_name, movie_name, quantity, category, original_price, discount,final_price):
    print("=" * 40)
    print("RECEIPT")
    print("=" * 40)
    print(f" Customer Name   : {customer_name}")
    print(f" Movie Name      : {movie_name}")
    print(f" Tickets         : {quantity}")
    print(f" Booking Type    : {category}")
    print(f" Ticket Price    : {original_price}")
    print(f" Discount        : {discount}")
    print(f" Final Amount    : {final_price}")


def main():
    display_header()
    customer_name, movie_name, quantity = collect_information()
    category = booking_category(quantity)
    original_price, discount, final_price = calculate_price(quantity)
    display_receipt(customer_name = customer_name,
                    movie_name = movie_name,
                    quantity = quantity,
                    category = category,
                    original_price = original_price,
                    discount = discount,
                    final_price = final_price)

main()