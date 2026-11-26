# Naming Conventions

<link rel="stylesheet" href="../notes.css">

[Home](../../README.md) | [Module Index](README.md)

## Table of Contents

- [Naming Conventions](#naming-conventions)

---

## Reference

Variable names should describe what they store.

| Avoid | Prefer |
|-------|--------|
| `x` | `balance` |
| `i` | `amount` |
| `count500` | `large_count` |
| `total500` | `large_total` |
| `count499` | `small_count` |
| `d` | `merchant_scores` |
| `l` | `transactions` |

### Naming Conventions

- Use descriptive names.
- Use snake_case for variables and functions.
- Use uppercase for constants.
- Use plural names for collections.
- Use singular names for individual elements.

```python
MINIMUM_AMOUNT = 500

transactions = [100, 500, 750]
total_revenue = 0

for amount in transactions:
    total_revenue += amount
```

[↑ Back to top](#table-of-contents)

[← Module Index](README.md)
