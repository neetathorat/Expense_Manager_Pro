# 02 Python Operators

## Objective

Learn different types of Python operators used for calculations, comparisons, decision making, updating values, checking membership, comparing objects, and working with bits.

---

# What is an Operator?

An operator is a symbol that performs an operation on one or more values.

Example:

10 + 5

Here:

10 and 5 are operands.

+ is the operator.

---

# Types of Python Operators

Python has several types of operators:

1. Arithmetic Operators
2. Comparison Operators
3. Logical Operators
4. Assignment Operators
5. Membership Operators
6. Identity Operators
7. Bitwise Operators

---

# 1. Arithmetic Operators

Arithmetic operators perform mathematical operations.

| Operator | Meaning | Example |
|----------|---------|---------|
| + | Addition | 5 + 3 |
| - | Subtraction | 5 - 3 |
| * | Multiplication | 5 * 3 |
| / | Division | 5 / 2 |
| // | Floor Division | 5 // 2 |
| % | Modulus | 5 % 2 |
| ** | Power | 2 ** 3 |

---

## Important Rules

Division:

5 / 2

Output:

2.5

The division operator always returns a float.

---

Floor Division:

5 // 2

Output:

2

It removes the decimal part by flooring the result.

---

Modulus:

5 % 2

Output:

1

It returns the remainder.

---

Power:

2 ** 3

Output:

8

Means:

2 * 2 * 2

---

# 2. Comparison Operators

Comparison operators compare two values.

They always return:

True

or

False

---

| Operator | Meaning |
|----------|---------|
| == | Equal to |
| != | Not equal to |
| > | Greater than |
| < | Less than |
| >= | Greater than or equal |
| <= | Less than or equal |

---

Examples:

10 == 10

Output:

True


10 != 5

Output:

True


"Python" == "python"

Output:

False

Reason:

String comparison is case-sensitive.

---

## Important Difference

== compares values.

Example:

5 == 5

True


is compares identity.

Example:

a is b

Checks whether both variables point to the same object.

---

# Boolean and Integer Relationship

In Python:

True behaves like 1.

False behaves like 0.

Examples:

True == 1

True


False == 0

True


True + True

Output:

2


False + 10

Output:

10

---

# 3. Logical Operators

Logical operators combine conditions.

| Operator | Meaning |
|----------|---------|
| and | Both conditions must be True |
| or | At least one condition must be True |
| not | Reverses the result |

---

## AND

Both conditions must be True.

Example:

True and True

Output:

True


True and False

Output:

False

---

## OR

At least one condition must be True.

Example:

True or False

Output:

True


False or False

Output:

False

---

## NOT

Reverses Boolean value.

Example:

not True

Output:

False


not False

Output:

True

---

# Truthy and Falsy Values

Falsy values:

False
0
0.0
""
[]
{}
()
None


Everything else is generally Truthy.

---

# Logical Operators With Values

Logical operators do not always return True or False.

They return one of the operands.

---

## AND Rule

Returns first Falsy value.

If no Falsy value exists, returns the last value.

Examples:

10 and 20

Output:

20


0 and 20

Output:

0

---

## OR Rule

Returns first Truthy value.

If no Truthy value exists, returns the last value.

Examples:

10 or 20

Output:

10


0 or 20

Output:

20

---

# Short-Circuit Evaluation

Python stops evaluating when the final result is already known.

Example:

False and (10 / 0)

Result:

False

The second expression is never executed.

---

True or (10 / 0)

Result:

True

The second expression is never executed.

---

# 4. Assignment Operators

Assignment operators assign or update values.

| Operator | Meaning |
|----------|---------|
| = | Assign |
| += | Add and assign |
| -= | Subtract and assign |
| *= | Multiply and assign |
| /= | Divide and assign |
| //= | Floor divide and assign |
| %= | Modulus and assign |
| **= | Power and assign |

---

Example:

x = 10

x += 5


Equivalent to:

x = x + 5


Output:

15

---

# Mutable Object Note

For immutable types:

int
float
str
bool

x += value behaves like:

x = x + value


For mutable objects like lists:

+= can modify the existing object.

---

# 5. Membership Operators

Membership operators check whether a value exists inside a collection.

| Operator | Meaning |
|----------|---------|
| in | Exists |
| not in | Does not exist |

---

Examples:

"a" in "apple"

Output:

True


20 in [10,20,30]

Output:

True


"AI" not in "OpenAI"

Output:

False

---

# Difference Between in and ==

in checks existence.

Example:

"a" in "apple"

Means:

Is "a" present inside "apple"?

Result:

True


== checks exact equality.

Example:

"a" == "apple"

Result:

False

---

# 6. Identity Operators

Identity operators compare object identity.

| Operator | Meaning |
|----------|---------|
| is | Same object |
| is not | Different object |

---

Example:

a = [1,2]

b = [1,2]


a == b

Output:

True


a is b

Output:

False


Because values are same but objects are different.

---

# None Comparison

Recommended:

value is None


Avoid:

value == None


Reason:

None is a singleton object.

---

# 7. Bitwise Operators

Bitwise operators work on binary representation of integers.

| Operator | Meaning |
|----------|---------|
| & | AND |
| | | OR |
| ^ | XOR |
| ~ | NOT |
| << | Left Shift |
| >> | Right Shift |

---

Examples:

5 & 3

Output:

1


5 | 3

Output:

7


5 ^ 3

Output:

6


5 << 1

Output:

10


8 >> 2

Output:

2


~7

Output:

-8

---

# Bitwise NOT Rule

Formula:

~x = -(x + 1)


Example:

~7

= -(7 + 1)

= -8

---

# Operator Precedence

Highest priority to lowest:

1. ()
2. **
3. Unary +, -, ~
4. *, /, //, %
5. +, -
6. <<, >>
7. &
8. ^
9. |
10. Comparison operators
11. not
12. and
13. or

---

# Common Beginner Mistakes

- Confusing = and ==
- Confusing == and is
- Forgetting that / returns float
- Thinking and/or always return Boolean values
- Forgetting string comparisons are case-sensitive
- Misunderstanding short-circuit evaluation

---

# Interview Points

- Operators perform operations on values.
- Comparison operators return Boolean values.
- bool is a subclass of int.
- True behaves like 1.
- False behaves like 0.
- == compares values.
- is compares object identity.
- Use is None for None checks.
- Logical operators use short-circuit evaluation.
- Membership operators check existence.
- Bitwise operators work on binary values.

---

# Revision Summary

Python operators allow programs to:

- Perform calculations
- Compare values
- Create logical decisions
- Update variables
- Search collections
- Compare object identity
- Manipulate binary data

Understanding operators is necessary before learning conditional statements because conditions depend heavily on operators.