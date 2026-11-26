# Booleans

<link rel="stylesheet" href="../notes.css">

[Home](../../README.md) | [Module Index](README.md) | [Practice](../../exercises/01_fundamentals/booleans.py)

## Table of Contents

- [Boolean Conditions](#boolean-conditions)
- [Truthy and Falsy Values](#truthy-and-falsy-values)
- [Boolean Conversion](#boolean-conversion)
- [Rules](#rules)

---

## Reference

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

[← Module Index](README.md)
