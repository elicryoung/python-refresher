# haven't coded in a while so this is just me messing around taking notes and refreshing my memory

'''
customer_id = "C001"
merchant_id = "M005"
amount = 7500
fee_percentage = 1.5
payment_successful = True

print(customer_id, merchant_id, amount, fee_percentage, payment_successful)

= C001 M005 7500 1.5 True

'''

""" amount = 2500

if amount <= 0:
    print("Invalid Payment")
elif amount <= 999:
    print("small payment")
elif amount <= 4999:
    print("medium payment ")
elif amount >= 5000:
    print("large payment")

= medium payment  """


""" 
amount = 750
balance = 1000
verified = True
blocked = False

if blocked == True:
    print("Account Blocked")
elif amount <= 0:
    print("invalid amount")
elif verified != True:
    print('Verification Required')
elif amount > balance:
    print("insufficient funds")
else:
    print("payment approved")

= payment approved

 """
""" 
transactions = [120, 500, 50, 1200, 750, 300, 1000]

for i in transactions:
    if i > 500:
        print(i)

= 1200
750
1000 """

""" 
transactions = [120, 500, 50, 1200, 750, 300, 1000]
total = 0

for amount in transactions:
    if amount > 500:
        total += amount

print(total)
 """
""" 
transactions = [120, 500, 50, 1200, 750, 300, 1000]
count = 0

for amount in transactions:
    if amount >= 500:
        count += 1

print(count)
 """


transactions = [120, 500, 50, 1200, 750, 300, 1000]
total = 0
count500 = 0
total500 = 0 
count499 = 0

for amount in transactions:
    total += amount
    if amount >= 500:
        count500 +=1
        total500 += amount
    else:
        count499 +=1

print("Total revenue: ", + total)
print("Lage transaction count: ", + count500)
print("Large transaction total: ", + total500)
print("Small transaction count ", + count499)


    
    
