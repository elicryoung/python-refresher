# Running Totals

<link rel="stylesheet" href="../notes.css">

[Home](../../README.md) | [Module Index](README.md) | [Practice](../../exercises/08_programming_patterns/running_totals.py)

## Table of Contents

- [Conditional Running Total](#conditional-running-total)

---

## Reference

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

[← Module Index](README.md)
