# Boolean Simplification

<link rel="stylesheet" href="../notes.css">

[Home](../../README.md) | [Module Index](README.md) | [Practice](../../exercises/10_clean_coding/boolean_simplification.py)

## Table of Contents

- [Reference](#reference)

---

## Reference

When variables already contain Boolean values,
avoid unnecessary comparisons.

| Avoid | Prefer |
|-------|--------|
| `if verified == True:` | `if verified:` |
| `if verified == False:` | `if not verified:` |
| `if verified != True:` | `if not verified:` |
| `if verified != False:` | `if verified:` |

[↑ Back to top](#table-of-contents)

[← Module Index](README.md)
