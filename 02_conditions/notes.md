# Conditions

<link rel="stylesheet" href="../notes.css">

[Home](../README.md) | [Exercises](exercises.py)

## Table of Contents

- [Comparison Operators](#comparison-operators)
- [Booleans](#booleans)
- [Logical Operators](#logical-operators)
- [Conditional Statements](#conditional-statements)

---

## Comparison Operators

Compare two values and return `True` or `False`.

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `5 < 3` | `False` |
| `>=` | Greater than or equal to | `5 >= 5` | `True` |
| `<=` | Less than or equal to | `5 <= 3` | `False` |

### Rules

- `=` assigns a value.
- `==` compares two values.
- Python is case-sensitive: `"Hello" == "hello"` is `False`.
- `500 == "500"` is `False`.

### Requirement Wording

| Requirement | Operator |
|-------------|----------|
| Strictly greater than | `>` |
| More than | `>` |
| At least | `>=` |
| Greater than or equal to | `>=` |
| Below | `<` |
| Less than | `<` |
| At most | `<=` |
| No more than | `<=` |

[↑ Back to top](#table-of-contents)

---

## Booleans

Booleans represent either `True` or `False`.

### Boolean Conditions

```python
verified = True
blocked = False

if verified:
    print("Verified")

if not blocked:
    print("Account active")

if verified and not blocked:
    print("Payment approved")
```

### Truthy and Falsy Values

| Value | Boolean equivalent |
|-------|--------------------|
| `0` | `False` |
| `0.0` | `False` |
| `""` | `False` |
| `[]` | `False` |
| `{}` | `False` |
| `()` | `False` |
| `set()` | `False` |
| `None` | `False` |
| Non-zero number | `True` |
| Non-empty string | `True` |
| Non-empty collection | `True` |

### Boolean Conversion

Use `bool()` to convert a value to a Boolean.

```python
bool(0)       # False
bool(500)     # True
bool("")      # False
bool("Hello") # True
bool("False") # True
bool("0")     # True
bool([])      # False
bool([0])     # True
```

### Rules

- Always capitalise `True` and `False`.
- Boolean variables can be checked directly.
- `not` reverses a truth value.
- Non-empty strings are truthy, even `"False"` and `"0"`.
- Empty collections are falsy.

[↑ Back to top](#table-of-contents)

---

## Logical Operators

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

---

## Conditional Statements

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

---

