"""Lists — Python Exercises"""

# ============================================================
# EXERCISE 03.01 — CREATING LISTS
# ============================================================
'''

# QUESTION
"""
A payment processing system needs to store transaction
amounts, merchant IDs and verification statuses.

# REQUIREMENTS

1. Create a list called transactions containing:
   100, 250, 500, 250, 1000

2. Create a list called merchants containing:
   M001, M002, M003

3. Create a list called verified containing:
   True, False, True

4. Create an empty list called rejected.

5. Print all four lists.
"""

# INPUT
# Create the lists yourself.
transactions = [100, 250, 500, 250, 1000]

merchants = ["M001", "M002", "M003"]

verified = [True, False, True]

rejected = []
# SOLUTION
print(transactions)
print(merchants)
print(verified)
print(rejected)

# EXPECTED OUTPUT
"""
[100, 250, 500, 250, 1000]
['M001', 'M002', 'M003']
[True, False, True]
[]
"""


'''
# ============================================================
# EXERCISE 03.02 — ACCESSING LIST ELEMENTS
# ============================================================
'''


# QUESTION
"""
A merchant has received five payments.

# REQUIREMENTS

1. Store the first transaction in a variable called first.
2. Store the third transaction in a variable called third.
3. Store the fifth transaction in a variable called fifth.
4. Calculate the combined value of these three transactions.
5. Print the three transactions and their combined total.

Use list indexing.
"""

# INPUT
transactions = [200, 450, 600, 150, 900]

# SOLUTION
first = transactions[0]
third = transactions[2]
fifth = transactions[4]

total = first + third + fifth
print(first, third, fifth, sep="\n")

print(total)

# EXPECTED OUTPUT
"""
First: 200
Third: 600
Fifth: 900
Total: 1700
"""

'''

# ============================================================
# EXERCISE 03.03 — RECENT TRANSACTIONS
# ============================================================

'''
# QUESTION
"""
A payment system stores transactions in chronological order,
with the most recent transaction at the end of the list.

# REQUIREMENTS

1. Store the most recent transaction in a variable.
2. Store the second most recent transaction in a variable.
3. Store the third most recent transaction in a variable.
4. Calculate their combined value.
5. Print all three amounts and their total.

Use negative indexing only.
"""

# INPUT
transactions = [120, 450, 800, 250, 600, 950, 300]

# SOLUTION
most_recent = transactions[-1]
second_most_recent = transactions[-2]
third_most_recent = transactions[-3]

total = most_recent + second_most_recent + third_most_recent
print(most_recent, second_most_recent, third_most_recent, sep="\n")
print(total)


# EXPECTED OUTPUT
"""
300
950
600
1850
"""
'''
# ============================================================
# EXERCISE 03.04 — SLICING TRANSACTIONS
# ============================================================
'''
# QUESTION
"""
A payment system stores transactions in chronological order.

# REQUIREMENTS

1. Retrieve the first three transactions.
2. Retrieve the last three transactions.
3. Retrieve the transactions at indexes 2, 3 and 4.
4. Retrieve every transaction except the first two.
5. Retrieve every second transaction, starting at index 0.
6. Retrieve all transactions in reverse order.
7. Print each resulting list.

Use slicing for every requirement.
Do not use loops.
"""

# INPUT
transactions = [120, 450, 800, 250, 600, 950, 300]

# SOLUTION
print(transactions[:3])
print(transactions[-3:])
print(transactions[2:5])
print(transactions[2:])
print(transactions[::2])
print(transactions[::-1])

# EXPECTED OUTPUT
"""
[120, 450, 800]
[600, 950, 300]
[800, 250, 600]
[800, 250, 600, 950, 300]
[120, 800, 600, 300]
[300, 950, 600, 250, 800, 450, 120]
"""

'''


# ============================================================
# EXERCISE 03.05 — UPDATING TRANSACTIONS
# ============================================================

# QUESTION
"""
A merchant needs to correct several transaction amounts.

# REQUIREMENTS

1. Replace the first transaction with 150.
2. Increase the second transaction by 100.
3. Reduce the third transaction by 50.
4. Double the last transaction.
5. Print the updated list.

Use indexing and assignment operators.
Do not recreate the entire list.
"""
""" 
# INPUT
transactions = [120, 450, 800, 250, 600]

# SOLUTION
transactions[0] = 150
transactions[1] += 100
transactions[2] -= 50
transactions[-1] *= 2

print(transactions)
 """
# EXPECTED OUTPUT
"""
[150, 550, 750, 250, 1200]
"""


# ============================================================
# EXERCISE 03.06 — ADDING TRANSACTIONS
# ============================================================

# QUESTION
"""
A merchant receives new transactions and discovers
a previously missing transaction.

# REQUIREMENTS

1. Add a transaction of 900 to the end of the list.
2. Insert a transaction of 50 at the beginning.
3. Insert a transaction of 350 at index 2.
4. Add transactions of 1200, 750 and 300 together
   using a single method.
5. Print the final list.

Use append(), insert() and extend().
Do not recreate the entire list.
"""
""" 
# INPUT
transactions = [100, 450, 800]

# SOLUTION
transactions.append(900)
transactions.insert(0,50)
transactions.insert(1, 350)
transactions.extend([1200, 750, 300])
print(transactions)
 """

# EXPECTED OUTPUT
"""
[50, 100, 350, 450, 800, 900, 1200, 750, 300]
"""

# ============================================================
# EXERCISE 03.08 — REMOVING TRANSACTIONS
# ============================================================

# QUESTION
"""
A payment system needs to remove several transactions.

# REQUIREMENTS

1. Remove the first occurrence of 450 by value.
2. Remove the last transaction and store it in
   a variable called refunded.
3. Delete the first two remaining transactions
   using slicing.
4. Print the remaining transactions.
5. Print the refunded amount.
6. Clear the entire transaction list.
7. Print the empty list.
"""
""" 
# INPUT
transactions = [100, 450, 800, 250, 450, 900, 600]

# SOLUTION
transactions.remove(450)

refunded = transactions.pop(-1)

del transactions[:2]

print(transactions)
print(refunded)

transactions.clear()

print(transactions)

 """
# EXPECTED OUTPUT
"""
[250, 450, 900]
600
[]
"""

# ============================================================
# EXERCISE 03.09 — MERCHANT REGISTRATION
# ============================================================

# QUESTION
"""
A payment platform needs to register new merchants while
preventing duplicate registrations and blocked merchants.

# REQUIREMENTS

1. If the merchant is in the blocked list, print:
   Merchant blocked

2. If the merchant is already registered, print:
   Merchant already registered

3. Otherwise, add the merchant to the registered list
   and print:
   Merchant registered successfully

4. Print the registered merchants after the conditions.

Blocked merchants must always be rejected first.
"""
""" 
# INPUT
registered = ["M001", "M002", "M003"]
blocked = ["M005", "M009"]
merchant = "M004"

# SOLUTION

if merchant in blocked:
    print("Merchant Blocker")
elif merchant in registered:
    print("Merchant already registered")
else:
    registered.append(merchant)
    print("Merchant registered successfully")

print(registered)
 """


# EXPECTED OUTPUT
"""
Merchant registered successfully
['M001', 'M002', 'M003', 'M004']
"""


# ============================================================
# EXERCISE 03.10 — MERCHANT CAPACITY
# ============================================================

# QUESTION
"""
A payment platform can register a maximum of five merchants.

# REQUIREMENTS

1. If the merchant is already registered, print:
   Merchant already registered

2. Otherwise, if the platform is at or above capacity,
   print:
   Capacity reached

3. Otherwise, register the merchant and print:
   Merchant registered successfully

4. Print the total number of registered merchants.

5. Print the number of remaining available spaces.

Use len() to determine the number of merchants.
"""
""" 
# INPUT
registered = ["M001", "M002", "M003"]
merchant = "M004"
capacity = 5

# SOLUTION

if merchant in registered:
    print("merchant already registered")
elif len(registered) >= capacity:
    print("capacity reached")
else:
    registered.append(merchant)
    print("merchant registered successfully")

print(len(registered))
print(capacity - len(registered))
 """

# EXPECTED OUTPUT
"""
Merchant registered successfully
4
1
"""

# ============================================================
# EXERCISE 03.11 — COMBINING TRANSACTION RECORDS
# ============================================================

# QUESTION
"""
A merchant stores morning, afternoon and evening
transactions in separate lists.

# REQUIREMENTS

1. Combine all three lists into a new list
   called daily_transactions.

2. Preserve all three original lists.

3. Print daily_transactions.

4. Print the total number of daily transactions.

5. Print the original morning transactions.
"""

""" # INPUT
morning = [100, 250, 300]
afternoon = [450, 800]
evening = [150, 900, 600]

# SOLUTION
daily_transactions = morning + afternoon + evening

print(daily_transactions)
print(len(daily_transactions))
print(morning)
 """
# EXPECTED OUTPUT
"""
[100, 250, 300, 450, 800, 150, 900, 600]
8
[100, 250, 300]
"""

# ============================================================
# EXERCISE 03.12 — TRANSACTION BACKUP
# ============================================================

# QUESTION
"""
A payment platform needs to correct transaction records
without modifying the original data.

# REQUIREMENTS

1. Create a copy of transactions called corrected.
2. Replace the first transaction in corrected with 150.
3. Remove the transaction worth 800 from corrected.
4. Add a transaction worth 1200 to corrected.
5. Print the original transactions.
6. Print the corrected transactions.
7. Print the number of corrected transactions.

The original list must remain unchanged.
"""
""" 
# INPUT
transactions = [100, 450, 800, 250, 600]

# SOLUTION

corrected = transactions.copy()

corrected[0] = 150
corrected.remove(800)
corrected.append(1200)

print(transactions)
print(corrected)
print(len(corrected))
 """
# EXPECTED OUTPUT
"""
[100, 450, 800, 250, 600]
[150, 450, 250, 600, 1200]
5
"""

# ============================================================
# EXERCISE 03.13 — NESTED TRANSACTION RECORDS
# ============================================================

# QUESTION
"""
A payment platform stores transaction records containing
a merchant ID, transaction amount and verification status.

# REQUIREMENTS

1. Print the entire first transaction record.
2. Print the second merchant's ID.
3. Print the third merchant's transaction amount.
4. Print the last merchant's verification status.
5. Increase the second merchant's amount by 100.
6. Change the third merchant's verification status to True.
7. Add a new record containing M005, 1200 and True.
8. Print the updated transaction records.
9. Print the total number of records.

Use nested indexing and previously learned list methods.
Do not use loops.
"""
""" 
# INPUT
transactions = [
    ["M001", 500, True],
    ["M002", 750, False],
    ["M003", 200, False],
    ["M004", 900, True]
]

# SOLUTION
print(transactions[0])
print(transactions[1][0])
print(transactions[2][1])
print(transactions[-1][2])
transactions[1][1] += 100
transactions[2][2] = True
transactions.append(['M005', 1200, True])
print(transactions)
print(len(transactions))
 """
# EXPECTED OUTPUT
"""
['M001', 500, True]
M002
200
True
[['M001', 500, True], ['M002', 850, False], ['M003', 200, True], ['M004', 900, True], ['M005', 1200, True]]
5
"""

# ============================================================
# EXERCISE 03.14 — COPYING NESTED RECORDS
# ============================================================

# QUESTION
"""
A merchant wants to modify a backup of two transaction
records without affecting the original records.

# REQUIREMENTS

1. Create a backup with independent inner lists.
2. Increase the first backup transaction amount by 100.
3. Change the second backup verification status to True.
4. Print the original transactions.
5. Print the backup transactions.

The original records must remain unchanged.
Do not use loops.
"""
""" 
# INPUT
transactions = [
    ["M001", 500, True],
    ["M002", 750, False]
]

# SOLUTION
backup = [transactions[0].copy(), transactions[1].copy()]

backup[0][1] += 100
backup[1][2] = True
print(transactions)
print(backup)
 """
# EXPECTED OUTPUT
"""
[['M001', 500, True], ['M002', 750, False]]
[['M001', 600, True], ['M002', 750, True]]
"""


# ============================================================
# EXERCISE 03.15 — PAYMENT PROCESSING
# ============================================================

# QUESTION
"""
A payment platform receives a batch of transactions.
The platform needs to validate and correct the batch
while preserving the original records.

# REQUIREMENTS

1. Create an independent copy of the original transactions
   called processed.
2. Remove the first occurrence of 0 from processed.
3. If the customer is blocked, print:
   Customer blocked
4. Otherwise, if the new payment is zero or negative, print:
   Invalid payment
5. Otherwise, if the new payment already exists in processed,
   print:
   Duplicate payment

6. Otherwise, add the new payment to processed and print:
   Payment accepted
7. Retrieve the three most recent processed transactions
   as a separate list.
8. Print the original transactions.
9. Print the processed transactions.
10. Print the three most recent transactions.
11. Print the number of processed transactions.

Do not use loops.
"""

# INPUT
transactions = [100, 450, 0, 800, 250, 600]
blocked_customers = ["C002", "C005"]
customer = "C001"
new_payment = 900

# SOLUTION

processed = transactions.copy()
processed.remove(0)

if customer in blocked_customers:
    print("Customer blocked")
elif new_payment <= 0:
    print("invalid payment")
elif new_payment in processed:
    print("Duplicate payment")
else:
    processed.append(new_payment)
    print("Payment accepted")

most_recent_transactions = processed[-3:]
print(transactions)
print(processed)
print(most_recent_transactions)
print(len(processed))


# EXPECTED OUTPUT
"""
Payment accepted
[100, 450, 0, 800, 250, 600]
[100, 450, 800, 250, 600, 900]
[250, 600, 900]
6
"""
