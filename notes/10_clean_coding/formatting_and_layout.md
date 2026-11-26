# Formatting And Layout

<link rel="stylesheet" href="../notes.css">

[Home](../../README.md) | [Module Index](README.md)

## Table of Contents

- [Before](#before)
- [After](#after)

---

## Reference

| Convention | Example |
|------------|---------|
| Four-space indentation | Inside loops and conditions |
| Spaces around operators | `total += amount` |
| Spaces after commas | `[100, 200, 300]` |
| Descriptive names | `customer_id` |
| Constants in uppercase | `MAX_AMOUNT = 5000` |

### Before

```python
total=0
for i in transactions:
    total+=i
```

### After

```python
total = 0

for amount in transactions:
    total += amount
```

[↑ Back to top](#table-of-contents)

[← Module Index](README.md)
