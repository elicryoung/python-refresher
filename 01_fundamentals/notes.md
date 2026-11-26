# Fundamentals

<link rel="stylesheet" href="../notes.css">

[Home](../README.md) | [Exercises](exercises.py)

## Table of Contents

- [Variables and Data Types](#variables-and-data-types)
- [Arithmetic Operators](#arithmetic-operators)
- [Assignment Operators](#assignment-operators)
- [VS Code Shortcuts](#vs-code-shortcuts)

---

## Variables and Data Types

| Type | Description | Example |
|------|-------------|---------|
| `str` | Text surrounded by quotes | `"hello"` |
| `int` | Whole number | `500` |
| `float` | Floating-point number | `2.5` |
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

### Rules

- Variable names cannot contain spaces.
- Variable names cannot start with a number.
- Python is case-sensitive.
- Strings require quotation marks.
- Booleans are capitalised: `True` and `False`.
- Variables can be reassigned.

[↑ Back to top](#table-of-contents)

---

## Arithmetic Operators

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

---

## Assignment Operators

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

---

## VS Code Shortcuts

| Shortcut (Mac) | Action |
|----------------|--------|
| `⇧ ⌘ Enter` | Run Python file (custom shortcut) |
| `⌘ S` | Save file |
| `⌘ /` | Comment / uncomment selected lines |
| `⌥ ⇧ A` | Toggle block comment (supported languages) |
| `⌘ J` | Show / hide terminal |
| `⌘ B` | Show / hide sidebar |
| `⌘ ⇧ V` | Open Markdown preview |
| `⌘ K`, then `V` | Open Markdown preview beside editor |
| `⌘ K`, then `⌘ S` | Open keyboard shortcut settings |
| `⌥ ↑ / ↓` | Move line up / down |
| `⇧ ⌥ ↑ / ↓` | Duplicate line up / down |
| `⌘ Z` | Undo |
| `⌘ ⇧ Z` | Redo |
| `⌘ F` | Find text |
| `⌘ D` | Select next matching occurrence |
| `⌘ P` | Quickly open a file |
| `⌘ ⇧ P` | Open command palette |
| `Ctrl + L` | Clear terminal when focused |
| `↑` in terminal | Retrieve previous command |
| `Tab` | Indent code |
| `⇧ Tab` | Remove indentation |

[↑ Back to top](#table-of-contents)

