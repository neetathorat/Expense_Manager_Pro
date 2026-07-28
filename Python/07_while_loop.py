# Print the numbers from 1 to 10 using a while loop.
number = 1
while number <= 10:
    print(number)
    number += 1

# Print only even numbers from 2 to 20 using a while loop.
# type 1(loop execute 19 times)
number = 2
while number <= 20:
    if number % 2 == 0:
        print(number)
    number += 1

# type 2(loop execute 10 times)
number = 2
while number <= 20:
    print(number)
    number += 2

# Print the numbers from 10 to 1 using a while loop.
number = 10
while number >= 1:
    print(number)
    number -= 1

#  How many times do you want to print "Python AI"?
count = int(input("How many times do you want to print 'Python AI'?"))
i = 1
while i <= count:
    print("Python AI")
    i += 1

# multiplication table for given number
number = int(input("Enter a number : "))
i = 1
while i <= 10:
    print(f"{number} * {i} = {number * i}")
    i += 1