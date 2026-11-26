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
A payment processing system contains a list of transaction amounts. 
Find the smallest and largest transaction amounts.

#REQUIREMENTS

1. Use a single for loop.
2. Do not use min(), max() or sorted().
3. Store the minimum and maximum amounts separately.
4. Print the results after the loop
"""
# INPUT
"""
transactions = [120, 500, 50, 1200, 750, 300, 1000]
"""

# SOLUTION


# EXPECTED OUTPUT
"""
Minimum: 50
Maximum: 1200
"""

