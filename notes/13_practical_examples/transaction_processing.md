# Transaction Processing

<link rel="stylesheet" href="../notes.css">

[Home](../../README.md) | [Module Index](README.md) | [Practice](../../exercises/13_practical_examples/transaction_processing.py)

## Table of Contents

- [Reference](#reference)

---

## Reference

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

[← Module Index](README.md)
