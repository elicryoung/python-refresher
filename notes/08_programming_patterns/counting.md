# Counting

<link rel="stylesheet" href="../notes.css">

[Home](../../README.md) | [Module Index](README.md) | [Practice](../../exercises/08_programming_patterns/counting.py)

## Table of Contents

- [Reference](#reference)

---

## Reference

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

[← Module Index](README.md)
