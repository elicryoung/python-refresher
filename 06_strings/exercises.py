"""Strings — Python Exercises"""

# ==========================================
# EXERCISE 1 - STRING INDEXING AND SLICING
# ==========================================

# QUESTION
"""
Extract information from a transaction reference.

REQUIREMENTS:
- Print the first character.
- Print the last character.
- Extract and print the merchant ID.
- Extract and print the customer ID.
- Extract and print the transaction amount.
- Print the length of the entire string.
"""

# INPUT
transaction = "m123_c456_500"

# SOLUTION
""" 
print(transaction[0])
print(transaction[-1])
print(transaction[0:4])
print(transaction[5:9])
print(transaction[10:])
print(len(transaction))
 """
# EXPECTED OUTPUT
"""
m
0
m123
c456
500
13
"""

# ==========================================
# EXERCISE 2 - SPLITTING TRANSACTION RECORDS
# ==========================================

# QUESTION
"""
Extract individual fields from transaction records.

REQUIREMENTS:
- Loop through the transactions.
- Split each transaction using the comma separator.
- Store each field in a separate variable:
    merchant
    amount
    customer
    hour
- Print all four variables on one line for each
  transaction.
"""

# INPUT
transactions = [
    "m1,200,c1,14",
    "m22,1500,c23,9",
    "m333,75,c4,18"
]
""" 
# SOLUTION

for transaction in transactions:
    transaction = transaction.split(",")
    merchant = transaction[0]
    amount =  transaction[1]
    customer =  transaction[2]
    hour =  transaction[3]
    print(merchant, amount, customer, hour)    

 """

# EXPECTED OUTPUT
"""
m1 200 c1 14
m22 1500 c23 9
m333 75 c4 18
"""


# ==========================================
# EXERCISE 3 - CLEANING TRANSACTION RECORDS
# ==========================================

# QUESTION
"""
Clean inconsistent merchant transaction records.

REQUIREMENTS:
- Loop through each transaction.
- Split each transaction using commas.
- Extract the merchant, amount and currency.
- Remove surrounding whitespace from all three fields.
- Convert the merchant ID to lowercase.
- Convert the currency to uppercase.
- Print the three cleaned fields on one line.
"""

# INPUT
transactions = [
    "  M1  , 200 , eur ",
    " m2 , 500 , Usd ",
    " M3 , 75 , gbp "
]

# SOLUTION

""" 
for transaction in transactions:
    transaction = transaction.split(",")
    merchant = transaction[0].strip().lower()
    amount = transaction[1].strip()
    currency = transaction[2].strip().upper()
    print(merchant, amount, currency)
 """
# EXPECTED OUTPUT
"""
m1 200 EUR
m2 500 USD
m3 75 GBP
"""

# ==========================================
# EXERCISE 4 - CLEANING AND FILTERING STRINGS
# ==========================================

# QUESTION
"""
Clean transaction records and display only
transactions using EUR.

REQUIREMENTS:
- Loop through each transaction.
- Split each transaction using commas.
- Remove surrounding whitespace from each field.
- Convert merchant IDs to lowercase.
- Replace hyphens in merchant IDs with underscores.
- Remove the currency symbol from each amount.
- Convert currency codes to uppercase.
- Only print transactions using EUR.
- Print the merchant, amount and currency.
"""

# INPUT
transactions = [
    " M-1 , €200 , eur ",
    " M-2 , $500 , usd ",
    " M-3 , €150 , EUR ",
    " M-4 , £75 , gbp ",
    " M-5 , €300 , Eur "
]

# SOLUTION
""" 
for transaction in transactions:
    transaction = transaction.split(",")
    merchant = transaction[0].strip().lower().replace("-","_")
    amount = transaction[1].strip()[1:]
    currency = transaction[2].strip().upper()
    if currency == "EUR":
        print(merchant, amount, currency)
 """
# EXPECTED OUTPUT
"""
m_1 200 EUR
m_3 150 EUR
m_5 300 EUR
"""

# ==========================================
# EXERCISE 5 - PARSING AND TYPE CONVERSION
# ==========================================

# QUESTION
"""
Analyse comma-separated transaction records.

REQUIREMENTS:
- Loop through each transaction.
- Extract the merchant, amount, customer and hour.
- Convert the amount and hour to integers.
- Calculate the total value of all transactions.
- Count transactions worth 200 or more.
- Calculate the total value of transactions occurring
  between hours 12 and 17 inclusive.
- Print all three results after processing the records.
"""

# INPUT
transactions = [
    "m1,200,c1,14",
    "m2,500,c2,9",
    "m1,75,c3,12",
    "m3,300,c1,17",
    "m2,150,c4,18",
    "m1,100,c2,11"
]
""" 
# SOLUTION
total = 0
count = 0
twelve_seventeen_total = 0

for transaction in transactions:
    transaction = transaction.split(",")
    
    merchant = transaction[0]
    amount =  int(transaction[1])
    customer =  transaction[2]
    hour =  int(transaction[3])

    total += amount

    if amount >= 200:
        count += 1
    if 12 <= hour <= 17:
        twelve_seventeen_total += amount

print(total)
print(count)
print(twelve_seventeen_total)
 """

# EXPECTED OUTPUT
"""
1325
3
575
"""

# ==========================================
# EXERCISE 6 - STRING FORMATTING
# ==========================================

# QUESTION
"""
Calculate transaction fees and produce a formatted
list of results.

REQUIREMENTS:
- Loop through each transaction.
- Extract the merchant and amount.
- Convert the amount to an integer.
- Calculate a transaction fee of 3%.
- Calculate the remaining amount after the fee.
- Use an f-string to create a comma-separated record
  containing the merchant, fee and remaining amount.
- Format the fee and remaining amount to two
  decimal places.
- Append each formatted record to the results list.
- Print the results list after processing all records.
"""
""" 
# INPUT
transactions = [
    "m1,200",
    "m2,350",
    "m3,75"
]

# SOLUTION
results = []
for transaction in transactions:
    transaction = transaction.split(",")
    
    merchant = transaction[0]
    amount =  int(transaction[1])
    fee = amount*0.03

    remainder = amount- fee

    results.append(f"{merchant},{fee:.2f},{remainder:.2f}")

print(results)
 """
# EXPECTED OUTPUT
"""
['m1,6.00,194.00', 'm2,10.50,339.50', 'm3,2.25,72.75']
"""



# ==========================================
# EXERCISE 7 - JOINING TRANSACTION FIELDS
# ==========================================

# QUESTION
"""
Convert nested transaction lists into
comma-separated strings.

REQUIREMENTS:
- Create an empty results list.
- Loop through each transaction.
- Convert the amount and hour to strings.
- Use join() to combine the four fields
  into a comma-separated string.
- Append each string to the results list.
- Print the results list.
- Do not use f-strings.
"""
""" 
# INPUT
transactions = [
    ["m1", 200, "c1", 14],
    ["m2", 500, "c2", 9],
    ["m3", 75, "c3", 18]
]

# SOLUTION

results = []

for transaction in transactions:

    transaction[1] = str(transaction[1])
    transaction[3] = str(transaction[3])

    results.append(",".join(transaction))

print(results)
 """
# EXPECTED OUTPUT
"""
['m1,200,c1,14', 'm2,500,c2,9', 'm3,75,c3,18']
"""


# ==========================================
# EXERCISE 8 - TRANSACTION PROCESSING
# ==========================================

# QUESTION
"""
Create a function that processes raw transaction
records and returns a list of valid, formatted
transactions.

REQUIREMENTS:
- Define a function called process_transactions.
- Accept a list of transaction strings.
- Extract the merchant, amount, customer and hour.
- Remove surrounding whitespace from all fields.
- Convert merchant and customer IDs to lowercase.
- Convert the amount and hour to integers.

VALIDATION RULES:
- Ignore transactions with amounts of zero or less.
- Ignore transactions with hours outside 0-23.

FEE RULES:
- Amounts below 100: 5%
- Amounts from 100 to below 500: 3%
- Amounts of 500 or more: 1%

OUTPUT:
- Calculate the fee for each valid transaction.
- Format each result as:
  merchant,customer,amount,fee
- Format the fee to two decimal places.
- Return a list of formatted transaction strings.
- Call the function and print the returned list.
"""

# INPUT
transactions = [
    " M1 , 200 , C1 , 14 ",
    " M2 , 500 , C2 , 9 ",
    " M3 , -50 , C3 , 12 ",
    " M1 , 75 , C2 , 17 ",
    " M4 , 300 , C4 , 25 ",
    " M2 , 100 , C1 , 18 ",
    " M5 , 0 , C5 , 10 ",
    " M3 , 1000 , C2 , 23 "
]

# SOLUTION


def process_transactions(transactions):
    processed_transactions =[]

    for transaction in transactions:
        transaction = transaction.split(",")

        merchant = transaction[0].lower().strip()
        amount = int(transaction[1])
        customer = transaction[2].lower().strip()
        hour = int(transaction[3])

        if amount > 0 and 0 <= hour <= 23:
            if amount < 100:
                fee = amount *0.05
            elif amount < 500:
                fee = amount *0.03
            else:
                fee = amount *0.01
            processed_transactions.append(f"{merchant},{customer},{amount},{fee:.2f}")

    return(processed_transactions)

for i in process_transactions(transactions):
    print(i)

# EXPECTED OUTPUT
"""
[
    'm1,c1,200,6.00',
    'm2,c2,500,5.00',
    'm1,c2,75,3.75',
    'm2,c1,100,3.00',
    'm3,c2,1000,10.00'
]
"""
