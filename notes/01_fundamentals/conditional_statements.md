# Conditional Statements

<link rel="stylesheet" href="../notes.css">

[Home](../../README.md) | [Module Index](README.md) | [Practice](../../exercises/01_fundamentals/conditional_statements.py)

## Table of Contents

- [Example](#example)
- [Separate If Statements](#separate-if-statements)
- [If / Elif Statements](#if--elif-statements)
- [Rules](#rules)

---

## Reference

Execute different code depending on whether conditions are true.

| Keyword | Purpose |
|---------|---------|
| `if` | Checks the first condition |
| `elif` | Checks a condition if previous conditions failed |
| `else` | Executes if all previous conditions failed |

### Example

```python
amount = 2500

if amount <= 0:
    print("Invalid payment")
elif amount < 1000:
    print("Small payment")
elif amount < 5000:
    print("Medium payment")
else:
    print("Large payment")

# Output: Medium payment
```

### Separate If Statements

Each condition is evaluated independently.

```python
amount = 1500

if amount > 500:
    print("Above 500")

if amount > 1000:
    print("Above 1000")

# Output:
# Above 500
# Above 1000
```

### If / Elif Statements

Only the first matching branch executes.

```python
amount = 1500

if amount > 500:
    print("Above 500")
elif amount > 1000:
    print("Above 1000")

# Output: Above 500
```

### Rules

- End each if, elif and else statement with a colon.
- Indent code inside each branch by four spaces.
- Conditions are evaluated from top to bottom.
- Only the first matching branch executes.
- Multiple elif statements are allowed.
- Elif and else are optional.
- Else does not require a condition.

[↑ Back to top](#table-of-contents)

[← Module Index](README.md)
