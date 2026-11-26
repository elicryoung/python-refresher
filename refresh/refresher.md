# Python Refresher
## Table of Contents
<link rel="stylesheet" href="notes.css">

- [Python Refresher](#python-refresher)
  - [Table of Contents](#table-of-contents)
  - [1. Data Types](#1-data-types)
    - [Variable Assignment](#variable-assignment)
  - [2. Arithmetic Operators](#2-arithmetic-operators)
  - [3. Assignment Operators](#3-assignment-operators)
    - [Assignment Example](#assignment-example)
    - [Important Rules](#important-rules)

---

## 1. Data Types

| Type | Description | Example |
|------|-------------|---------|
| `str` | Text surrounded by quotes | `"hello"` |
| `int` | Whole number | `500` |
| `float` | Decimal number | `2.5` |
| `bool` | Boolean value | `True` or `False` |

### Variable Assignment

```python
customer_id = "C001"
amount = 7500
fee_percentage = 1.5
payment_successful = True

print(amount)        # 7500
print(type(amount))  # <class 'int'>
```

## 2. Arithmetic Operators

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `+` | Adds two values | `10 + 3` | `13` |
| `-` | Subtracts two values | `10 - 3` | `7` |
| `*` | Multiplies two values | `10 * 3` | `30` |
| `/` | Divides and returns a float | `10 / 4` | `2.5` |
| `//` | Divides and rounds down | `10 // 4` | `2` |
| `%` | Returns the remainder after division | `10 % 4` | `2` |
| `**` | Raises a number to a power | `3 ** 3` | `27` |

## 3. Assignment Operators

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

### Assignment Example

```python
balance = 100
balance += 50
balance -= 20

print(balance)  # 130
```

### Important Rules

- Variable names cannot contain spaces.
- Variable names cannot start with a number.
- Python is case-sensitive.
- Strings require quotation marks.
- Booleans are capitalised: `True` and `False`.
- `/` returns a float, even when dividing two integers.
- `%` returns the remainder, not the decimal portion.
- Multiplication and division occur before addition and subtraction.
- Parentheses can change the order of operations.