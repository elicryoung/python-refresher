# For Loops

<link rel="stylesheet" href="../notes.css">

[Home](../../README.md) | [Module Index](README.md) | [Practice](../../exercises/02_control_flow/for_loops.py)

## Table of Contents

- [Syntax](#syntax)
- [Example](#example)
- [Filtering](#filtering)
- [Running Totals](#running-totals)
- [Conditional Running Total](#conditional-running-total)
- [Counting Occurrences](#counting-occurrences)
- [Counting vs Running Totals](#counting-vs-running-totals)
- [Multiple Calculations](#multiple-calculations)
- [Rules](#rules)

---

## Reference

Repeat an operation for every element in a collection.

### Syntax

```python
for variable in collection:
    # Code to execute
```

### Example

```python
transactions = [100, 200, 300]

for amount in transactions:
    print(amount)

# Output:
# 100
# 200
# 300
```

| Component | Purpose |
|-----------|---------|
| `for` | Begins the loop |
| `amount` | Holds the current element |
| `in` | Specifies what to iterate through |
| `transactions` | Collection being iterated through |
| `:` | Begins the loop body |

### Filtering

Process only elements that satisfy a condition.

```python
transactions = [100, 500, 750, 200, 1000]

for amount in transactions:
    if amount > 500:
        print(amount)

# Output:
# 750
# 1000
```

### Running Totals

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

### Counting Occurrences

Count how many elements satisfy a condition.

```python
transactions = [100, 500, 750, 200, 1000]
count = 0

for amount in transactions:
    if amount >= 500:
        count += 1

print(count)  # 3
```

### Counting vs Running Totals

| Operation | Syntax | Purpose |
|-----------|--------|---------|
| Counting | `count += 1` | Number of matching elements |
| Running total | `total += amount` | Combined value of elements |

### Multiple Calculations

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

### Rules

- A for loop visits each element automatically.
- Code inside the loop must be indented.
- Initialise counters and totals before the loop.
- Update counters and totals inside the loop.
- Print final results outside the loop.
- An empty collection results in zero iterations.
- Multiple variables can be updated in one loop.

[↑ Back to top](#table-of-contents)

[← Module Index](README.md)
