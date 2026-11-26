# Assignment Operators

<link rel="stylesheet" href="../notes.css">

[Home](../../README.md) | [Module Index](README.md) | [Practice](../../exercises/01_fundamentals/assignment_operators.py)

## Table of Contents

- [Example](#example)

---

## Reference

Each example below starts with `x = 10`.

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `=` | Assigns a value | `x = 5` | `5` |
| `+=` | Adds to an existing value | `x += 5` | `15` |
| `-=` | Subtracts from an existing value | `x -= 5` | `5` |
| `*=` | Multiplies an existing value | `x *= 5` | `50` |
| `/=` | Divides an existing value | `x /= 5` | `2.0` |
| `//=` | Floor divides an existing value | `x //= 3` | `3` |
| `%=` | Assigns the remainder | `x %= 3` | `1` |
| `**=` | Raises an existing value to a power | `x **= 2` | `100` |

### Example

```python
balance = 100
balance += 50
balance -= 20

print(balance)  # 130
```

Assignment operators update an existing variable.

```python
total += 5

# Equivalent to:
total = total + 5
```

[↑ Back to top](#table-of-contents)

[← Module Index](README.md)
