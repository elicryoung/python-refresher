# Arithmetic Operators

<link rel="stylesheet" href="../notes.css">

[Home](../../README.md) | [Module Index](README.md) | [Practice](../../exercises/01_fundamentals/arithmetic_operators.py)

## Table of Contents

- [Rules](#rules)

---

## Reference

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `+` | Adds two values | `10 + 3` | `13` |
| `-` | Subtracts two values | `10 - 3` | `7` |
| `*` | Multiplies two values | `10 * 3` | `30` |
| `/` | Divides and returns a float | `10 / 4` | `2.5` |
| `//` | Divides and rounds down | `10 // 4` | `2` |
| `%` | Returns the remainder after division | `10 % 4` | `2` |
| `**` | Raises a number to a power | `3 ** 3` | `27` |

### Rules

- `/` returns a float when dividing integers.
- `%` returns the remainder, not the decimal portion.
- Multiplication and division occur before addition and subtraction.
- Parentheses can change the order of operations.

```python
10 + 5 * 2    # 20
(10 + 5) * 2  # 30

10 % 2        # 0 (even number)
11 % 2        # 1 (odd number)
```

[↑ Back to top](#table-of-contents)

[← Module Index](README.md)
