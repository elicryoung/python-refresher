# Module 06 — Strings and Parsing

## 1. Strings

A string is a sequence of characters.

```python
merchant = "m123"
amount = "200"
```

Numbers inside quotation marks are strings, not integers.

Strings are immutable: individual characters cannot be
changed directly using index assignment.

## 2. Indexing and Slicing

```python
transaction = "m123_c456_500"

print(transaction[0])
print(transaction[-1])
print(transaction[:4])
print(transaction[5:9])
print(transaction[10:])
print(len(transaction))
```

Output:

```text
m
0
m123
c456
500
12
```

Syntax:

```python
string[start:stop:step]
```

- start: inclusive starting index.
- stop: exclusive ending index.
- step: distance between selected characters.
- Negative indices count backwards from the end.
- Omitting start begins at the beginning.
- Omitting stop continues to the end.

Common examples:

```python
string[0]       # First character
string[-1]      # Last character
string[:3]      # First three characters
string[-3:]     # Last three characters
string[1:]      # Remove first character
string[:-1]     # Remove last character
string[::-1]    # Reverse string
```

Slicing a string returns another string.

## 3. String Immutability

Incorrect:

```python
merchant = "m123"
merchant[0] = "c"
```

This raises a TypeError.

Correct:

```python
merchant = "m123"
merchant = "c" + merchant[1:]

print(merchant)
```

Output:

```text
c123
```

String methods return new strings rather than changing
the original string.

## 4. split()

Separates a string into a list of smaller strings.

Syntax:

```python
string.split(separator, maxsplit)
```

Arguments:
- separator: string used to separate fields.
  Defaults to whitespace when omitted.
- maxsplit: maximum number of splits.
  Optional; defaults to unlimited.

Example:

```python
transaction = "m1,200,c1,14"
parts = transaction.split(",")

print(parts)
```

Output:

```python
['m1', '200', 'c1', '14']
```

After splitting, the result is a list.

You can use indexing to access individual fields:

```python
merchant = parts[0]
amount = parts[1]
customer = parts[2]
hour = parts[3]
```

IMPORTANT:
Every element returned by split() is a string.

Additional examples:

```python
"m1_c1_500".split("_")
# ['m1', 'c1', '500']

"hello world".split()
# ['hello', 'world']

"a,b,c,d".split(",", 1)
# ['a', 'b,c,d']

"a,,b".split(",")
# ['a', '', 'b']
```

Unlike fixed slicing, split() works with fields of
different lengths.

## 5. strip(), lstrip() and rstrip()

Remove characters from the ends of strings.

```python
string.strip(chars)
string.lstrip(chars)
string.rstrip(chars)
```

- strip(): removes from both ends.
- lstrip(): removes from the beginning.
- rstrip(): removes from the end.
- chars: optional characters to remove.
  Defaults to whitespace.

Example:

```python
merchant = "  M123  "

print(merchant.strip())
```

Output:

```text
M123
```

strip() does not remove whitespace inside a string.

```python
"  hello world  ".strip()
# 'hello world'
```

The optional chars argument is a collection of individual
characters to remove, not an exact prefix or suffix.

## 6. lower() and upper()

Convert strings to lowercase or uppercase.

Neither method requires arguments.

```python
merchant = "M123"
currency = "eur"

print(merchant.lower())
print(currency.upper())
```

Output:

```text
m123
EUR
```

Useful for normalising inconsistent transaction records.

## 7. Method Chaining

Multiple string methods can be chained together.

```python
merchant = "  M-123  "

merchant = merchant.strip().lower().replace("-", "_")

print(merchant)
```

Output:

```text
m_123
```

Operations execute from left to right:

1. Remove surrounding whitespace.
2. Convert to lowercase.
3. Replace hyphens with underscores.

## 8. replace()

Replaces occurrences of one string with another.

Syntax:

```python
string.replace(old, new, count)
```

Arguments:
- old: string to search for.
- new: replacement string.
- count: optional maximum number of replacements.
  Defaults to replacing every occurrence.

Examples:

```python
"merchant-123".replace("-", "_")
# 'merchant_123'

"€500".replace("€", "")
# '500'

"a-a-a".replace("-", "_", 1)
# 'a_a-a'
```

Replacing with an empty string removes matching text.

## 9. Removing the First Character

Use slicing when removing a character based on its
position rather than its value.

```python
amount = " €200 "
amount = amount.strip()[1:]

print(amount)
```

Output:

```text
200
```

Processing order:

```python
" €200 "
"€200"     # After strip()
"200"      # After [1:]
```

Common mistake:

```python
amount = transaction[1].strip().replace(transaction[1][0], "")
```

transaction[1][0] refers to the original uncleaned
string, so it may contain whitespace rather than
the currency symbol.

Also, replace() removes all occurrences by default.

Use strip()[1:] when the input guarantees exactly one
leading currency symbol after cleaning.

## 10. String Comparisons

String comparisons are case-sensitive and
whitespace-sensitive.

```python
print("EUR" == "EUR")
print("EUR" == "eur")
print("EUR" == " EUR ")
print("EUR" == " eur ".strip().upper())
```

Output:

```text
True
False
False
True
```

Normalise strings before comparing them when the
input may contain inconsistent formatting.

## 11. Type Conversion

### int()

Converts a suitable value to an integer.

```python
amount = int("200")

print(amount + 50)
```

Output:

```text
250
```

### float()

Converts a suitable value to a floating-point number.

```python
fee = float("2.50")

print(fee)
```

Output:

```text
2.5
```

### str()

Converts a value to a string.

```python
amount = str(200)

print("Amount: " + amount)
```

Output:

```text
Amount: 200
```

Common mistakes:

```python
"200" + "50"      # '20050'
200 + 50          # 250

int("200")        # 200
int(" 200 ")      # 200
int("200.50")     # ValueError
float("200.50")   # 200.5
int("€200")       # ValueError
```

int() and float() accept surrounding whitespace.

Remove currency symbols and other invalid characters
before converting numerical strings.

## 12. Parsing Transaction Records

```python
transaction = "m1,200,c1,14"

parts = transaction.split(",")

merchant = parts[0]
amount = int(parts[1])
customer = parts[2]
hour = int(parts[3])

print(amount + 50)
print(hour >= 12)
```

Output:

```text
250
True
```

Use meaningful variable names to identify the fields.

Keep IDs as strings and convert fields that require
numerical comparisons or calculations.

## 13. Parsing Multiple Records

```python
transactions = [
    "m1,200,c1,14",
    "m2,500,c2,9",
    "m1,75,c3,12"
]

total = 0
count = 0

for transaction in transactions:
    parts = transaction.split(",")

    merchant = parts[0]
    amount = int(parts[1])
    customer = parts[2]
    hour = int(parts[3])

    total += amount

    if amount >= 200:
        count += 1

print(total)
print(count)
```

Output:

```text
775
2
```

Using parts rather than overwriting transaction keeps
the original string available and improves readability.

## 14. Chained Comparisons

Instead of:

```python
if hour >= 12 and hour <= 17:
    total += amount
```

Use:

```python
if 12 <= hour <= 17:
    total += amount
```

Both conditions are equivalent.

Always check whether the boundaries are inclusive
or exclusive.

## 15. F-Strings

F-strings insert variables and expressions into strings.

Syntax:

```python
f"Text {variable}"
```

Example:

```python
merchant = "m1"
amount = 200

result = f"{merchant},{amount}"

print(result)
```

Output:

```text
m1,200
```

F-strings automatically format integers and other
values as strings.

Explicit str() conversion is not required here.

Calculations can also be performed inside f-strings:

```python
amount = 200

print(f"Fee: {amount * 0.03}")
```

Output:

```text
Fee: 6.0
```

## 16. Decimal Formatting

```python
fee = 7.5

print(f"{fee:.2f}")
```

Output:

```text
7.50
```

Format specifiers:

| Syntax | Purpose |
|---|---|
| :.0f | Zero decimal places |
| :.1f | One decimal place |
| :.2f | Two decimal places |
| :.3f | Three decimal places |

Formatting changes the displayed string, not the
original numerical value.

For real financial applications, integer minor units
or Decimal are often preferable to floating-point
arithmetic. For these exercises, follow the supplied
requirements.

## 17. Building Formatted Result Lists

```python
transactions = [
    "m1,200",
    "m2,350",
    "m3,75"
]

results = []

for transaction in transactions:
    parts = transaction.split(",")

    merchant = parts[0]
    amount = int(parts[1])

    fee = amount * 0.03
    remainder = amount - fee

    results.append(f"{merchant},{fee:.2f},{remainder:.2f}")

print(results)
```

Output:

```python
['m1,6.00,194.00', 'm2,10.50,339.50', 'm3,2.25,72.75']
```

Avoid unnecessary spaces in formatted output.

Incorrect when exact comma-separated output is required:

```python
f"{merchant}, {fee:.2f}, {remainder:.2f}"
```

Correct:

```python
f"{merchant},{fee:.2f},{remainder:.2f}"
```

Automated tests may compare strings exactly.

Reuse previously calculated variables rather than
repeating the same calculation.

## 18. join()

Combines a collection of strings into one string.

Syntax:

```python
separator.join(iterable)
```

- separator: string inserted between each element.
- iterable: collection of strings, such as a list.

Example:

```python
parts = ["m1", "200", "c1", "14"]

transaction = ",".join(parts)

print(transaction)
```

Output:

```text
m1,200,c1,14
```

join() is effectively the reverse of split() when
using the same explicit separator.

Different separators:

```python
parts = ["m1", "200", "c1"]

",".join(parts)    # 'm1,200,c1'
"-".join(parts)    # 'm1-200-c1'
" ".join(parts)    # 'm1 200 c1'
"".join(parts)     # 'm1200c1'
```

IMPORTANT:
Every element must be a string.

```python
",".join(["m1", 200, "c1"])
```

This raises a TypeError because 200 is an integer.

## 19. Converting List Elements Before Joining

Incorrect:

```python
transaction = ["m1", 200, "c1", 14]

amount = str(transaction[1])
hour = str(transaction[3])

print(",".join(transaction))
```

Creating separate variables does not update the
original list.

The list still contains integers.

Correct:

```python
transaction = ["m1", 200, "c1", 14]

transaction[1] = str(transaction[1])
transaction[3] = str(transaction[3])

print(",".join(transaction))
```

Output:

```text
m1,200,c1,14
```

Index assignment updates the actual list element.

Be aware that modifying a nested list inside a loop
also modifies the original input list.

To preserve the original input, construct a new list:

```python
transaction = ["m1", 200, "c1", 14]

parts = [
    transaction[0],
    str(transaction[1]),
    transaction[2],
    str(transaction[3])
]

print(",".join(parts))
```

## 20. Printing Results on Separate Lines

Using a loop:

```python
results = ["m1,200", "m2,500", "m3,75"]

for result in results:
    print(result)
```

Using join():

```python
print("\n".join(results))
```

Output for both:

```text
m1,200
m2,500
m3,75
```

Using print() with a list directly displays the list:

```python
print(results)
```

Output:

```python
['m1,200', 'm2,500', 'm3,75']
```

Choose the required output format.

## 21. Validation and Processing Order

When processing transactions:

1. Split the record.
2. Extract the required fields.
3. Clean the fields.
4. Convert numerical values.
5. Validate the transaction.
6. Calculate results.
7. Format the result.
8. Append the result.
9. Return the completed collection.

Only append records that satisfy the validation rules.

Example:

```python
if amount > 0 and 0 <= hour <= 23:
    results.append(merchant)
```

An alternative uses continue:

```python
if amount <= 0 or hour < 0 or hour > 23:
    continue

results.append(merchant)
```

continue skips the remaining code in the current
loop iteration.

An else containing only continue is unnecessary when
there is no further code to execute in that iteration.

## 22. Condition Ordering

Incorrect:

```python
if amount < 100:
    fee = amount * 0.05
if amount < 500:
    fee = amount * 0.03
else:
    fee = amount * 0.01
```

An amount of 75 satisfies both if statements.

The second calculation overwrites the first fee.

Correct:

```python
if amount < 100:
    fee = amount * 0.05
elif amount < 500:
    fee = amount * 0.03
else:
    fee = amount * 0.01
```

Use if/elif/else when only one rule should apply.

Use separate if statements when multiple independent
rules may apply.

## 23. Combined Transaction Processing Example

```python
def process_transactions(transactions):
    processed_transactions = []

    for transaction in transactions:
        parts = transaction.split(",")

        merchant = parts[0].strip().lower()
        amount = int(parts[1])
        customer = parts[2].strip().lower()
        hour = int(parts[3])

        if amount > 0 and 0 <= hour <= 23:
            if amount < 100:
                fee = amount * 0.05
            elif amount < 500:
                fee = amount * 0.03
            else:
                fee = amount * 0.01

            processed_transactions.append(
                f"{merchant},{customer},{amount},{fee:.2f}"
            )

    return processed_transactions


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

results = process_transactions(transactions)

for transaction in results:
    print(transaction)
```

Output:

```text
m1,c1,200,6.00
m2,c2,500,5.00
m1,c2,75,3.75
m2,c1,100,3.00
m3,c2,1000,10.00
```

This example assumes each record contains four fields
and valid integer strings for amount and hour.

Malformed records will require additional validation
and exception handling, covered later.

## 24. Return vs Print

Functions responsible for processing data should
generally return their calculated results.

```python
return processed_transactions
```

The caller can then print, reuse or further process
the returned list.

```python
print(process_transactions(transactions))
```

Or print individual records:

```python
for transaction in process_transactions(transactions):
    print(transaction)
```

Printing inside a function is appropriate when its
purpose is displaying information.

Always follow the problem requirements.

HackerRank may check the returned value rather than
the printed output.

## 25. Common Mistakes

1. Forgetting that split() returns a list.
2. Forgetting that split() returns strings.
3. Performing arithmetic on numerical strings.
4. Comparing strings instead of integers.
5. Assuming string methods modify the original string.
6. Forgetting to assign the result of a string method.
7. Confusing string slicing with replace().
8. Removing the wrong character before cleaning.
9. Joining lists containing integers.
10. Creating new variables instead of updating list elements.
11. Accidentally modifying the original input list.
12. Adding unwanted spaces to formatted output.
13. Forgetting the required decimal precision.
14. Using separate if statements for exclusive fee rules.
15. Appending invalid transactions due to indentation.
16. Returning from inside a loop prematurely.
17. Printing when the requirements specify returning.
18. Using unclear variable names.
19. Repeating calculations unnecessarily.
20. Missing individual requirements.

## 26. Problem-Solving Checklist

Before coding:

- What format is the input?
- What separates the fields?
- What does each field represent?
- Which fields need cleaning?
- Which fields need numerical conversion?
- What makes a record valid?
- Can multiple rules apply or only one?
- What exact format should be returned?

After coding:

- Check condition boundaries.
- Check indentation.
- Check invalid and empty inputs.
- Check output spaces and decimal places.
- Check the return value.
- Check whether the original input was modified.
- Verify every requirement individually.

## 27. Quick Reference Cheat Sheet

| Operation | Syntax |
|---|---|
| String length | len(text) |
| First character | text[0] |
| Last character | text[-1] |
| First three characters | text[:3] |
| Last three characters | text[-3:] |
| Remove first character | text[1:] |
| Remove last character | text[:-1] |
| Split string | text.split(",") |
| Remove whitespace | text.strip() |
| Remove leading whitespace | text.lstrip() |
| Remove trailing whitespace | text.rstrip() |
| Lowercase | text.lower() |
| Uppercase | text.upper() |
| Replace text | text.replace(old, new) |
| Remove text | text.replace(old, "") |
| Convert to integer | int(text) |
| Convert to float | float(text) |
| Convert to string | str(value) |
| Format variables | f"{merchant},{amount}" |
| Two decimal places | f"{fee:.2f}" |
| Join strings | ",".join(parts) |
| Join with newlines | "\n".join(parts) |
| Inclusive range | 12 <= hour <= 17 |

Standard parsing pattern:

```python
parts = transaction.split(",")

merchant = parts[0].strip().lower()
amount = int(parts[1])
customer = parts[2].strip().lower()
hour = int(parts[3])
```

Standard result-building pattern:

```python
results = []

for transaction in transactions:
    # Parse
    # Validate
    # Calculate
    # Format
    # Append

    pass
```

## 28. Personal Revision Priorities

Mistakes identified during Module 06:

- Forgetting individual output requirements.
- Using replace() when slicing was simpler.
- Creating converted variables without updating
  the list passed into join().
- Adding unnecessary spaces inside f-strings.
- Using overlapping if statements for fee calculations.
- Incorrect indentation when appending valid results.
- Printing instead of returning the required list.

Strengths demonstrated:

- Independent use of split() and indexing.
- Method chaining.
- String cleaning and normalisation.
- Integer conversion.
- Running totals and counters.
- Inclusive boundary comparisons.
- Constructing formatted transaction records.

The final combined challenge was completed correctly
after corrective feedback.

Continue reinforcing these concepts through dictionary
exercises and unfamiliar practical programming problems.
