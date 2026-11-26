# Logical Operators

<link rel="stylesheet" href="../notes.css">

[Home](../../README.md) | [Module Index](README.md) | [Practice](../../exercises/01_fundamentals/logical_operators.py)

## Table of Contents

- [Truth Table](#truth-table)
- [Example](#example)
- [Checking Ranges](#checking-ranges)
- [Rules](#rules)

---

## Reference

Combine or reverse conditions.

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `and` | Both conditions must be true | `True and False` | `False` |
| `or` | At least one condition must be true | `True or False` | `True` |
| `not` | Reverses a truth value | `not True` | `False` |

### Truth Table

| A | B | A and B | A or B |
|---|---|---------|--------|
| True | True | True | True |
| True | False | False | True |
| False | True | False | True |
| False | False | False | False |

### Example

```python
verified = True
balance = 1000
amount = 500

print(verified and balance >= amount)  # True
print(not verified)                    # False
```

### Checking Ranges

```python
amount = 750

print(amount >= 500 and amount <= 1000)  # True
```

Python also supports chained comparisons:

```python
print(500 <= amount <= 1000)  # True
```

### Rules

- `and` requires both conditions to be truthy.
- `or` requires at least one condition to be truthy.
- `not` reverses the truth value.
- Logical precedence: `not`, then `and`, then `or`.
- Use parentheses to group conditions.

[↑ Back to top](#table-of-contents)

[← Module Index](README.md)
