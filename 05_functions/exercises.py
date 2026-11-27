"""Functions — Python Exercises"""

# ==========================================
# EXERCISE 1 - DEFINING AND CALLING FUNCTIONS
# ==========================================

# QUESTION
"""
Create a function that displays a payment status.

REQUIREMENTS:
- Define a function called payment_status.
- Inside the function, print "Payment processing".
- Inside the function, print "Payment complete".
- Call the function twice.
"""

# SOLUTION
""" 

def payment_status():
    print("Payment processing")
    print("Payment complete")


payment_status()
payment_status()
 """



# EXPECTED OUTPUT
"""
Payment processing
Payment complete
Payment processing
Payment complete
"""


# ==========================================
# EXERCISE 2 - PARAMETERS AND ARGUMENTS
# ==========================================

# QUESTION
"""
Create a function that calculates a transaction fee.

REQUIREMENTS:
- Define a function called calculate_fee.
- Accept two parameters: amount and fee_rate.
- Calculate the fee by multiplying them.
- Print the calculated fee.
- Call the function using each pair of inputs below.
"""

# INPUT
"""
Amount: 200, Fee rate: 0.05
Amount: 500, Fee rate: 0.02
Amount: 100, Fee rate: 0.03
"""

# SOLUTION
""" 
def calculate_fee(amount, fee_rate):
    fee = amount * fee_rate
    print(fee)
    

calculate_fee(200, 0.05)
calculate_fee(500, 0.02)
calculate_fee(100, 0.03)


 """

# EXPECTED OUTPUT
"""
10.0
10.0
3.0
"""


# ==========================================
# EXERCISE 3 - RETURNING VALUES
# ==========================================

# QUESTION
"""
Create a function that calculates a transaction fee
and use its returned values to calculate a total.

REQUIREMENTS:
- Define a function called calculate_fee.
- Accept two parameters: amount and fee_rate.
- Calculate and return the transaction fee.
- Do not print anything inside the function.
- Call the function for each transaction below.
- Store each returned fee in a separate variable.
- Calculate and print the total of all three fees.
"""

# INPUT
"""
Transaction 1: 200, 0.05
Transaction 2: 500, 0.02
Transaction 3: 100, 0.03
"""

# SOLUTION
""" 
def calculate_fee(amount, fee_rate):
    fee = amount * fee_rate
    return fee

transation_1 = calculate_fee(200, 0.05)
transation_2 = calculate_fee(500, 0.02)
transation_3 = calculate_fee(100, 0.03)

print(transation_1 + transation_2 + transation_3)

 """
# EXPECTED OUTPUT
"""
23.0
"""

# ==========================================
# EXERCISE 5 - FUNCTIONS WITH CONDITIONS
# ==========================================

# QUESTION
"""
Create a function that calculates a transaction fee
based on the transaction amount.

REQUIREMENTS:
- Define a function called calculate_fee.
- Accept one parameter: amount.
- If the amount is less than 100, charge a 5% fee.
- If the amount is between 100 and 499 inclusive,
  charge a 3% fee.
- If the amount is 500 or greater, charge a 1% fee.
- Return the calculated fee.
- Call the function for each amount below.
- Print each returned fee.
"""

# INPUT
amounts = [50, 100, 200, 500, 1000]

# SOLUTION
""" 

def calculate_fee(amount):
    if amount < 100:
        fee = amount * 0.05
        return fee
    elif amount <500:
        fee = amount * 0.03
        return fee
    else:
        fee = amount * 0.01
        return fee


for amount in amounts:
    print(calculate_fee(amount))

 """
# EXPECTED OUTPUT
"""
2.5
3.0
6.0
5.0
10.0
"""


# ==========================================
# EXERCISE 6 - FUNCTIONS WITH LOOPS AND LISTS
# ==========================================

# QUESTION
"""
Create a function that calculates the total value
of transactions meeting a minimum threshold.

REQUIREMENTS:
- Define a function called calculate_total.
- Accept two parameters: amounts and minimum.
- Only include amounts greater than or equal
  to the minimum.
- Return the total of qualifying transactions.
- Call the function with a minimum of 100.
- Call the function again with a minimum of 200.
- Print both returned results.
"""
""" 
# INPUT
amounts = [50, 100, 200, 75, 300, 150]

# SOLUTION
def calculate_total(amounts, minimum):
    total = 0

    for amount in amounts:
        if amount >= minimum:
            total += amount

    return total

total = calculate_total(amounts, 100)
print(total)

total = calculate_total(amounts, 200)
print(total)
 """
# EXPECTED OUTPUT
"""
750
500
"""

# ==========================================
# EXERCISE 7 - MERCHANT TRANSACTION ANALYSIS
# ==========================================

# QUESTION
"""
Analyse a merchant's transactions using three functions.

REQUIREMENTS:
- Create a function called calculate_total that returns
  the total value of all transactions.

- Create a function called count_large that returns
  the number of transactions worth 200 or more.

- Create a function called calculate_fees that returns
  the combined fees for all transactions.

FEE RULES:
- Below 100: 5%
- From 100 to below 500: 3%
- 500 or above: 1%

Call all three functions and print their results.
"""

# INPUT
amounts = [50, 100, 250, 500, 75, 300, 1000]

# SOLUTION


def calculate_total(transactions):
    total = 0
    for transaction in transactions:
        total += transaction
    return total

def count_large(transactions):
    count = 0 
    for transaction in transactions:
        if transaction >= 200:
            count += 1
    return count

def calculate_fees(transactions):
    total_fees = 0
    for transaction in transactions:
        if transaction < 100:
            fee = transaction * 0.05
            total_fees += fee
        elif transaction < 500:
            fee = transaction * 0.03
            total_fees += fee
        else:
            fee = transaction *0.01
            total_fees += fee
    return total_fees

total = calculate_total(amounts)
print(total)

large = count_large(amounts)
print(large)

fees = calculate_fees(amounts)
print(fees)
        





# EXPECTED OUTPUT
"""
2275
4
40.75
"""