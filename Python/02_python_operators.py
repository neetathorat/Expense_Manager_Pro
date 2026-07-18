# 02 Python Operators


# 1. Arithmetic Operators

print("=" * 10 + " ARITHMETIC OPERATORS " + "=" * 10)

a = 10
b = 3

print("Addition :", a + b)
print("Subtraction :", a - b)
print("Multiplication :", a * b)
print("Division :", a / b)
print("Floor Division :", a // b)
print("Modulus :", a % b)
print("Power :", a ** b)


# 2. Comparison Operators

print("=" * 10 + " COMPARISON OPERATORS " + "=" * 10)

print(10 == 10)
print(10 != 5)
print(10 > 5)
print(5 < 2)
print(10 >= 10)
print(5 <= 3)

print("Python" == "python")
print("5" == 5)


# 3. Logical Operators

print("=" * 10 + " LOGICAL OPERATORS " + "=" * 10)

print(True and True)
print(True and False)

print(True or False)
print(False or False)

print(not True)
print(not False)


# Truthy and Falsy Examples

print("=" * 10 + " TRUTHY FALSY " + "=" * 10)

print(10 and 20)
print(0 and 20)

print(10 or 20)
print(0 or 20)


# 4. Assignment Operators

print("=" * 10 + " ASSIGNMENT OPERATORS " + "=" * 10)

x = 10

x += 5
print("After += :", x)

x -= 3
print("After -= :", x)

x *= 2
print("After *= :", x)

x //= 4
print("After //= :", x)

x %= 3
print("After %= :", x)

x **= 2
print("After **= :", x)


# 5. Membership Operators

print("=" * 10 + " MEMBERSHIP OPERATORS " + "=" * 10)

print("a" in "apple")
print("z" in "apple")

numbers = [10, 20, 30]

print(20 in numbers)
print(50 not in numbers)


# 6. Identity Operators

print("=" * 10 + " IDENTITY OPERATORS " + "=" * 10)

list1 = [1, 2, 3]
list2 = [1, 2, 3]

list3 = list1

print(list1 == list2)
print(list1 is list2)

print(list1 == list3)
print(list1 is list3)


value = None

print(value is None)
print(value == None)


# 7. Bitwise Operators

print("=" * 10 + " BITWISE OPERATORS " + "=" * 10)

print("AND :", 5 & 3)
print("OR :", 5 | 3)
print("XOR :", 5 ^ 3)
print("Left Shift :", 5 << 1)
print("Right Shift :", 8 >> 2)
print("NOT :", ~7)


# Operator Precedence Examples

print("=" * 10 + " PRECEDENCE " + "=" * 10)

print(2 + 3 * 4)
print((2 + 3) * 4)
print(2 ** 3 ** 2)

print(True or False and False)
print(not False and True)