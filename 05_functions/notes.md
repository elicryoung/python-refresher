# Module 05 — Functions

## 1. What is a Function?

A function is a reusable block of code that performs a specific task.

Functions help:
- Avoid repeating code.
- Break problems into smaller tasks.
- Improve readability.
- Make code easier to test and debug.

## 2. Defining and Calling Functions

Syntax:

```python
def function_name():
    # Code to execute

function_name()
```

- def: defines a function.
- function_name: the name of the function.
- (): contains parameters.
- Indentation: identifies the function body.
- Calling the function executes its body.

Example:

```python
def payment_status():
    print("Payment complete")

payment_status()
payment_status()
```

Output:

```text
Payment complete
Payment complete
```

Defining a function does not execute it.

## 3. Parameters and Arguments

A parameter is a variable declared in a function definition.

An argument is the actual value supplied when calling the function.

Syntax:

```python
def function_name(parameter):
    print(parameter)

function_name(argument)
```

Example:

```python
def display_merchant(merchant):
    print(merchant)

display_merchant("m1")
display_merchant("m2")
```

Output:

```text
m1
m2
```

merchant is the parameter.
"m1" and "m2" are arguments.

## 4. Multiple Parameters

Separate parameters and arguments using commas.

```python
def calculate_fee(amount, fee_rate):
    fee = amount * fee_rate
    print(fee)

calculate_fee(200, 0.05)
calculate_fee(500, 0.02)
```

Output:

```text
10.0
10.0
```

Positional arguments are assigned to parameters in order.

Arguments can be integers, floats, strings, lists,
dictionaries and other Python objects.

## 5. Returning Values

return sends a value back to wherever the function
was called.

Syntax:

```python
def function_name(parameter):
    result = parameter * 2
    return result

answer = function_name(10)
print(answer)
```

Output:

```text
20
```

Returned values can be:
- Stored in variables.
- Used in calculations.
- Passed into other functions.
- Printed.
- Returned from another function.

Example:

```python
def calculate_fee(amount, fee_rate):
    return amount * fee_rate

fee1 = calculate_fee(200, 0.05)
fee2 = calculate_fee(500, 0.02)
fee3 = calculate_fee(100, 0.03)

print(fee1 + fee2 + fee3)
```

Output:

```text
23.0
```

## 6. Print vs Return

print() displays a value.
return sends a value back to the caller.

Using print:

```python
def double(number):
    print(number * 2)

result = double(5)
print(result)
```

Output:

```text
10
None
```

Using return:

```python
def double(number):
    return number * 2

result = double(5)
print(result)
```

Output:

```text
10
```

| print() | return |
|---|---|
| Displays information | Returns a usable value |
| Does not end the function | Immediately ends the function |
| Useful for debugging | Useful for calculations |
| Returns None | Returns the specified value |

If a function finishes without an explicit return
value, Python returns None.

IMPORTANT:
HackerRank often checks returned values rather than
printed output. Always follow the requirements.

## 7. Using Returned Values

A returned value can become an argument in another
function call.

```python
def calculate_balance(balance, payment):
    return balance - payment

balance = calculate_balance(500, 150)
balance = calculate_balance(balance, 100)

print(balance)
```

Output:

```text
250
```

A function call can also be placed directly inside print.

```python
print(calculate_balance(500, 150))
```

Output:

```text
350
```

## 8. Local Variables and Scope

Scope determines where a variable can be accessed.

Variables created inside a function are local to
that function.

```python
def calculate_fee(amount):
    fee = amount * 0.05
    return fee

result = calculate_fee(200)

print(result)
print(fee)
```

Output:

```text
10.0
NameError: name 'fee' is not defined
```

amount and fee are local variables.
result exists outside the function.

Returning a value does not make the original local
variable accessible outside the function.

## 9. Local vs Global Variables

```python
amount = 100

def calculate_payment(amount):
    amount += 50
    return amount

result = calculate_payment(200)

print(amount)
print(result)
```

Output:

```text
100
250
```

The parameter amount is local to the function.

It is separate from the variable amount defined
outside the function.

Prefer passing values as arguments and returning results
rather than relying on global variables.

## 10. Functions with Conditions

Functions can contain if, elif and else statements.

```python
def payment_status(amount):
    if amount >= 1000:
        return "Review required"
    else:
        return "Approved"

print(payment_status(1500))
print(payment_status(200))
```

Output:

```text
Review required
Approved
```

## 11. Multiple Return Statements

A function can contain multiple return statements.

However, only the first return reached will execute.

return immediately ends the function.

```python
def payment_status(amount):
    if amount >= 1000:
        return "Review required"

    return "Approved"
```

An else statement is not always necessary when the
previous condition returns a value.

## 12. Condition Order and Boundary Conditions

Python evaluates if and elif conditions from top
to bottom.

Incorrect:

```python
def calculate_fee(amount):
    if amount < 100:
        return amount * 0.05
    elif amount >= 100:
        return amount * 0.03
    elif amount >= 500:
        return amount * 0.01
```

The final condition is unreachable because every amount
greater than or equal to 500 also satisfies amount >= 100.

Correct:

```python
def calculate_fee(amount):
    if amount < 100:
        return amount * 0.05
    elif amount < 500:
        return amount * 0.03
    else:
        return amount * 0.01
```

Example results:

| Amount | Fee |
|---|---|
| 50 | 2.5 |
| 100 | 3.0 |
| 200 | 6.0 |
| 500 | 5.0 |
| 1000 | 10.0 |

Always test values exactly on each boundary.

For this example:
- 99
- 100
- 499
- 500

## 13. Avoiding Redundant Conditions

Unnecessary:

```python
if amount < 100:
    return amount * 0.05
elif amount >= 100 and amount < 500:
    return amount * 0.03
else:
    return amount * 0.01
```

Cleaner:

```python
if amount < 100:
    return amount * 0.05
elif amount < 500:
    return amount * 0.03
else:
    return amount * 0.01
```

Reaching the elif already means that the first
condition was false.

Therefore, amount >= 100 does not need to be checked again.

## 14. Functions with Lists and Loops

Functions can accept an entire list as an argument.

```python
def calculate_total(amounts):
    total = 0

    for amount in amounts:
        total += amount

    return total

payments = [100, 200, 300]

print(calculate_total(payments))
```

Output:

```text
600
```

Initialise the running total before the loop.

Return the result after the loop finishes.

## 15. Functions with Lists and Conditions

```python
def calculate_total(amounts, minimum):
    total = 0

    for amount in amounts:
        if amount >= minimum:
            total += amount

    return total

amounts = [50, 100, 200, 75, 300, 150]

print(calculate_total(amounts, 100))
print(calculate_total(amounts, 200))
```

Output:

```text
750
500
```

This combines:
- Multiple parameters.
- Lists.
- Loops.
- Conditions.
- Running totals.
- Return values.

## 16. Returning Too Early

Incorrect:

```python
def calculate_total(amounts):
    total = 0

    for amount in amounts:
        total += amount
        return total

print(calculate_total([100, 200, 300]))
```

Output:

```text
100
```

The return statement ends the function during the
first loop iteration.

Correct:

```python
def calculate_total(amounts):
    total = 0

    for amount in amounts:
        total += amount

    return total
```

Output for the same input:

```text
600
```

Check whether the return statement should execute during
the loop or after every element has been processed.

## 17. Counting Using Functions

```python
def count_large(transactions):
    count = 0

    for transaction in transactions:
        if transaction >= 200:
            count += 1

    return count

amounts = [50, 100, 250, 500, 75, 300, 1000]

print(count_large(amounts))
```

Output:

```text
4
```

Counters and running totals are usually initialised
inside the function so each call starts from zero.

## 18. Avoiding Repeated Code

Repetitive:

```python
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
            fee = transaction * 0.01
            total_fees += fee

    return total_fees
```

Cleaner:

```python
def calculate_fees(transactions):
    total_fees = 0

    for transaction in transactions:
        if transaction < 100:
            fee = transaction * 0.05
        elif transaction < 500:
            fee = transaction * 0.03
        else:
            fee = transaction * 0.01

        total_fees += fee

    return total_fees
```

Both versions are correct.

If every branch performs the same operation, consider
moving that operation outside the conditional block.

## 19. Calling Functions from Other Functions

Functions can reuse other functions.

```python
def calculate_fee(amount):
    if amount < 100:
        return amount * 0.05
    elif amount < 500:
        return amount * 0.03
    else:
        return amount * 0.01


def calculate_fees(transactions):
    total_fees = 0

    for transaction in transactions:
        total_fees += calculate_fee(transaction)

    return total_fees


amounts = [50, 100, 250, 500, 75, 300, 1000]

print(calculate_fees(amounts))
```

Output:

```text
40.75
```

This separates calculating an individual fee from
calculating the combined fees.

## 20. Combined Practical Example

```python
amounts = [50, 100, 250, 500, 75, 300, 1000]


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
        elif transaction < 500:
            fee = transaction * 0.03
        else:
            fee = transaction * 0.01

        total_fees += fee

    return total_fees


print(calculate_total(amounts))
print(count_large(amounts))
print(calculate_fees(amounts))
```

Output:

```text
2275
4
40.75
```

Each function has one clear responsibility.

## 21. Common Mistakes

1. Defining a function without calling it.
2. Forgetting parentheses when calling a function.
3. Forgetting the colon after the function definition.
4. Supplying the wrong number of arguments.
5. Supplying arguments in the wrong order.
6. Printing when the requirements specify returning.
7. Forgetting a return statement.
8. Returning prematurely from inside a loop.
9. Accessing local variables outside their function.
10. Placing broader conditions before specific conditions.
11. Repeating unnecessary conditions.
12. Repeating operations across conditional branches.
13. Initialising counters inside loops incorrectly.
14. Forgetting inclusive and exclusive boundaries.
15. Ignoring the requested function name or parameters.

## 22. Function Problem-Solving Checklist

Before implementing:

1. What is the function supposed to accomplish?
2. What information does it receive?
3. What parameters are required?
4. What should it return?
5. Do I need a counter, total or result list?
6. What information should I iterate through?
7. What conditions must be checked?
8. When should the function return?

After implementing:

1. Did I follow every requirement?
2. Did I return rather than print?
3. Are my conditions in the correct order?
4. Is my return statement correctly indented?
5. Have I tested boundary values?
6. What happens with an empty list?
7. Can I remove unnecessary repeated code?
8. Are my variable names clear?

## 23. Quick Reference Cheat Sheet

### Define a function

```python
def function_name():
    print("Hello")
```

### Call a function

```python
function_name()
```

### One parameter

```python
def function_name(value):
    return value
```

### Multiple parameters

```python
def add(a, b):
    return a + b
```

### Store a returned value

```python
result = add(10, 20)
```

### Print a returned value

```python
print(add(10, 20))
```

### Return a calculation

```python
return amount * rate
```

### Conditional return

```python
if amount >= minimum:
    return True

return False
```

### Process a list

```python
def calculate_total(values):
    total = 0

    for value in values:
        total += value

    return total
```

### Count matching elements

```python
def count_matches(values, target):
    count = 0

    for value in values:
        if value == target:
            count += 1

    return count
```

### Filter elements

```python
def filter_amounts(amounts, minimum):
    result = []

    for amount in amounts:
        if amount >= minimum:
            result.append(amount)

    return result
```

## 24. Personal Revision Priorities

Mistakes identified during Module 05:

- Overlapping elif conditions.
- Using print instead of return when returning was required.
- Redundant boundary comparisons.
- Repeating additions inside conditional branches.

All major concepts were successfully applied in the
final independent merchant transaction analysis exercise.

Keep practising functions as part of larger practical
problems involving strings, dictionaries and multiple
processing passes.
