cd ~/Documents/python-refresher

cat > 03_lists/notes.md <<'EOF'
# Lists

<link rel="stylesheet" href="../notes.css">

[Home](../README.md) | [Exercises](exercises.py)

## Table of Contents

- [Creating Lists](#creating-lists)
- [Positive Indexing](#positive-indexing)
- [Negative Indexing](#negative-indexing)
- [Slicing](#slicing)
- [Updating Elements](#updating-elements)
- [Adding Elements](#adding-elements)
- [Removing Elements](#removing-elements)
- [Membership Checking](#membership-checking)
- [List Length](#list-length)
- [Combining Lists](#combining-lists)
- [Copying Lists](#copying-lists)
- [Nested Lists](#nested-lists)
- [Copying Nested Lists](#copying-nested-lists)
- [Choosing the Right Operation](#choosing-the-right-operation)
- [Lists Cheat Sheet](#lists-cheat-sheet)

---

## Creating Lists

A list stores multiple values inside one variable.

### Syntax

```python
transactions = [100, 200, 300]
```

Lists use square brackets `[]`, with values separated
by commas.

| Type | Example |
|---|---|
| Integers | `[100, 200, 300]` |
| Strings | `["M001", "M002"]` |
| Floats | `[10.50, 20.75]` |
| Booleans | `[True, False]` |
| Mixed types | `["M001", 500, True]` |
| Empty list | `[]` |

### Important Rules

- Lists are ordered.
- Lists are mutable: their contents can change.
- Duplicate values are allowed.
- Different data types can be stored together.
- Use square brackets, not parentheses.
- Parentheses with comma-separated values create tuples,
  which are covered in Module 08.

```python
transactions = [500, 100, 500]

print(transactions)

# Output:
# [500, 100, 500]
```

[Back to top](#table-of-contents)

---

## Positive Indexing

Indexing retrieves an individual element by its position.

Python starts counting positions at zero.

```python
transactions = [100, 200, 300, 400, 500]
```

| Index | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| Value | 100 | 200 | 300 | 400 | 500 |

### Syntax

```python
list_name[index]
```

| Syntax | Meaning | Result |
|---|---|---|
| `transactions[0]` | First item | 100 |
| `transactions[1]` | Second item | 200 |
| `transactions[2]` | Third item | 300 |
| `transactions[4]` | Fifth item | 500 |

### Storing Retrieved Values

```python
first = transactions[0]
third = transactions[2]

total = first + third

print(total)

# Output:
# 400
```

### Rules

- Indexes start at zero.
- An index identifies a position, not a value.
- Retrieving an element does not remove it.
- Accessing a nonexistent index causes an IndexError.

[Back to top](#table-of-contents)

---

## Negative Indexing

Negative indexing retrieves elements relative to
the end of a list.

```python
transactions = [100, 200, 300, 400, 500]
```

| Value | 100 | 200 | 300 | 400 | 500 |
|---|---|---|---|---|---|
| Positive index | 0 | 1 | 2 | 3 | 4 |
| Negative index | -5 | -4 | -3 | -2 | -1 |

| Syntax | Meaning | Result |
|---|---|---|
| `transactions[-1]` | Last item | 500 |
| `transactions[-2]` | Second-last item | 400 |
| `transactions[-3]` | Third-last item | 300 |

### Example

```python
last = transactions[-1]
second_last = transactions[-2]

print(last + second_last)

# Output:
# 900
```

Use negative indexing when the required position is
relative to the end of the list.

`transactions[-1]` retrieves the last element regardless
of how many elements the list contains.

[Back to top](#table-of-contents)

---

## Slicing

Slicing retrieves multiple elements from a list.

### Syntax

```python
list_name[start:stop:step]
```

| Component | Meaning |
|---|---|
| Start | Starting index, included |
| Stop | Ending index, excluded |
| Step | Number of positions to move each time |

The stop index is never included.

```python
transactions = [100, 200, 300, 400, 500, 600, 700]
```

| Syntax | Meaning | Result |
|---|---|---|
| `transactions[1:4]` | Indexes 1 to 3 | `[200, 300, 400]` |
| `transactions[:3]` | First three | `[100, 200, 300]` |
| `transactions[3:]` | Skip first three | `[400, 500, 600, 700]` |
| `transactions[-3:]` | Last three | `[500, 600, 700]` |
| `transactions[:-3]` | Exclude last three | `[100, 200, 300, 400]` |
| `transactions[::2]` | Every second item | `[100, 300, 500, 700]` |
| `transactions[::-1]` | Reverse order | `[700, 600, 500, 400, 300, 200, 100]` |
| `transactions[:]` | Copy entire list | `[100, 200, 300, 400, 500, 600, 700]` |

### How to Read Slicing

Think of the colon as the word TO.

```python
transactions[2:5]
```

Start at index 2 and continue TO index 5,
excluding index 5.

```python
transactions[-3:]
```

Start three positions from the end and continue
TO the end.

```python
transactions[:-3]
```

Start at the beginning and continue TO the position
three places from the end, excluding that position.

### Indexing vs Slicing

```python
transactions = [100, 200, 300]

print(transactions[0])
print(transactions[:1])

# Output:
# 100
# [100]
```

Indexing returns an individual element.
Slicing returns a new list.

### Rules

- Start is inclusive.
- Stop is exclusive.
- The default step is 1.
- With a positive step, an omitted start means the beginning.
- With a positive step, an omitted stop means the end.
- A negative step moves backwards.
- A step cannot be zero.
- Slicing does not modify the original list.
- Slicing outside the list boundaries safely returns
  the available elements.

[Back to top](#table-of-contents)

---

## Updating Elements

Lists are mutable, so existing elements can be changed.

### Syntax

```python
list_name[index] = new_value
```

```python
transactions = [100, 200, 300]

transactions[1] = 500

print(transactions)

# Output:
# [100, 500, 300]
```

### Assignment Operators

Each example starts with `[100, 200, 300]`.

| Syntax | Result |
|---|---|
| `transactions[0] = 50` | `[50, 200, 300]` |
| `transactions[-1] = 900` | `[100, 200, 900]` |
| `transactions[1] += 50` | `[100, 250, 300]` |
| `transactions[0] -= 20` | `[80, 200, 300]` |
| `transactions[-1] *= 2` | `[100, 200, 600]` |

Updating an individual element does not change
the length of the list.

The specified index must already exist.

[Back to top](#table-of-contents)

---

## Adding Elements

List methods perform operations on an existing list.

### Method Syntax

```python
list_name.method(arguments)
```

- The dot identifies the method belonging to the list.
- Parentheses execute the method.
- Arguments provide information required by the method.

### append()

Adds one item to the end of a list.

Accepts exactly one argument.

```python
transactions = [100, 200]

transactions.append(300)

print(transactions)

# Output:
# [100, 200, 300]
```

### insert()

Adds one item at a specified position.

Accepts two arguments:

1. The index.
2. The value to insert.

```python
transactions = [100, 200, 300]

transactions.insert(1, 500)

print(transactions)

# Output:
# [100, 500, 200, 300]
```

Existing elements shift to the right.

The new element occupies index 1.

### extend()

Adds multiple individual elements to a list.

Accepts exactly one argument: an iterable.
A list is one example of an iterable.

```python
transactions = [100, 200]

transactions.extend([300, 400, 500])

print(transactions)

# Output:
# [100, 200, 300, 400, 500]
```

The square brackets group the values into one list,
which is passed as one argument.

| Syntax | Result |
|---|---|
| `extend(300, 400, 500)` | TypeError: three arguments |
| `extend([300, 400, 500])` | Correct: one list argument |

If the values already exist in a list, additional
square brackets are not required.

```python
transactions = [100, 200]
new_transactions = [300, 400]

transactions.extend(new_transactions)
```

### append() vs extend()

```python
numbers = [10, 20]
numbers.append([1, 2, 3, 4])

print(numbers)

# Output:
# [10, 20, [1, 2, 3, 4]]
```

The entire list becomes one additional element.

```python
numbers = [10, 20]
numbers.extend([1, 2, 3, 4])

print(numbers)

# Output:
# [10, 20, 1, 2, 3, 4]
```

Each value becomes a separate element.

| Operation | Resulting length | Element at index 2 |
|---|---|---|
| append | 3 | `[1, 2, 3, 4]` |
| extend | 6 | `1` |

### Important Rules

- append adds its argument as one element.
- extend adds the individual elements of its argument.
- insert adds one element at a specified position.
- All three methods modify the original list immediately.
- These methods return None, not the modified list.

Incorrect:

```python
transactions = transactions.append(500)
```

Correct:

```python
transactions.append(500)
```

[Back to top](#table-of-contents)

---

## Removing Elements

### remove()

Removes the first occurrence of a specified value.

Accepts one argument: the value to remove.

```python
transactions = [100, 200, 300, 200]

transactions.remove(200)

print(transactions)

# Output:
# [100, 300, 200]
```

If the value does not exist, Python raises a ValueError.

### pop()

Removes an element by index and returns the removed value.

Accepts one optional argument: the index.

```python
transactions = [100, 200, 300]

removed = transactions.pop(1)

print(transactions)
print(removed)

# Output:
# [100, 300]
# 200
```

Without an argument, pop removes the last element.

```python
transactions.pop()
```

This is equivalent to:

```python
transactions.pop(-1)
```

### When Does pop Execute?

Python evaluates the right-hand side of an assignment
before storing its result.

```python
removed = transactions.pop(1)
```

Python immediately:

1. Removes the element at index 1.
2. Returns the removed value.
3. Assigns that value to removed.

The removal happens even if removed is never used
or printed afterwards.

| Syntax | Removes item? | Stores value? |
|---|---|---|
| `transactions.pop(1)` | Yes | No |
| `removed = transactions.pop(1)` | Yes | Yes |
| `removed = transactions[1]` | No | Yes |

### del

Deletes an element or slice by position.

del is a Python keyword, not a method.

```python
transactions = [100, 200, 300, 400]

del transactions[1]

print(transactions)

# Output:
# [100, 300, 400]
```

Delete multiple elements using slicing:

```python
transactions = [100, 200, 300, 400]

del transactions[:2]

print(transactions)

# Output:
# [300, 400]
```

### clear()

Removes all elements from a list.

Accepts no arguments.

```python
transactions = [100, 200, 300]

transactions.clear()

print(transactions)

# Output:
# []
```

### Choosing a Removal Method

| Requirement | Method |
|---|---|
| Remove a known value | `remove(value)` |
| Remove by index and keep the value | `pop(index)` |
| Remove the last item | `pop()` |
| Delete by index | `del list[index]` |
| Delete several consecutive items | `del list[start:stop]` |
| Remove everything | `clear()` |

Remember that indexes may change after elements
are removed.

[Back to top](#table-of-contents)

---

## Membership Checking

Membership checking determines whether a value exists
inside a list.

### Syntax

```python
value in list_name
value not in list_name
```

Both expressions produce Boolean values.

```python
merchants = ["M001", "M002", "M003"]

print("M002" in merchants)
print("M005" in merchants)
print("M005" not in merchants)

# Output:
# True
# False
# True
```

### Combining Membership with Conditions

```python
registered = ["M001", "M002"]
blocked = ["M005"]
merchant = "M003"

if merchant in blocked:
    print("Merchant blocked")
elif merchant in registered:
    print("Merchant already registered")
else:
    registered.append(merchant)
    print("Merchant registered successfully")

# Output:
# Merchant registered successfully
```

Use an if/elif/else chain because the outcomes
are mutually exclusive.

### Rules

- in checks values, not indexes.
- not in checks whether a value is absent.
- String membership is case-sensitive.
- Membership checking does not modify the list.
- No explicit loop is required.
- Do not unnecessarily compare the result with True.

[Back to top](#table-of-contents)

---

## List Length

len() returns the number of elements in a list.

### Syntax

```python
len(list_name)
```

Accepts one list and returns an integer.

```python
transactions = [100, 200, 300, 400]

print(len(transactions))

# Output:
# 4
```

### Length vs Index

| Expression | Result |
|---|---|
| `len(transactions)` | 4 |
| `len(transactions) - 1` | 3 |
| `transactions[-1]` | 400 |
| `len([])` | 0 |

Length counts elements, while indexing starts at zero.

### Practical Example

```python
registered = ["M001", "M002", "M003"]
capacity = 5

remaining = capacity - len(registered)

print(remaining)

# Output:
# 2
```

Calculate length after modifying a list when the
updated count is required.

[Back to top](#table-of-contents)

---

## Combining Lists

### Using +

Creates a new combined list without modifying
the original lists.

```python
morning = [100, 200]
evening = [300, 400]

combined = morning + evening

print(combined)
print(morning)

# Output:
# [100, 200, 300, 400]
# [100, 200]
```

### Using extend()

Modifies the original list by adding the elements
of another list.

```python
morning = [100, 200]
evening = [300, 400]

morning.extend(evening)

print(morning)

# Output:
# [100, 200, 300, 400]
```

### Comparison

| Syntax | Behaviour |
|---|---|
| `c = a + b` | Creates a new combined list |
| `a.extend(b)` | Modifies a |
| `a += b` | Extends a |
| `a.append(b)` | Adds b as one nested element |

List addition combines lists rather than adding
their numerical values together.

[Back to top](#table-of-contents)

---

## Copying Lists

Assigning a list to another variable does not
automatically create a copy.

### Assignment

```python
original = [100, 200, 300]
backup = original

backup.append(400)

print(original)
print(backup)

# Output:
# [100, 200, 300, 400]
# [100, 200, 300, 400]
```

Both variables refer to the same list.

### Creating a Copy

The copy method accepts no arguments.

```python
original = [100, 200, 300]
backup = original.copy()

backup.append(400)

print(original)
print(backup)

# Output:
# [100, 200, 300]
# [100, 200, 300, 400]
```

### Comparison

| Syntax | Behaviour |
|---|---|
| `backup = original` | Shares the same list |
| `backup = original.copy()` | Creates a shallow copy |
| `backup = original[:]` | Creates a shallow copy |

A shallow copy creates a new outer list.

For lists containing immutable values such as integers,
strings and Booleans, changes to elements in the copy
do not affect the original list.

[Back to top](#table-of-contents)

---

## Nested Lists

A nested list contains other lists as elements.

Useful for storing records with multiple fields.

```python
transactions = [
    ["M001", 500, True],
    ["M002", 750, False],
    ["M003", 200, True]
]
```

| Record index | Field 0 | Field 1 | Field 2 |
|---|---|---|---|
| 0 | M001 | 500 | True |
| 1 | M002 | 750 | False |
| 2 | M003 | 200 | True |

### Accessing Records

```python
print(transactions[0])

# Output:
# ['M001', 500, True]
```

### Accessing Individual Fields

```python
transactions[record_index][field_index]
```

First select the record, then select the field.

```python
print(transactions[1][0])
print(transactions[1][1])
print(transactions[1][2])

# Output:
# M002
# 750
# False
```

### Syntax Reference

| Syntax | Result |
|---|---|
| `transactions[0]` | `["M001", 500, True]` |
| `transactions[0][0]` | `"M001"` |
| `transactions[0][1]` | `500` |
| `transactions[0][2]` | `True` |
| `transactions[-1][0]` | `"M003"` |
| `len(transactions)` | `3` |
| `len(transactions[0])` | `3` |

### Updating Records

```python
transactions[0][1] += 100
transactions[1][2] = True
```

### Adding a Record

```python
transactions.append(["M004", 900, True])
```

Use append rather than extend to keep the record
together as one element.

### Removing a Record

```python
transactions.pop(0)
```

Removes the entire first record.

[Back to top](#table-of-contents)

---

## Copying Nested Lists

The copy method creates a shallow copy.

It copies the outer list but shares the inner lists.

```python
original = [[100, 200], [300, 400]]
backup = original.copy()

backup[0][1] = 999

print(original)
print(backup)

# Output:
# [[100, 999], [300, 400]]
# [[100, 999], [300, 400]]
```

Both lists contain references to the same inner lists.

### Copying Inner Lists Independently

```python
original = [[100, 200], [300, 400]]

backup = [
    original[0].copy(),
    original[1].copy()
]

backup[0][1] = 999

print(original)
print(backup)

# Output:
# [[100, 200], [300, 400]]
# [[100, 999], [300, 400]]
```

This works for the two-level structure shown here.

More deeply nested structures require copying at
additional levels.

General deep copying will be covered when learning
standard library imports.

### Comparison

| Method | Behaviour |
|---|---|
| Assignment | Shares original list |
| Shallow copy | Separate outer list, shared inner lists |
| Copy each inner list | Independent inner lists for this structure |

[Back to top](#table-of-contents)

---

## Choosing the Right Operation

Think about what the problem requires before
selecting a method.

| Requirement | Operation |
|---|---|
| Retrieve one element | Indexing |
| Retrieve several elements | Slicing |
| Replace an existing element | Index assignment |
| Add one element | append |
| Add multiple elements | extend |
| Add at a specific position | insert |
| Remove a known value | remove |
| Remove and retain a value | pop |
| Delete by position | del |
| Delete all elements | clear |
| Check whether a value exists | in |
| Check whether a value is absent | not in |
| Count all elements | len |
| Combine without modifying originals | + |
| Preserve an original list | copy |
| Access a field inside a record | Nested indexing |

[Back to top](#table-of-contents)

---

## Lists Cheat Sheet

A quick revision guide for commonly forgotten
syntax and important differences between operations.

### Slicing

Assume:

```python
items = [100, 200, 300, 400, 500, 600, 700]
```

| Syntax | Meaning | Result |
|---|---|---|
| `items[:3]` | KEEP first 3 | `[100, 200, 300]` |
| `items[3:]` | SKIP first 3 | `[400, 500, 600, 700]` |
| `items[-3:]` | KEEP last 3 | `[500, 600, 700]` |
| `items[:-3]` | SKIP last 3 | `[100, 200, 300, 400]` |
| `items[2:5]` | Indexes 2 to 4 | `[300, 400, 500]` |
| `items[::2]` | Every second item | `[100, 300, 500, 700]` |
| `items[1::2]` | Every second from index 1 | `[200, 400, 600]` |
| `items[::-1]` | Reverse | `[700, 600, 500, 400, 300, 200, 100]` |
| `items[:]` | Shallow copy | All elements |

Remember:

- Before the colon = START.
- After the colon = STOP.
- Stop is always excluded.
- Negative indexes count from the end.

### Indexing vs Slicing

| Syntax | Result |
|---|---|
| `items[-1]` | Last value |
| `items[-1:]` | List containing last value |
| `items[-3]` | Third-last value |
| `items[-3:]` | List containing last three values |

Indexing returns an element.
Slicing returns a list.

### Method Arguments

| Method | Arguments | Purpose |
|---|---|---|
| `append(value)` | One value | Add one element |
| `extend([a, b])` | One iterable | Add individual elements |
| `insert(index, value)` | Index, then value | Insert at position |
| `remove(value)` | One value | Remove first matching value |
| `pop(index)` | Optional index | Remove and return element |
| `pop()` | None | Remove and return last element |
| `clear()` | None | Remove everything |
| `copy()` | None | Create shallow copy |

Remember that extend accepts ONE argument.

```python
items.extend([100, 200, 300])  # Correct
items.extend(100, 200, 300)    # Incorrect
```

### Append vs Extend

Starting with `[10, 20]`:

| Operation | Result |
|---|---|
| `items.append(30)` | `[10, 20, 30]` |
| `items.append([30, 40])` | `[10, 20, [30, 40]]` |
| `items.extend([30, 40])` | `[10, 20, 30, 40]` |

Append adds the argument itself.
Extend adds the elements inside the argument.

### Insert vs Replace

Starting with `[100, 200, 300]`:

| Operation | Result |
|---|---|
| `items.insert(1, 500)` | `[100, 500, 200, 300]` |
| `items[1] = 500` | `[100, 500, 300]` |
| `items[1] += 500` | `[100, 700, 300]` |

Insert shifts existing elements.
Assignment replaces an existing element.

### Removing Elements

Starting with `[100, 200, 300, 200]`:

| Operation | Result |
|---|---|
| `items.remove(200)` | `[100, 300, 200]` |
| `items.pop(1)` | `[100, 300, 200]` |
| `items.pop()` | `[100, 200, 300]` |
| `del items[1]` | `[100, 300, 200]` |
| `del items[:2]` | `[300, 200]` |
| `del items[-2:]` | `[100, 200]` |
| `items.clear()` | `[]` |

remove uses a VALUE.
pop and del use a POSITION.

remove only deletes the first matching occurrence.

### Return Values and Modification

| Operation | Changes original? | Returns |
|---|---|---|
| `append()` | Yes | None |
| `extend()` | Yes | None |
| `insert()` | Yes | None |
| `remove()` | Yes | None |
| `pop()` | Yes | Removed value |
| `clear()` | Yes | None |
| `copy()` | No | New outer list |
| `items[a:b]` | No | New outer list |
| `items[index]` | No | Selected value |
| `a + b` | No | New combined list |
| `len(items)` | No | Integer |
| `value in items` | No | Boolean |

Do not assign the result of a method that returns None.

```python
items = items.append(500)  # Incorrect
items.append(500)          # Correct
```

Methods execute immediately.

```python
removed = items.pop(1)
```

The element is removed even if removed is never used.

### Combining and Copying

| Syntax | Behaviour |
|---|---|
| `c = a + b` | New combined list |
| `a.extend(b)` | Modify a by adding elements of b |
| `a += b` | Extend a with elements of b |
| `a.append(b)` | Add b as one nested element |
| `b = a` | Both refer to the same list |
| `b = a.copy()` | Separate outer list |
| `b = a[:]` | Separate outer list |

### Nested Lists

Assume:

```python
records = [
    ["M001", 500, True],
    ["M002", 750, False]
]
```

| Syntax | Result or effect |
|---|---|
| `records[0]` | Entire first record |
| `records[1][0]` | `"M002"` |
| `records[1][1]` | `750` |
| `records[-1][2]` | `False` |
| `records[0][1] += 100` | Increase first amount |
| `records[1][2] = True` | Update second status |
| `len(records)` | Number of records |
| `len(records[0])` | Number of fields in first record |
| `records.pop(0)` | Remove entire first record |
| `records.append(["M003", 900, True])` | Add complete record |

Remember:

```python
records[record_index][field_index]
```

First select the record, then the field.

### Copying Nested Lists

```python
backup = records.copy()
```

Copies only the outer list.
Inner lists are still shared.

For two records containing immutable values:

```python
backup = [
    records[0].copy(),
    records[1].copy()
]
```

Both inner lists can now be modified independently.

### Common Traps

| Mistake | Remember |
|---|---|
| Using `()` to create a list | Lists use `[]` |
| Third element at index 3 | Third element is index 2 |
| Using `[:-3]` for last three | Use `[-3:]` |
| Including the stop index | Stop is excluded |
| `extend(1, 2, 3)` | Use `extend([1, 2, 3])` |
| Confusing append and extend | One object vs individual elements |
| Confusing remove and pop | Value vs index |
| Forgetting indexes shift | Track the updated list |
| Assigning append's result | append returns None |
| Assuming pop waits until used | pop executes immediately |
| Using assignment as a copy | Use copy() |
| Assuming nested copies are independent | Inner lists remain shared |
| Removing and reinserting to replace | Use index assignment |
| Accessing an empty list | Check length before indexing |

[Back to top](#table-of-contents)
