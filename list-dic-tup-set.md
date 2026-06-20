# Python Collections: Lists, Dictionaries, Tuples, and Sets

A comprehensive reference for Python's core collection data structures, detailing their behaviors, operations, time complexities, and key gotchas.

---

## 1. Lists (`list`)

A **List** is an ordered, mutable sequence of elements. It is one of the most versatile and frequently used data structures in Python.

### Slicing & Modifying
You can slice list elements using `list[start:end:step]`. Note that slicing is **exclusive** of the end index.

> [!WARNING]
> **Gotcha: Slicing Assignment with Strings**
> Assigning a string directly to a list slice iterates over the string and inserts each character as a separate element. To replace a slice with a single string, wrap it inside a list.
> 
> ```python
> tea_varieties = ["Black", "Green", "Oolong", "White"]
> 
> # Incorrect Slice Assignment (String gets unpacked):
> tea_varieties[1:2] = "Lemon"
> print(tea_varieties)  
> # Output: ['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'White']
> 
> # Correct Slice Assignment:
> tea_varieties = ["Black", "Green", "Oolong", "White"]
> tea_varieties[1:2] = ["Lemon"]
> print(tea_varieties)  
> # Output: ['Black', 'Lemon', 'Oolong', 'White']
> ```

### Modifying Lists
Lists are mutable, meaning you can add, change, or remove items in place.

* **`.append(item)`**: Adds an item to the end of the list. `O(1)`
* **`.pop(index=-1)`**: Removes and returns the item at the specified index (defaults to the last item). `O(1)` from end, `O(N)` from start/middle.
* **`.remove(item)`**: Searches for and removes the first occurrence of `item`. Raises `ValueError` if not found. `O(N)`
* **`.insert(index, item)`**: Inserts `item` at the given `index`, shifting subsequent elements. `O(N)`
* **`.copy()`**: Creates a **shallow copy** of the list. Modifying nested lists within the copy will affect the original.

```python
tea_varieties = ["Black", "green", "Masala", "White"]

# Insert at index 1
tea_varieties.insert(1, "green")
print(tea_varieties)  # ['Black', 'green', 'green', 'Masala', 'White']

# Append
tea_varieties.append("Oolong")
print(tea_varieties)  # ['Black', 'green', 'green', 'Masala', 'White', 'Oolong']

# Pop (removes last element by default)
popped = tea_varieties.pop()
print(popped)         # 'Oolong'
print(tea_varieties)  # ['Black', 'green', 'green', 'Masala', 'White']

# Remove first occurrence of "green"
tea_varieties.remove("green")
print(tea_varieties)  # ['Black', 'green', 'Masala', 'White']
```

### List Comprehension
Provides a concise way to create lists using the pattern `[expression for item in iterable if condition]`.

```python
squared_num = [x ** 2 for x in range(10)]
print(squared_num)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

---

## 2. Dictionaries (`dict`)

A **Dictionary** is a mutable, unordered (ordered by insertion since Python 3.7) mapping of unique keys to values.

### Key Access & Safety
Accessing a missing key via `dict[key]` raises a `KeyError`. Using `.get(key)` is safer because it returns `None` (or a custom default) if the key does not exist.

```python
chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}

# Unsafe access:
# print(chai_types["Masalaa"])  # Raises KeyError

# Safe access:
print(chai_types.get("Ginger"))   # Output: "Zesty"
print(chai_types.get("Gingery"))  # Output: None
```

### Iteration Patterns
You can iterate through keys, values, or key-value pairs (`.items()`).

```python
chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Fresh"}

# Iterate keys (default behavior)
for chai in chai_types:
    print(chai)  # Masala, Ginger, Green

# Iterate keys and values
for key in chai_types:
    print(key, chai_types[key])

# Iterate key-value pairs directly (Recommended)
for key, value in chai_types.items():
    print(key, value)
```

### Removing Elements: `.pop()` vs `.popitem()`
* **`.pop(key[, default])`**: Removes the specified `key` and returns its value. If the key is not found, it returns the `default` value if provided; otherwise, it raises a `KeyError`.
* **`.popitem()`**: Removes and returns the last inserted key-value pair as a tuple `(key, value)`. Raises `KeyError` if the dictionary is empty.

```python
chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Fresh"}

# pop()
ginger_value = chai_types.pop("Ginger")
print(ginger_value)  # Output: "Zesty"

# popitem()
last_item = chai_types.popitem()
print(last_item)     # Output: ('Green', 'Fresh')
```

### Creating Dictionaries: `dict.fromkeys()`

> [!CAUTION]
> **Gotcha: Shared Mutable References in `fromkeys`**
> When using `dict.fromkeys(keys, value)` with a mutable object (like a list) as the default value, **every key points to the exact same list in memory**. Modifying one key's list will modify all of them.
> 
> ```python
> keys = ["Masala", "Ginger", "Lemon"]
> 
> # Basic usage with immutable default:
> d1 = dict.fromkeys(keys, "Delicious")
> print(d1)  # {'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}
> 
> # Dangerous usage with mutable default:
> d2 = dict.fromkeys(keys, [])
> d2["Masala"].append("Chai")
> print(d2)  # {'Masala': ['Chai'], 'Ginger': ['Chai'], 'Lemon': ['Chai']} -- ALL updated!
> ```

### Nested Dictionaries
Dictionaries can contain other dictionaries (nested mappings), which is ideal for structured data.

```python
tea_shop = {
    "black": {"name": "English Breakfast", "price": 2.5},
    "green": {"name": "Jasmine", "price": 3.0}
}
print(tea_shop["green"]["price"])  # Output: 3.0
```

---

## 3. Tuples (`tuple`)

A **Tuple** is an ordered, **immutable** sequence of items. 

### Why do we need Tuples?
1. **Data Integrity (Read-Only)**: Ensures the data cannot be modified, which is useful for constants or configuration.
2. **Performance**: Tuples are slightly faster and consume less memory than lists because of their fixed size.
3. **Hashability**: Because they are immutable, tuples containing only immutable elements can be used as keys in dictionaries or elements in sets (lists cannot).

### How does a Tuple differ from a List?
* **Syntax**: Tuples use parentheses `(1, 2)`, whereas Lists use square brackets `[1, 2]`.
* **Mutability**: Lists are mutable; Tuples are immutable.
* **Gotcha: Single-Element Tuple**: To define a tuple with a single element, you **must** include a trailing comma. Otherwise, Python treats it as a standard parenthesized expression.
  ```python
  not_a_tuple = ("Masala")   # Type: str
  is_a_tuple = ("Masala",)   # Type: tuple
  ```

### Common Operations & Methods
Tuples only have two built-in methods because they cannot be modified in place:
* **`.count(value)`**: Returns the number of times `value` appears.
* **`.index(value)`**: Returns the first index of `value` (raises `ValueError` if not found).

```python
# Tuple Unpacking
dimensions = (1920, 1080)
width, height = dimensions
print(f"Width: {width}, Height: {height}")  # Width: 1920, Height: 1080

# Methods
my_tuple = (1, 2, 3, 2, 4)
print(my_tuple.count(2))  # Output: 2
print(my_tuple.index(3))  # Output: 2
```

---

## 4. Sets (`set`)

A **Set** is an unordered collection of **unique, hashable** elements. Sets do not allow duplicate keys or indices.

### Why do we need Sets?
1. **Removing Duplicates**: Convert any iterable to a set to instantly deduplicate it.
2. **Fast Membership Testing**: Checking if an element exists (`item in my_set`) runs in `O(1)` average time, compared to `O(N)` for lists and tuples.
3. **Mathematical Set Operations**: Easily execute union, intersection, and difference operations.

### Set Operations
Python sets support mathematical operators directly.

```python
set_a = {"Green", "Black", "Oolong"}
set_b = {"Green", "Lemon", "Ginger"}

# 1. Intersection (&) - elements in both sets
print(set_a & set_b)  # Output: {'Green'}

# 2. Union (|) - elements in either or both sets
print(set_a | set_b)  # Output: {'Green', 'Black', 'Oolong', 'Lemon', 'Ginger'}

# 3. Difference (-) - elements in set_a but not in set_b
print(set_a - set_b)  # Output: {'Black', 'Oolong'}

# 4. Symmetric Difference (^) - elements in either set, but not both
print(set_a ^ set_b)  # Output: {'Black', 'Oolong', 'Lemon', 'Ginger'}
```

### Set Modification Methods
* **`.add(item)`**: Adds `item` to the set. Does nothing if the item is already present.
* **`.remove(item)`**: Removes `item` from the set. Raises `KeyError` if not found.
* **`.discard(item)`**: Removes `item` if present, but does **not** raise an error if missing.
* **`.pop()`**: Removes and returns an arbitrary element (since sets are unordered). Raises `KeyError` on empty set.
* **`.clear()`**: Removes all elements from the set.

```python
tea_set = {"Black", "Green"}
tea_set.add("Lemon")
print(tea_set)  # Output: {'Black', 'Green', 'Lemon'}

# discard is safer than remove
tea_set.discard("Oolong")  # Does nothing, no error
# tea_set.remove("Oolong")   # Raises KeyError
```
