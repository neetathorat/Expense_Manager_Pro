# Challenge 1: Student Marks Analyzer (Easy)
marks = [85, 90, 78, 92, 88]
print(marks) # Print the complete list.
print(marks[0]) # Print the first mark.
print(marks[-1]) # Print the last mark using negative indexing.
print(len(marks)) # Print the total number of marks.
marks[2] = 95 # Change the third mark to 95.
print(marks) # modified list

# Challenge 2: Shopping Cart System (Easy → Medium)
cart = ["Laptop", "Mouse", "Keyboard"]
print(cart)
cart.append("Monitor") # Add "Monitor" using append().
print(cart)
cart.remove("Mouse") # Remove "Mouse" using remove().
print(cart) # Print the final cart.
print(len(cart)) # Print how many items are in the cart.

# Challenge 3: Employee Name Manager (Medium)
employees = ["John", "Alice", "Mike", "Sara"]
for element in employees: 
    print(element)         # Print all employees using a loop.
employees[2] = "David" # Replace "Mike" with "David" using index.
print(employees)
employees.append("Neeta") # Add "Neeta" to the list.
print(employees)
employees.remove("Alice") # Remove "Alice".
print(employees) # Print the final list.

# Challenge 4: Number Processing System (Medium)
numbers = [10, 20, 30, 40, 50]
for num in numbers:
    print(num)               # Print each number using a loop.
total = 0
for num in numbers:
    total += num
print(f"Sum of all number is {total}")       # Calculate the sum manually using a loop.
large = numbers[0]
for num in numbers:
    if large < num:
        large = num
print(f"The largest number is {large}")      # Print the largest number.
small = numbers[0]
for num in numbers:
    if small > num:
        small = num
print(f"The smallest number is {small}")        # Print the smallest number.

# Challenge 5: Duplicate Detector (Hard 🔥)
numbers = [10, 20, 30, 20, 40, 10]
duplicate =[]
checked = []
for num in numbers:
    if num in checked:
        if num not in duplicate:
            duplicate.append(num)
    else:
        checked.append(num)
print("duplicate numbers : ")
for num in duplicate:
    print(num)    