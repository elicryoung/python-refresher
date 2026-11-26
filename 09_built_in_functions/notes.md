# Built-in Functions

<link rel="stylesheet" href="../notes.css">

[Home](../README.md) | [Exercises](exercises.py)

## Table of Contents

- [Filtering](#filtering)

---

## Filtering

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

[↑ Back to top](#table-of-contents)
