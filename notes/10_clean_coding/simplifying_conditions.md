# Simplifying Conditions

<link rel="stylesheet" href="../notes.css">

[Home](../../README.md) | [Module Index](README.md) | [Practice](../../exercises/10_clean_coding/simplifying_conditions.py)

## Table of Contents

- [Before](#before)
- [After](#after)
- [How to recognise this](#how-to-recognise-this)
- [Redundant Conditions](#redundant-conditions)

---

## Reference

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

[← Module Index](README.md)
