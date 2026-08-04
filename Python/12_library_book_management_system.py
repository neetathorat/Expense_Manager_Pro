def display_books(books):
    print("Available books : ")
    print()
    i = 1
    for book in books:
        print(f"{i}. {book}")
        i +=1

def add_book(books):
    book_name = input("Add name of book :")
    if book_name not in books:
        books.append(book_name)
        print("Book added succesfully")
    else:
        print("Book is already exists")

def remove_book(books):
    while True:
        book_name = input("Enter book name to remove :")
        if book_name not in books:
            print("Book not found")
        else:
            books.remove(book_name)
            print("Book removed succesfully")
            break

def search_book(books):
    book_name = input("Enter book name to search : ")
    if book_name in books:
        print("Book is Available")
    else:
        print("Book is not Available")

def display_menu():
    print("=" * 5 + " LIBRARY MANAGEMENT SYSTEM " + "=" * 5)
    print("1. Display Books")
    print("2. Add Book")
    print("3. Remove Book")
    print("4. Search Book")
    print("5. Exit")

def main():
    books = ["Python Basics", "AI Fundamentals", "Data Science"]
    while True:
        display_menu()
        menu_number = int(input("Enter the operation number you want to perform"))
        if menu_number == 1:
            display_books(books)
        elif menu_number == 2:
            add_book(books)
        elif menu_number == 3:
            remove_book(books)
        elif menu_number == 4:
            search_book(books)
        elif menu_number == 5:
            print("Thank you for using Library Management System.")
            break
        else:
            print("Enter the right choice(1 to 5)")  
    
main()
