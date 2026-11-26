# Output Formatting

<link rel="stylesheet" href="../notes.css">

[Home](../../README.md) | [Module Index](README.md) | [Practice](../../exercises/10_clean_coding/output_formatting.py)

## Table of Contents

- [Reference](#reference)

---

## Reference

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

[← Module Index](README.md)
