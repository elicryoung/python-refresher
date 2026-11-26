"""PYTHON CONDITIONS — EXERCISES"""


# ============================================================
# EXERCISE 02.01 — COMPARISON OPERATORS
# ============================================================

"""
QUESTION

Predict whether each comparison returns True or False.

Code:
amount = 1000
threshold = 1000
merchant = "M001"

print(amount > threshold)
print(amount >= threshold)
print(amount != threshold)
print(amount == 1000)
print(merchant == "m001")
print(1000 == "1000")
print(amount <= threshold)
"""


# SOLUTION

"""
amount = 1000
threshold = 1000
merchant = "M001"

print(amount > threshold)
print(amount >= threshold)
print(amount != threshold)
print(amount == 1000)
print(merchant == "m001")
print(1000 == "1000")
print(amount <= threshold)
"""


# EXPECTED OUTPUT

"""
False
True
False
True
False
False
True
"""


# EXPLANATION

"""
> excludes equality.
>= and <= include equality.
== checks whether values are equal.
!= checks whether values are different.
String comparisons are case-sensitive.
An integer is not equal to a string containing that number.
"""


# ============================================================
# EXERCISE 02.02 — LOGICAL OPERATORS
# ============================================================

"""
QUESTION

Predict the result of each Boolean expression.

Code:
amount = 500
balance = 1000
verified = False
blocked = True

print(amount <= balance and verified)
print(amount <= balance or verified)
print(not verified)
print(not blocked)
print(verified or blocked)
print(amount > 100 and not blocked)
print((verified or blocked) and amount == 500)
"""


# SOLUTION

"""
amount = 500
balance = 1000
verified = False
blocked = True

print(amount <= balance and verified)
print(amount <= balance or verified)
print(not verified)
print(not blocked)
print(verified or blocked)
print(amount > 100 and not blocked)
print((verified or blocked) and amount == 500)
"""


# EXPECTED OUTPUT

"""
False
True
True
False
True
False
True
"""


# EXPLANATION

"""
and requires both conditions to be truthy.
or requires at least one condition to be truthy.
not reverses the truth value.
Parentheses allow conditions to be grouped together.
"""


# ============================================================
# EXERCISE 02.03 — PAYMENT CLASSIFICATION
# ============================================================

"""
QUESTION

Classify a payment according to its integer amount.

Zero or negative: Invalid payment
1-999: Small payment
1000-4999: Medium payment
5000 or more: Large payment

INPUT

amount = 2500

EXPECTED RESULT

Medium payment
"""


# SOLUTION

"""
amount = 2500

if amount <= 0:
    print("Invalid payment")
elif amount < 1000:
    print("Small payment")
elif amount < 5000:
    print("Medium payment")
else:
    print("Large payment")
"""


# EXPECTED OUTPUT

"""
Medium payment
"""


# EXPLANATION

"""
Python checks conditions from top to bottom.
Only the first matching branch executes.
Earlier conditions eliminate unnecessary lower boundaries.
The else branch handles all remaining integer amounts.
"""


# ============================================================
# EXERCISE 02.04 — TRANSACTION APPROVAL
# ============================================================

"""
QUESTION

Apply the following rules in order of priority:

1. Blocked customer: Account blocked
2. Zero or negative amount: Invalid amount
3. Unverified customer: Verification required
4. Amount exceeds balance: Insufficient funds
5. Otherwise: Payment approved

INPUT

amount = 750
balance = 1000
verified = True
blocked = False

EXPECTED RESULT

Payment approved
"""


# SOLUTION

"""
amount = 750
balance = 1000
verified = True
blocked = False

if blocked:
    print("Account blocked")
elif amount <= 0:
    print("Invalid amount")
elif not verified:
    print("Verification required")
elif amount > balance:
    print("Insufficient funds")
else:
    print("Payment approved")
"""


# EXPECTED OUTPUT

"""
Payment approved
"""


# EXPLANATION

"""
An if/elif chain preserves rule priority.
Boolean variables can be checked directly.
not verified checks whether verification is false.
The else branch runs only if every previous condition fails.
"""


# ============================================================
# EXERCISE 02.05 — BOOLEAN CONDITIONS
# ============================================================

"""
QUESTION

Predict which letters will be printed.

Code:
verified = True
blocked = False

if verified:
    print("A")

if not verified:
    print("B")

if blocked:
    print("C")

if not blocked:
    print("D")

if verified and not blocked:
    print("E")

if verified and blocked:
    print("F")
"""


# SOLUTION

"""
verified = True
blocked = False

if verified:
    print("A")

if not verified:
    print("B")

if blocked:
    print("C")

if not blocked:
    print("D")

if verified and not blocked:
    print("E")

if verified and blocked:
    print("F")
"""


# EXPECTED OUTPUT

"""
A
D
E
"""


# EXPLANATION

"""
verified is True.
blocked is False.
not blocked therefore evaluates to True.
Separate if statements are evaluated independently.
"""


# ============================================================
# EXERCISE 02.06 — ACCOUNT ACCESS
# ============================================================

"""
QUESTION

Write separate if statements for these requirements:

1. Verified customer: Verified customer
2. Not blocked: Account active
3. Verified and not blocked: Access granted
4. Admin or verified: Authorised
5. Neither admin nor verified: Access denied

Do not explicitly compare variables with True or False.

INPUT

verified = True
blocked = False
admin = False

EXPECTED RESULT

Verified customer
Account active
Access granted
Authorised
"""


# SOLUTION

# Write your solution here.


# EXPECTED OUTPUT

"""
Verified customer
Account active
Access granted
Authorised
"""


# EXPLANATION

"""
Complete after solving the exercise.
"""
