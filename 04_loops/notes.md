# 04 — Loops

Loops allow us to repeat operations, process collections,
calculate totals, count occurrences and match records.

## Table of Contents

- [4.1 For Loops](#41-for-loops)
- [4.2 Filtering](#42-filtering)
- [4.3 Running Totals](#43-running-totals)
- [4.4 Counting](#44-counting)
- [4.5 Multiple Calculations](#45-multiple-calculations)
- [4.6 Minimum and Maximum](#46-minimum-and-maximum)
- [4.7 Building Lists](#47-building-lists)
- [4.8 Range](#48-range)
- [4.9 Index-Based Loops](#49-index-based-loops)
- [4.10 While Loops](#410-while-loops)
- [4.11 Break](#411-break)
- [4.12 Continue](#412-continue)
- [4.13 Nested Loops](#413-nested-loops)
- [4.14 Multiple Passes](#414-multiple-passes)
- [4.15 Combined Challenge](#415-combined-challenge)
- [Common Mistakes](#common-mistakes)
- [Cheat Sheet](#cheat-sheet)

---

## 4.1 For Loops

A for loop iterates through the elements of an iterable.

### Syntax

```python
for variable in iterable:
    # Operation
```

- variable: Holds the current element.
- iterable: The collection being processed.
- The indented block executes once per element.

### Example

```python
transactions = [100, 200, 300]

for amount in transactions:
    print(amount)
```

### Output

```text
100
200
300
```

The variable amount contains the actual value, not its index.

---

## 4.2 Filtering

Filtering means selecting elements that satisfy a condition.

### Example

```python
transactions = [100, 750, 200, 1000]

for amount in transactions:
    if amount >= 500:
        print(amount)
```

### Output

```text
750
1000
```

Only elements satisfying the condition are printed.

---

## 4.3 Running Totals

A running total accumulates values across iterations.

### Syntax

```python
total = 0

for item in items:
    total += item
```

### Example

```python
transactions = [100, 200, 300]

total = 0

for amount in transactions:
    total += amount

print(total)
```

### Output

```text
600
```

Initialise the total before the loop so it retains its value
between iterations.

The statement:

```python
total += amount
```

Is equivalent to:

```python
total = total + amount
```

---

## 4.4 Counting

A counter tracks how many elements satisfy a condition.

### Example

```python
transactions = [100, 750, 200, 1000]

count = 0

for amount in transactions:
    if amount >= 500:
        count += 1

print(count)
```

### Output

```text
2
```

### Counting versus totalling

```python
count += 1
total += amount
```

A counter increases by one.
A running total increases by the relevant value.

---

## 4.5 Multiple Calculations

A single loop can maintain several variables.

### Example

```python
transactions = [100, -50, 500, 0, 750]

valid_count = 0
invalid_count = 0
valid_total = 0

for amount in transactions:
    if amount > 0:
        valid_count += 1
        valid_total += amount
    else:
        invalid_count += 1

print(valid_count)
print(invalid_count)
print(valid_total)
```

### Output

```text
3
2
1350
```

Group operations that depend on the same condition.

Avoid repeating identical conditions unnecessarily.

---

## 4.6 Minimum and Maximum

Track the smallest and largest values while iterating.

### Example

```python
transactions = [400, 100, 750, 50, 300]

smallest = transactions[0]
largest = transactions[0]

for amount in transactions:
    if amount < smallest:
        smallest = amount

    if amount > largest:
        largest = amount

print(smallest)
print(largest)
```

### Output

```text
50
750
```

Initialise using the first element rather than an arbitrary
number such as zero.

Initialising the minimum to zero would produce an incorrect
result if every amount were positive.

This approach assumes the list is not empty.

---

## 4.7 Building Lists

Create an empty list and append matching elements.

### Example

```python
transactions = [100, -50, 500, 0, 750]

valid_transactions = []

for amount in transactions:
    if amount > 0:
        valid_transactions.append(amount)

print(valid_transactions)
```

### Output

```text
[100, 500, 750]
```

The original list remains unchanged.

### When to use a list

Use a list when individual matching values must be retained.

Use a counter when only the number of matches is required.

Use a running total when only their combined value is required.

---

## 4.8 Range

range() produces a sequence of integers for iteration.

### Syntax

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

### Arguments

| Argument | Description |
|----------|-------------|
| start | Starting value, inclusive. Defaults to 0. |
| stop | Ending boundary, exclusive. |
| step | Difference between values. Defaults to 1. |

The step cannot be zero.

### Examples

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

```python
for i in range(1, 6):
    print(i)
```

Output:

```text
1
2
3
4
5
```

```python
for i in range(2, 11, 2):
    print(i)
```

Output:

```text
2
4
6
8
10
```

```python
for i in range(5, 0, -1):
    print(i)
```

Output:

```text
5
4
3
2
1
```

A negative step moves backwards.

The stop value is never included.

---

## 4.9 Index-Based Loops

An index-based loop iterates through list positions rather
than directly through values.

### Syntax

```python
for i in range(len(items)):
    print(items[i])
```

### Example

```python
transactions = [100, 200, 300]

for i in range(len(transactions)):
    print(i, transactions[i])
```

### Output

```text
0 100
1 200
2 300
```

### Updating original list elements

```python
transactions = [100, 500, 200]

for i in range(len(transactions)):
    if transactions[i] >= 500:
        transactions[i] -= 50

print(transactions)
```

Output:

```text
[100, 450, 200]
```

### Updating a temporary variable

```python
transactions = [100, 200, 300]

for amount in transactions:
    amount += 50

print(transactions)
```

Output:

```text
[100, 200, 300]
```

Reassigning an integer loop variable does not update the
original list.

Use the list index to replace an existing element.

### Choosing a loop

Use direct iteration when only the values are required.

```python
for amount in transactions:
```

Use index-based iteration when positions are required or
when replacing list elements.

```python
for i in range(len(transactions)):
```

### Nested list indexing

```python
transactions = [
    ["M001", 100],
    ["M002", 500]
]

print(transactions[0][0])
print(transactions[0][1])
```

Output:

```text
M001
100
```

The first index selects the record.
The second index selects a field within that record.

Direct iteration is often simpler:

```python
for transaction in transactions:
    print(transaction[0], transaction[1])
```

---

## 4.10 While Loops

A while loop repeats while its condition remains true.

### Syntax

```python
while condition:
    # Operation
    # Update relevant variables
```

The condition is checked before each iteration.

### Example

```python
balance = 500
subscription_cost = 100
payments = 0

while balance >= subscription_cost:
    balance -= subscription_cost
    payments += 1

print(payments)
print(balance)
```

### Output

```text
5
0
```

The condition must eventually become false, or the loop may
continue indefinitely.

### When to use while

Use while when the number of iterations depends on a condition.

Examples:

- Continue processing while sufficient balance remains.
- Repeat until a savings target is reached.
- Repeat until valid input is supplied.

Use for when processing an existing collection or a known
sequence of values.

---

## 4.11 Break

break immediately exits the current loop.

It takes no arguments and requires no parentheses.

### Example

```python
transactions = [120, 450, 1000, 750, 1500]

count = 0

for amount in transactions:
    count += 1

    if amount >= 1000:
        print(amount)
        break

print(count)
```

### Output

```text
1000
3
```

The loop ends when the first suspicious transaction is found.

The remaining transactions are not examined.

In nested loops, break exits only the innermost loop
containing the statement.

---

## 4.12 Continue

continue skips the remaining statements in the current
iteration and moves to the next iteration.

It takes no arguments and requires no parentheses.

### Example

```python
transactions = [100, -50, 200, 0, 750]

for amount in transactions:
    if amount <= 0:
        continue

    print(amount)
```

### Output

```text
100
200
750
```

### Guard clauses

A guard clause handles an exceptional or unwanted case
before the main logic.

```python
valid_count = 0
valid_total = 0

for amount in transactions:
    if amount <= 0:
        continue

    valid_count += 1
    valid_total += amount
```

There is no need to check amount > 0 again.

All values reaching the remaining statements must
already be positive.

### Break versus continue versus pass

| Statement | Behaviour |
|-----------|-----------|
| break | Exits the current loop entirely. |
| continue | Skips the rest of the current iteration. |
| pass | Does nothing; execution continues normally. |

In a while loop, ensure continue does not skip an update
needed to make the loop terminate.

---

## 4.13 Nested Loops

A nested loop is a loop inside another loop.

For each outer iteration, the inner loop normally processes
its entire sequence.

### Syntax

```python
for outer_item in outer_list:
    for inner_item in inner_list:
        # Operation
```

### Example

```python
merchants = ["M001", "M002"]
amounts = [100, 200, 300]

for merchant in merchants:
    for amount in amounts:
        print(merchant, amount)
```

### Output

```text
M001 100
M001 200
M001 300
M002 100
M002 200
M002 300
```

### Matching records

Nested loops can match records across multiple lists.

```python
merchants = ["M001", "M002", "M003", "M004"]

transactions = [
    ["M001", 100],
    ["M002", 750],
    ["M001", 300],
    ["M003", 500],
    ["M002", 200],
    ["M001", 600]
]

for merchant in merchants:
    merchant_total = 0

    for transaction in transactions:
        if merchant == transaction[0]:
            merchant_total += transaction[1]

    print(merchant, merchant_total)
```

### Output

```text
M001 1000
M002 950
M003 500
M004 0
```

### Choosing the outer and inner loops

Ask:

1. What do I need one result for?
2. What information must I examine for each result?
3. When should variables reset?
4. When is an individual result complete?

In this example:

- One result is required per merchant.
- Every transaction must be examined for each merchant.
- The merchant total resets before each inner loop.
- The result is printed after the inner loop completes.

### Variable placement

| Placement | Behaviour |
|-----------|-----------|
| Before both loops | Retains value across all merchants. |
| Inside outer loop | Resets for each merchant. |
| Inside inner loop | Resets for each transaction. |

### Print placement

```python
for merchant in merchants:
    for transaction in transactions:
        # Process transaction

        # Printing here occurs per transaction.

    # Printing here occurs per merchant.

# Printing here occurs once after both loops.
```

### Basic performance

If the outer list contains m elements and the inner list
contains n elements, the inner loop can run m * n times.

Dictionaries can often make record matching more efficient.
Learn the straightforward correct approach first.

---

## 4.14 Multiple Passes

Multiple passes means processing the same data more than once
for different purposes.

Unlike nested loops, the loops are separate.

### Syntax

```python
for item in items:
    # First processing stage

for item in items:
    # Second processing stage
```

### Example

Find transactions greater than the overall average.

```python
transactions = [100, 200, 600, 300]

total = 0

# Pass 1: Calculate total.
for amount in transactions:
    total += amount

average = total / len(transactions)

# Pass 2: Apply a rule using the average.
above_average = []

for amount in transactions:
    if amount > average:
        above_average.append(amount)

print(average)
print(above_average)
```

### Output

```text
300.0
[600]
```

### Why separate loops?

The second stage depends on information that is unavailable
until the first stage has completed.

It is not possible to compare every transaction against
the final average before calculating that average.

### When to use multiple passes

Ask:

- Does a calculation depend on an earlier result?
- Must I count all occurrences before applying a rule?
- Does a later rule depend on updated values?
- Do I need to apply a condition to earlier records?

### Nested loops versus multiple passes

| Requirement | Approach |
|-------------|----------|
| Calculate a total and count together | Single loop |
| Compare each merchant against every transaction | Nested loops |
| Calculate an average, then filter | Multiple passes |
| Count occurrences, then apply a frequency rule | Multiple passes |
| Process groups using a previously calculated result | Multiple passes and nested loops |

---

## 4.15 Combined Challenge

### Merchant performance analysis

Requirements:

1. Ignore transactions with amounts of zero or less.
2. Calculate the overall valid transaction total and average.
3. Calculate each merchant's valid total and count.
4. Count each merchant's above-average transactions.
5. Identify merchants with total transaction values of at least 1000.

### Input

```python
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
```

### Solution

```python
total_valid = 0
total_count = 0

# Pass 1: Calculate the overall statistics.
for transaction in transactions:
    if transaction[1] > 0:
        total_valid += transaction[1]
        total_count += 1

average = total_valid / total_count

print(total_valid)
print(average)

qualifying_merchants = []

# Pass 2: Calculate individual merchant statistics.
for merchant in merchants:
    merchant_total = 0
    merchant_valid_count = 0
    above_average = 0

    for transaction in transactions:
        if transaction[0] == merchant:
            if transaction[1] > 0:
                merchant_total += transaction[1]
                merchant_valid_count += 1

                if transaction[1] > average:
                    above_average += 1

    if merchant_total >= 1000:
        qualifying_merchants.append(merchant)

    print(
        merchant,
        merchant_total,
        merchant_valid_count,
        above_average
    )

print(qualifying_merchants)
```

### Output

```text
3000
500.0
M001 1400 3 1
M002 1200 2 1
M003 400 1 0
M004 0 0 0
['M001', 'M002']
```

### Important decisions

- Calculate overall statistics before using the average.
- Initialise global totals outside all loops.
- Initialise individual merchant totals inside the outer loop.
- Match transaction merchant IDs before processing amounts.
- Group operations sharing the same condition.
- Use >= for an inclusive threshold.
- Print each merchant's result after its inner loop finishes.
- Retain qualifying merchants until all merchants are processed.

### Edge cases

Consider:

- No merchants.
- No transactions.
- All transactions invalid.
- Merchant total exactly 1000.
- Transaction amount exactly equal to the average.
- Merchants with no matching records.
- Repeated transaction records.

The solution above assumes at least one valid transaction.

If none exists, clarify the expected average behaviour
before dividing by total_count.

---

## Common Mistakes

### 1. Resetting a total inside the wrong loop

Incorrect:

```python
for amount in transactions:
    total = 0
    total += amount
```

Correct:

```python
total = 0

for amount in transactions:
    total += amount
```

### 2. Confusing an index with a value

Incorrect:

```python
for i in range(len(transactions)):
    if i >= 500:
        print(i)
```

Correct:

```python
for i in range(len(transactions)):
    if transactions[i] >= 500:
        print(transactions[i])
```

Prefer direct iteration when the index is unnecessary.

### 3. Updating a temporary integer variable

Incorrect if the intention is to update the original list:

```python
for amount in transactions:
    amount += 10
```

Correct:

```python
for i in range(len(transactions)):
    transactions[i] += 10
```

### 4. Incorrect range boundaries

Incorrect when the intention is to produce 1 through 5:

```python
range(6)
```

Correct:

```python
range(1, 6)
```

### 5. Incorrect inclusive thresholds

Requirement: At least 1000.

Incorrect:

```python
if amount > 1000:
```

Correct:

```python
if amount >= 1000:
```

Always test the exact threshold.

### 6. Repeating identical conditions

Unnecessary:

```python
if amount > 0:
    total += amount

if amount > 0:
    count += 1
```

Cleaner:

```python
if amount > 0:
    total += amount
    count += 1
```

### 7. Rechecking a condition after continue

Unnecessary:

```python
if amount <= 0:
    continue
elif amount > 0:
    total += amount
```

Cleaner:

```python
if amount <= 0:
    continue

total += amount
```

### 8. Printing outside the outer loop

Incorrect when one result is required per merchant:

```python
for merchant in merchants:
    total = 0

    for transaction in transactions:
        if transaction[0] == merchant:
            total += transaction[1]

print(merchant, total)
```

Correct:

```python
for merchant in merchants:
    total = 0

    for transaction in transactions:
        if transaction[0] == merchant:
            total += transaction[1]

    print(merchant, total)
```

### 9. Dividing by zero

Potential error:

```python
average = total / count
```

Check whether count can be zero.

Clarify what should happen if there are no valid values.

### 10. Using else when equality must be excluded

Incorrect when counting strictly below-average values:

```python
if amount > average:
    above_count += 1
else:
    below_count += 1
```

Correct:

```python
if amount > average:
    above_count += 1
elif amount < average:
    below_count += 1
```

Values equal to the average belong to neither category.

---

## Cheat Sheet

### Loop syntax

| Syntax | Purpose |
|--------|---------|
| for item in items: | Iterate through values. |
| for i in range(n): | Iterate through 0 to n-1. |
| for i in range(len(items)): | Iterate through list indices. |
| while condition: | Repeat while a condition is true. |
| break | Exit the current loop. |
| continue | Skip the current iteration. |
| pass | Do nothing. |

### Range arguments

| Expression | Values |
|------------|--------|
| range(5) | 0, 1, 2, 3, 4 |
| range(1, 6) | 1, 2, 3, 4, 5 |
| range(2, 11, 2) | 2, 4, 6, 8, 10 |
| range(5, 0, -1) | 5, 4, 3, 2, 1 |
| range(len(items)) | All valid list indices. |

Start is inclusive.
Stop is exclusive.
Step defaults to 1.
Start defaults to 0.
Step cannot be zero.

### Common programming patterns

| Requirement | Pattern |
|-------------|---------|
| Count matching elements | count += 1 |
| Accumulate values | total += amount |
| Store matching values | results.append(item) |
| Update original list element | items[i] = new_value |
| Find minimum | if amount < smallest |
| Find maximum | if amount > largest |
| Match records | if record[0] == target |
| Ignore invalid records | if invalid: continue |
| Find first matching record | break after match |
| Calculate average | total / count |

### Boundary conditions

| Requirement | Operator |
|-------------|----------|
| At least | >= |
| More than | > |
| At most | <= |
| Less than | < |
| Exactly | == |
| Not equal to | != |
| Inclusive range | lower <= value <= upper |

### Variable placement

| Requirement | Initialisation location |
|-------------|-------------------------|
| One total for everything | Before all loops |
| One total per group | Inside outer loop |
| Temporary value per record | Inside record-processing loop |
| List of final results | Before the loop collecting results |

### Choosing a loop structure

| Situation | Structure |
|-----------|-----------|
| Process all values | for |
| Repeat until a condition changes | while |
| Need list positions | Index-based for |
| Replace original list elements | Index-based for |
| Compare each item with other records | Nested loops |
| Later stage depends on earlier results | Multiple passes |
| Stop after the first match | break |
| Ignore an unwanted record | continue |

### Nested loop template

```python
for target in targets:
    total = 0

    for record in records:
        if record[0] == target:
            total += record[1]

    print(target, total)
```

### Multiple-pass template

```python
# Initialise shared information.

for record in records:
    # Collect information.

# Complete intermediate calculations.

for record in records:
    # Apply rules using collected information.
```

### Problem-solving checklist

Before writing a loop, ask:

1. What result is required?
2. What information must I store?
3. What collection must I iterate through?
4. Am I processing a value or an index?
5. What condition must be checked?
6. What variables must be updated?
7. When should variables reset?
8. Does a later calculation depend on an earlier result?
9. Where should the result be printed or stored?
10. What happens at the exact threshold?
11. What happens with empty inputs?
12. Can any conditions or loops be simplified?

