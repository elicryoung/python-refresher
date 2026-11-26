"""PYTHON FUNDAMENTALS — EXERCISES"""


# ============================================================
# EXERCISE 01.01 — VARIABLE ASSIGNMENT
# ============================================================

"""
QUESTION

Create variables containing the following values:
customer_id: C001
merchant_id: M005
amount: 7500
fee_percentage: 1.5
payment_successful: True

Print all five variables individually.

EXPECTED RESULT

C001
M005
7500
1.5
True
"""


# SOLUTION

"""
customer_id = "C001"
merchant_id = "M005"
amount = 7500
fee_percentage = 1.5
payment_successful = True

print(customer_id)
print(merchant_id)
print(amount)
print(fee_percentage)
print(payment_successful)
"""


# EXPECTED OUTPUT

"""
C001
M005
7500
1.5
True
"""


# EXPLANATION

"""
Strings require quotation marks.
Integers and floats do not require quotation marks.
Boolean values use True or False.
Python determines the variable type automatically.
"""


# ============================================================
# EXERCISE 01.02 — IDENTIFYING DATA TYPES
# ============================================================

"""
QUESTION

Identify the value and data type of each variable
without executing the code.

a = 500
b = "500"
c = 500.0
d = False
e = "True"
f = 10 / 2
g = 10 // 2

Code:
a = 500
b = "500"
c = 500.0
d = False
e = "True"
f = 10 / 2
g = 10 // 2

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))
print(g, type(g))
"""


# SOLUTION

"""
a = 500
b = "500"
c = 500.0
d = False
e = "True"
f = 10 / 2
g = 10 // 2

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))
print(g, type(g))
"""


# EXPECTED OUTPUT

"""
500 <class 'int'>
500 <class 'str'>
500.0 <class 'float'>
False <class 'bool'>
True <class 'str'>
5.0 <class 'float'>
5 <class 'int'>
"""


# EXPLANATION

"""
Quoted values are strings.
Standard division of integers returns a float.
Floor division of integers returns an integer.
"""


# ============================================================
# EXERCISE 01.03 — ARITHMETIC OPERATORS
# ============================================================

"""
QUESTION

Predict the output of each expression before running it.

Code:
print(17 / 5)
print(17 // 5)
print(17 % 5)
print(20 % 4)
print(3 ** 3)
print(10 + 5 * 2)
print((10 + 5) * 2)
"""


# SOLUTION

"""
print(17 / 5)
print(17 // 5)
print(17 % 5)
print(20 % 4)
print(3 ** 3)
print(10 + 5 * 2)
print((10 + 5) * 2)
"""


# EXPECTED OUTPUT

"""
3.4
3
2
0
27
20
30
"""


# EXPLANATION

"""
/ performs standard division.
// performs floor division.
% returns the remainder after division.
** raises a number to a power.
Multiplication takes priority over addition.
Parentheses change the order of operations.
"""


# ============================================================
# EXERCISE 01.04 — ARITHMETIC REINFORCEMENT
# ============================================================

"""
QUESTION

Predict the results of these arithmetic operations.

Code:
print(23 % 5)
print(23 // 5)
print(8 % 2)
print(9 % 2)
print(2 ** 5)
print(4 ** 2)
"""


# SOLUTION

"""
print(23 % 5)
print(23 // 5)
print(8 % 2)
print(9 % 2)
print(2 ** 5)
print(4 ** 2)
"""


# EXPECTED OUTPUT

"""
3
4
0
1
32
16
"""


# EXPLANATION

"""
Modulo returns what remains after division.
A number is even when its remainder after division
by 2 is zero.
Exponentiation repeatedly multiplies the base number.
"""
