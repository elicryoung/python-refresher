# Clean Coding

<link rel="stylesheet" href="notes.css">

[Home](README.md)

## Table of Contents

- [Boolean Simplification](#boolean-simplification)
- [Formatting And Layout](#formatting-and-layout)
- [Naming Conventions](#naming-conventions)
- [Output Formatting](#output-formatting)
- [Simplifying Conditions](#simplifying-conditions)

---

## Boolean Simplification

When variables already contain Boolean values,
avoid unnecessary comparisons.

| Avoid | Prefer |
|-------|--------|
| `if verified == True:` | `if verified:` |
| `if verified == False:` | `if not verified:` |
| `if verified != True:` | `if not verified:` |
| `if verified != False:` | `if verified:` |

[↑ Back to top](#table-of-contents)

---

## Formatting And Layout

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

---

## Naming Conventions

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

---

## Output Formatting

```python
total = 500

# Unnecessary
print("Total revenue: ", + total)

# Better
print("Total revenue:", total)

# F-string
print(f"Total revenue: {total}")
```

Always match the required output exactly, including
capitalisation, punctuation and whitespace.

[↑ Back to top](#table-of-contents)

---

## Simplifying Conditions

### Before

```python
if amount <= 0:
    print("Invalid payment")
elif amount >= 1 and amount <= 999:
    print("Small payment")
elif amount >= 1000 and amount <= 4999:
    print("Medium payment")
elif amount >= 5000:
    print("Large payment")
```

### After

```python
if amount <= 0:
    print("Invalid payment")
elif amount < 1000:
    print("Small payment")
elif amount < 5000:
    print("Medium payment")
else:
    print("Large payment")
```

### How to recognise this

Ask yourself: What do I already know when I reach
this condition?

Every previous condition in an if/elif/else chain
must have been false.

For integer amounts, this eliminates unnecessary
boundary checks.

### Redundant Conditions

```python
# Before
if amount >= 500:
    large_count += 1
elif amount < 500:
    small_count += 1

# After
if amount >= 500:
    large_count += 1
else:
    small_count += 1
```

[↑ Back to top](#table-of-contents)
