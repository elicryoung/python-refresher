# Practical Patterns

<link rel="stylesheet" href="../notes.css">

[Home](../README.md) | [Exercises](exercises.py)

## Table of Contents

- [Counting](#counting)
- [Running Totals](#running-totals)
- [Transaction Processing](#transaction-processing)

---

## Counting

Count how many elements satisfy a condition.

```python
transactions = [100, 500, 750, 200, 1000]
count = 0

for amount in transactions:
    if amount >= 500:
        count += 1

print(count)  # 3
```

[↑ Back to top](#table-of-contents)

---

## Running Totals

Accumulate the values of multiple elements.

```python
transactions = [100, 200, 300]
total = 0

for amount in transactions:
    total += amount

print(total)  # 600
```

### Conditional Running Total

```python
transactions = [100, 500, 750, 200, 1000]
total = 0

for amount in transactions:
    if amount > 500:
        total += amount

print(total)  # 1750
```

[↑ Back to top](#table-of-contents)

---

## Transaction Processing

Perform multiple calculations within one loop.

```python
transactions = [100, 500, 750, 200, 1000]

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
print("Large count:", large_count)
print("Large total:", large_total)
print("Small count:", small_count)

# Output:
# Total revenue: 2550
# Large count: 3
# Large total: 2250
# Small count: 2
```

[↑ Back to top](#table-of-contents)
