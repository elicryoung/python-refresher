"""Dictionaries — Python Exercises"""

# ========================================== 
# EXERCISE 1 - CREATING DICTIONARIES
# ==========================================

# QUESTION
"""
Create a dictionary containing merchant balances.

REQUIREMENTS:
- Create a dictionary called balances.
- Store merchant IDs as keys.
- Store balances as integer values.
- Print the balance of m2.
- Print the balance of m4.
- Print the combined balance of m1 and m3.
- Print the number of merchants.
"""

# INPUT
"""
m1: 500
m2: 1200
m3: 750
m4: 300
"""

# SOLUTION
""" 
balances = {

    'm1': 500,
    'm2': 1200,
    'm3': 750,
    'm4': 300

}

print(balances["m2"])
print(balances["m4"])
print(balances["m1"] + balances["m3"])
print(len(balances))

# EXPECTED OUTPUT

1200
300
1250
4
"""


# ==========================================
# EXERCISE 2 - ADDING AND UPDATING ENTRIES
# ==========================================

# QUESTION
"""
Update merchant balances following several events.

REQUIREMENTS:
- Add merchant m4 with a balance of 600.
- Increase m1's balance by 200.
- Decrease m2's balance by 350.
- Double m3's balance.
- Replace m4's balance with 900.
- Print the final dictionary.
- Print the combined balance of all four merchants.
"""

# INPUT
balances = {
    "m1": 500,
    "m2": 1200,
    "m3": 750
}

# SOLUTION
""" 
balances["m4"] = 600
balances["m1"] += 200
balances["m2"] -= 350
balances["m3"] *= 2
balances["m4"] = 900

print(balances)
total = 0 

for key in balances:
    total += balances[key]
    
print(total)
 """
# EXPECTED OUTPUT
"""
{'m1': 700, 'm2': 850, 'm3': 1500, 'm4': 900}
3950
"""

# ==========================================
# EXERCISE 3 - CHECKING AND REMOVING KEYS
# ==========================================

# QUESTION
"""
Manage a dictionary of merchant balances.

REQUIREMENTS:
- If m2 exists, increase its balance by 100.
- If m4 does not exist, add it with a balance of 500.
- If m3 exists, remove it using pop() and print
  its removed balance.
- Print the final dictionary.
- Calculate and print the combined remaining balance
  using a loop.
"""

# INPUT
balances = {
    "m1": 500,
    "m2": 1200,
    "m3": 750
}

# SOLUTION

""" 
if "m2" in balances:
    balances["m2"] += 100
else:
    print("no m2 in balances")

if "m4" not in balances:
    balances["m4"] = 500
else:
    print("m4 in balances")

if "m3" in balances:
    print(balances.pop("m3"))

else:
    print("no m3 in abalnces")

print(balances)

total = 0
for key in balances:
    total += balances[key]

print(total)
    
 """

# EXPECTED OUTPUT
"""
750
{'m1': 500, 'm2': 1300, 'm4': 500}
2300
"""

# ==========================================
# EXERCISE 4 - GET AND MISSING KEYS
# ==========================================

# QUESTION
"""
Retrieve merchant balances safely.

REQUIREMENTS:
- Loop through requested_merchants.
- Retrieve each merchant's balance using get().
- Use 0 as the default for missing merchants.
- Print each merchant ID and its balance.
- Calculate and print the combined balance
  of all requested merchants.
- Do not modify the dictionary.
- Do not use if statements.
"""

""" # INPUT
balances = {
    "m1": 500,
    "m2": 1200,
    "m3": 750
}

requested_merchants = ["m1", "m4", "m2", "m5", "m3"]

# SOLUTION

total = 0
for request in requested_merchants:
    amount = balances.get(request, 0)
    print(request, amount)
    total += amount

print(total)
 """

# EXPECTED OUTPUT
"""
m1 500
m4 0
m2 1200
m5 0
m3 750
2450
"""

# ==========================================
# EXERCISE 5 - KEYS, VALUES AND ITEMS
# ==========================================

# QUESTION
"""
Analyse merchant balances using dictionary methods.

REQUIREMENTS:
- Use keys() to print every merchant ID.
- Use values() to calculate and print the total balance.
- Use items() to print the ID and balance of every
  merchant with a balance of 1000 or more.
"""

# INPUT
balances = {
    "m1": 500,
    "m2": 1200,
    "m3": 750,
    "m4": 1500,
    "m5": 1000
}

# SOLUTION

""" 
for key in balances.keys():
    print(key)

total = 0
for value in balances.values():
    total += value

for key, value in balances.items():
    if value >= 1000:
        print(key, value)
 """

# EXPECTED OUTPUT
"""
m1
m2
m3
m4
m5
4950
m2 1200
m4 1500
m5 1000
"""

# ==========================================
# EXERCISE 6 - COUNTING OCCURRENCES
# ==========================================

# QUESTION
"""
Count how many transactions each customer makes.

REQUIREMENTS:
- Create an empty dictionary called counts.
- Loop through the transaction records.
- Extract the customer ID from each record.
- Count how many transactions each customer makes.
- Use get() to handle customers not yet in the
  dictionary.
- Print the completed dictionary.
- Print the ID and transaction count of customers
  who made three or more transactions.
"""

# INPUT
transactions = [
    "m1,200,c1",
    "m2,500,c2",
    "m1,150,c1",
    "m3,75,c3",
    "m2,300,c2",
    "m1,400,c1",
    "m3,100,c2",
    "m2,250,c4"
]

# SOLUTION


counts = {}
customers = []

for transaction in transactions:
    transaction = transaction.split(",")
    customers.append(transaction[2])

for customer in customers:
    counts[customer] = counts.get(customer, 0) + 1

for value in counts:
    if value[1] >= 3:
        print(value)

print(counts)







# EXPECTED OUTPUT
"""
{'c1': 3, 'c2': 3, 'c3': 1, 'c4': 1}
c1 3
c2 3
"""