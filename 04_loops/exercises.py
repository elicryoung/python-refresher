"""
PYTHON LOOPS — EXERCISES

Try each exercise independently before reading its solution.
Remove the triple quotes around a solution to execute it.
Restore the triple quotes before moving to the next exercise.
"""


# ============================================================
# EXERCISE 04.01 — FILTERING TRANSACTIONS
# ============================================================

# QUESTION
"""
Print every transaction strictly greater than 500.
"""
# INPUT
"""
transactions = [120, 500, 50, 1200, 750, 300, 1000]
"""



# SOLUTION

"""
transactions = [120, 500, 50, 1200, 750, 300, 1000]

for amount in transactions:
    if amount > 500:
        print(amount)
"""
# EXPLANATION
"""
The loop visits every transaction.
The condition determines whether it is printed.
Strictly greater than means >, not >=.
"""
# EXPECTED OUTPUT
"""
1200
750
1000
"""
# ============================================================
# EXERCISE 04.02 — RUNNING TOTALS
# ============================================================

# QUESTION
"""
Calculate the combined value of all transactions
strictly greater than 500.

Use a for loop and a conditional statement.
Do not use sum().
"""
# INPUT
"""
transactions = [120, 500, 50, 1200, 750, 300, 1000]
"""
# SOLUTION

"""
transactions = [120, 500, 50, 1200, 750, 300, 1000]
total = 0

for amount in transactions:
    if amount > 500:
        total += amount

print(total)
"""
# EXPLANATION
"""
Initialise the total before entering the loop.
Add each matching amount to the running total.
Print the final result outside the loop.
"""
# EXPECTED OUTPUT
"""
2950
"""
# ============================================================
# EXERCISE 04.03 — COUNTING OCCURRENCES
# ============================================================

# QUESTION
"""
Count the number of transactions greater than or
equal to 500.
"""
# INPUT
"""
transactions = [120, 500, 50, 1200, 750, 300, 1000]
"""
# SOLUTION

"""
transactions = [120, 500, 50, 1200, 750, 300, 1000]
count = 0

for amount in transactions:
    if amount >= 500:
        count += 1

print(count)
"""
# EXPLANATION
"""
Initialise the counter before the loop.
Increase it by one for each matching transaction.
Use += 1 to count items, rather than += amount,
which would calculate their combined value.
"""
# EXPECTED OUTPUT
"""
4
"""
# ============================================================
# EXERCISE 04.04 — MULTIPLE CALCULATIONS
# ============================================================

# QUESTION
"""
Using one for loop, calculate:

1. Total revenue from all transactions.
2. Number of transactions worth 500 or more.
3. Combined value of transactions worth 500 or more.
4. Number of transactions below 500.

Do not use sum() or len().
"""
# INPUT
"""
transactions = [120, 500, 50, 1200, 750, 300, 1000]
"""
# SOLUTION

"""
transactions = [120, 500, 50, 1200, 750, 300, 1000]

total_revenue = 0
large_count = 0
large_total = 0
small_count = 0

for amount in transactions:
    total_revenue += amount

    if amount >= 500:
        large_count += 1
        large_total += amount
    else:
        small_count += 1

print("Total revenue:", total_revenue)
print("Large transaction count:", large_count)
print("Large transaction total:", large_total)
print("Small transaction count:", small_count)
"""
# EXPLANATION
"""
Initialise all counters and totals before the loop.
Total revenue updates for every transaction.
Large transactions update both their count and total.
Remaining transactions update the small transaction count.
There is no need to check amount < 500 again in else.
Multiple calculations can be performed in one loop.
"""
# EXPECTED OUTPUT
"""
Total revenue: 3920
Large transaction count: 4
Large transaction total: 3450
Small transaction count: 3
"""


# ============================================================
# EXERCISE 04.05 — MINIMUM AND MAXIMUM
# ============================================================

# QUESTION
"""
A payment processing system contains a list of transaction
amounts.

# REQUIREMENTS

1. Find the smallest transaction amount.
2. Find the largest transaction amount.
3. Use a single for loop.
4. Store the minimum and maximum separately.
5. Print the results after the loop.

Do not use min(), max() or sorted().
Assume the list is not empty.
"""
""" 
# INPUT
transactions = [120, 500, 50, 1200, 750, 300, 1000]

# SOLUTION
smallest_transaction = transactions[0]
largest_transaction = transactions[0]

for amount in transactions:
    if amount < smallest_transaction:
        smallest_transaction = amount
    if amount > largest_transaction:
        largest_transaction = amount

print("max: ", largest_transaction)
print("min: ", smallest_transaction)

 """
# EXPECTED OUTPUT
"""
Minimum: 50
Maximum: 1200
"""

# ============================================================
# EXERCISE 04.06 — TRANSACTION CLASSIFICATION
# ============================================================

# QUESTION
"""
A payment platform needs to separate transactions
into three categories.

# REQUIREMENTS

1. Transactions of zero or less are invalid.
2. Transactions between 1 and 499 are small.
3. Transactions of 500 or more are large.
4. Store each category in a separate list.
5. Print all three lists.
6. Print the number of transactions in each category.
7. Preserve the original transaction list.

Use a single for loop.
"""
""" 
# INPUT
transactions = [120, 500, -50, 1200, 0, 750, 300, 1000]

# SOLUTION
invalid = []
small = []
large = []

for amount in transactions:
    if amount <= 0:
        invalid.append(amount)
    elif amount < 500:
        small.append(amount)
    else:
        large.append(amount)

print(invalid)
print(small)
print(large)

print(len(invalid))
print(len(small))
print(len(large))

 """

# EXPECTED OUTPUT
"""
Invalid: [-50, 0]
Small: [120, 300]
Large: [500, 1200, 750, 1000]
Invalid count: 2
Small count: 2
Large count: 4
"""


# ============================================================
# EXERCISE 04.07 — GENERATING NUMBERS
# ============================================================

# QUESTION
"""
Use for loops and range() to generate sequences of numbers.

# REQUIREMENTS

1. Print numbers from 1 to 5 inclusive.
2. Print even numbers from 2 to 10 inclusive.
3. Print numbers from 5 down to 1 inclusive.
4. Calculate the total of all integers from 1 to 10
   inclusive and print the result.

Use range() for every requirement.
Do not use sum().
"""
""" 
# INPUT
# No input required.

# SOLUTION
for number in range(1,6):
    print(number)

for number in range(2,11,2):
    print(number)

for number in range(5,0,-1):
    print(number)

total = 0 
for number in range(11):
    total += number

print(total)
 """
# EXPECTED OUTPUT
"""
1
2
3
4
5
2
4
6
8
10
5
4
3
2
1
55
"""


# ============================================================
# EXERCISE 04.08 — CORRECTING TRANSACTION AMOUNTS
# ============================================================

# QUESTION
"""
A payment platform needs to correct its existing
transaction amounts.

# REQUIREMENTS

1. Replace any negative transaction with 0.
2. Increase transactions between 1 and 499 by 50.
3. Reduce transactions of 500 or more by 100.
4. Leave transactions of exactly 0 unchanged.
5. Print the updated transaction list.

Use a single for loop with range() and len().
Modify the original list directly.
Do not create a new list.
"""
""" 
# INPUT
transactions = [120, 500, -50, 1200, 0, 750, 300]

# SOLUTION

for i in range(len(transactions)):
    amount = transactions[i]
    if amount < 0:
        transactions[i] = 0
    elif amount > 0 and amount < 500:
        transactions[i] += 50
    elif amount >= 500:
        transactions[i] -= 100

    
print(transactions)
 """
# EXPECTED OUTPUT
"""
[170, 400, 0, 1100, 0, 650, 350]
"""



# ============================================================
# EXERCISE 04.09 — APPLYING TRANSACTION FEES
# ============================================================

# QUESTION
"""
A payment platform applies fees to existing transactions.

# REQUIREMENTS

1. Negative transactions must remain unchanged.
2. Transactions of exactly 0 must remain unchanged.
3. Transactions between 1 and 499 incur a fee of 10.
4. Transactions between 500 and 999 incur a fee of 25.
5. Transactions of 1000 or more incur a fee of 50.
6. Subtract the applicable fee from each transaction.
7. Calculate the total fees collected.
8. Print the updated transactions and total fees.

Use a single for loop.
Modify the original list directly.
Do not create a new list.
"""
""" 
# INPUT
transactions = [100, 500, -50, 1200, 0, 750, 300, 1000]

# SOLUTION
total_fees = 0

for i in range(len(transactions)):
    amount = transactions[i]

    if amount <= 0:
        pass
    elif amount < 500:
        transactions[i] -= 10
        total_fees += 10
    elif amount < 1000:
        transactions[i] -= 25
        total_fees += 25
    else:
        transactions[i] -= 50
        total_fees += 50

print(transactions)
print(total_fees)
 """
# EXPECTED OUTPUT
"""
[90, 475, -50, 1150, 0, 725, 290, 950]
170
"""


# ============================================================
# EXERCISE 04.10 — SUBSCRIPTION PAYMENTS
# ============================================================

# QUESTION
"""
A customer has a prepaid account balance.
A subscription payment is deducted every month.

# REQUIREMENTS

1. Deduct the subscription cost while the customer
   has enough money to pay.
2. Count how many successful payments are made.
3. Calculate the total amount paid.
4. Print the number of successful payments.
5. Print the total amount paid.
6. Print the remaining balance.

Use a while loop.
The balance must never become negative.
"""
""" 
# INPUT
balance = 550
subscription_cost = 100

# SOLUTION

count = 0
total = 0

while balance >= subscription_cost:
    balance -= subscription_cost
    count +=1
    total += subscription_cost

print(count)
print(total)

print(balance) """

# EXPECTED OUTPUT
"""
5
500
50
"""

# ============================================================
# EXERCISE 04.11 — REACHING A SAVINGS TARGET
# ============================================================

# QUESTION
"""
A merchant deposits a fixed amount into a savings
account every month until a target is reached.

# REQUIREMENTS

1. Deposit the monthly amount until the balance
   reaches or exceeds the savings target.
2. Count the number of deposits made.
3. Calculate the total amount deposited.
4. Print the number of deposits.
5. Print the total amount deposited.
6. Print the final balance.
7. Print the amount by which the balance exceeds
   the target.

Use a while loop.
"""

""" # INPUT
balance = 200
monthly_deposit = 150
target = 1000

# SOLUTION
count = 0 
total = 0 
while balance < target:
    balance += monthly_deposit
    count +=1
    total += monthly_deposit

print(count)
print(total)
print(balance)
print(balance - target)
 """
# EXPECTED OUTPUT
"""
6
900
1100
100
"""

# ============================================================
# EXERCISE 04.12 — SUSPICIOUS TRANSACTION DETECTION
# ============================================================

# QUESTION
"""
A payment platform checks transactions for suspicious
activity.

# REQUIREMENTS

1. Process transactions in their original order.
2. Count every transaction checked.
3. A transaction of 1000 or more is suspicious.
4. When the first suspicious transaction is found,
   print its amount and stop checking transactions.
5. Print the total number of transactions checked,
   including the suspicious transaction.

Use a for loop and break.
"""
""" 
# INPUT
transactions = [120, 450, 800, 1000, 750, 1500, 300]

# SOLUTION

count = 0 

for amount in transactions:
    count +=1
    if amount >= 1000:
        print(amount)
        break
    
print(count)

 """
# EXPECTED OUTPUT
"""
1000
4
"""

# ============================================================
# EXERCISE 04.13 — SKIPPING INVALID TRANSACTIONS
# ============================================================

# QUESTION
"""
A payment platform needs to process valid transactions
while ignoring invalid transactions.

# REQUIREMENTS

1. Transactions of zero or less are invalid.
2. Count invalid transactions and skip them using continue.
3. Count valid transactions.
4. Calculate the total value of valid transactions.
5. Store valid transactions worth 500 or more
   in a separate list.
6. Print the invalid transaction count.
7. Print the valid transaction count.
8. Print the total valid transaction value.
9. Print the list of large valid transactions.

Use a single for loop and continue.
Preserve the original transaction list.
"""

# INPUT
transactions = [100, -50, 500, 0, 750, 200, -100, 1200]

# SOLUTION


# EXPECTED OUTPUT
"""
3
5
2750
[500, 750, 1200]
"""


# ============================================================
# EXERCISE 04.13 — SKIPPING INVALID TRANSACTIONS
# ============================================================

# QUESTION
"""
A payment platform needs to process valid transactions
while ignoring invalid transactions.

# REQUIREMENTS

1. Transactions of zero or less are invalid.
2. Count invalid transactions and skip them using continue.
3. Count valid transactions.
4. Calculate the total value of valid transactions.
5. Store valid transactions worth 500 or more
   in a separate list.
6. Print the invalid transaction count.
7. Print the valid transaction count.
8. Print the total valid transaction value.
9. Print the list of large valid transactions.

Use a single for loop and continue.
Preserve the original transaction list.
"""
""" 
# INPUT
transactions = [100, -50, 500, 0, 750, 200, -100, 1200]

# SOLUTION
count_invalid = 0
count_valid = 0 
total_valid = 0 
large_transactions = []

for amount in transactions:
    if amount <= 0:
        count_invalid +=1
        continue
    count_valid += 1
    total_valid += amount
    if amount >= 500:
        large_transactions.append(amount)

print(count_invalid)
print(count_valid)
print(total_valid)
print(large_transactions)
 """
# EXPECTED OUTPUT
"""
3
5
2750
[500, 750, 1200]
"""

# ============================================================
# EXERCISE 04.14 — MATCHING MERCHANT TRANSACTIONS
# ============================================================

# QUESTION
"""
A payment platform stores merchant IDs separately
from its transaction records.

Each transaction contains a merchant ID and an amount.

# REQUIREMENTS

1. Process each merchant in the merchants list.
2. Find all transactions belonging to that merchant.
3. Calculate the merchant's total transaction value.
4. Print each merchant ID and its total.
5. Merchants with no transactions should have a total of 0.

Use nested for loops.
"""
""" 
# INPUT
merchants = ["M001", "M002", "M003", "M004"]

transactions = [
    ["M001", 100],
    ["M002", 750],
    ["M001", 300],
    ["M003", 500],
    ["M002", 200],
    ["M001", 600]
]

# SOLUTION
for merchant in merchants:
    merchant_total = 0
    for transaction in transactions:
        if merchant == transaction[0]:
            merchant_total += transaction[1]
    print(merchant, merchant_total)
 """
# EXPECTED OUTPUT
"""
M001 1000
M002 950
M003 500
M004 0
"""
# ============================================================
# EXERCISE 04.15 — TRANSACTION ANALYSIS
# ============================================================

# QUESTION
"""
A payment platform wants to analyse transactions
relative to the average transaction amount.

# REQUIREMENTS

1. Calculate the total transaction value.
2. Calculate the average transaction amount.
3. Store all transactions above the average in
   a separate list.
4. Count transactions below the average.
5. Calculate the combined value of transactions
   above the average.
6. Print the total transaction value.
7. Print the average.
8. Print the above-average transactions.
9. Print the below-average count.
10. Print the above-average total.

Use two separate for loops.
Do not use sum().
Preserve the original list.
"""
""" 
# INPUT
transactions = [100, 500, 200, 900, 300, 400]

# SOLUTION

total = 0

for transaction in transactions:
    total += transaction

average = total / len(transactions)

above_average = []
above_average_total = 0
below_average_count = 0
for transaction in transactions:
    if transaction > average:
        above_average.append(transaction)
        above_average_total += transaction
    elif transaction < average:
        below_average_count += 1

print(total)
print(average)
print(above_average)
print(below_average_count)
print(above_average_total)
 """
# EXPECTED OUTPUT
"""
2400
400.0
[500, 900]
3
1400
"""


# ============================================================
# EXERCISE 04.16 — MERCHANT PERFORMANCE ANALYSIS
# ============================================================

# QUESTION
"""
A payment platform wants to analyse merchant performance.

Each transaction record contains a merchant ID
and a transaction amount.

# REQUIREMENTS

1. Ignore transactions with amounts of zero or less.

2. Calculate the combined value of all valid transactions.

3. Calculate the average value of all valid transactions.

4. For each merchant, calculate:
   - Total value of their valid transactions.
   - Number of their valid transactions.
   - Number of their transactions above the overall average.

5. Store merchant IDs whose total transaction value
   is at least 1000 in a separate list.

6. Print the overall total and average.

7. Print each merchant ID, total, transaction count
   and above-average count.

8. Print the list of merchants whose total is
   at least 1000.

Preserve the original input lists.
Do not use sum().
"""

# INPUT
merchants = ["M001", "M002", "M003", "M004"]

transactions = [
    ["M001", 200],
    ["M002", 800],
    ["M001", 500],
    ["M003", -100],
    ["M002", 400],
    ["M001", 700],
    ["M003", 400],
    ["M002", 0]
]

# SOLUTION
total_valid = 0
total_count = 0

for transaction in transactions:
    if transaction[1] > 0:
        total_valid += transaction[1]
        total_count += 1

average = total_valid / total_count

print(total_valid)
print(average)

merchants_over_1000 = []

for merchant in merchants:
    merchant_total = 0
    merchant_valid_count = 0
    above_average = 0
   
    for trans in transactions:

        if trans[0] == merchant:
            if trans[1] > 0:
                merchant_total += trans[1]
                merchant_valid_count += 1
            if trans[1] > average:
                above_average += 1

    if merchant_total >= 1000:
        merchants_over_1000.append(merchant)

    print(merchant, merchant_total, merchant_valid_count, above_average)

print(merchants_over_1000)


# EXPECTED OUTPUT
"""
3000
500.0
M001 1400 3 1
M002 1200 2 1
M003 400 1 0
M004 0 0 0
['M001', 'M002']
"""
