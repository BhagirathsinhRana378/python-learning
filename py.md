# Python Quick Reference & Core Concepts

A comprehensive guide to Python's memory model, data structures, strings, functions, and critical gotchas to remember.

---

## 1. Python Core Mechanics & Memory Model

### Reference Counting & Garbage Collection
Python uses **Reference Counting** as its primary mechanism for memory management, supplemented by a cyclic garbage collector.
- Every object in Python has a reference count (`ob_refcnt`). When an object is referenced, its count increases. When references are deleted or go out of scope, the count decreases.
- When the reference count reaches `0`, Python immediately deallocates the object.

```python
import sys

# Checking the reference count of an object
a = [1, 2, 3]
# Note: sys.getrefcount(a) returns 2 because passing 'a' to getrefcount 
# creates a temporary reference inside the function.
print(sys.getrefcount(a))  # Output: 2

b = a
print(sys.getrefcount(a))  # Output: 3 (a, b, and the function argument)
```

> [!NOTE]
> For small integers (typically -5 to 256) and short strings, Python caches/interns them.
> ```python
> sys.getrefcount(24601)  # Might be higher or lower depending on the environment/caching.
> ```

### Mutability vs. Immutability
Understanding mutability is crucial because it affects variable assignment, function arguments, and performance.

| Data Type | Immutable? | Examples / Description |
| :--- | :--- | :--- |
| **int, float, bool** | Yes | Any arithmetic creates a new object. |
| **str** | Yes | Modifying a string creates a new string. |
| **tuple** | Yes | Elements cannot be added, removed, or replaced. |
| **list** | No | Can append, extend, pop, or modify elements in-place. |
| **dict** | No | Keys/values can be added, updated, or deleted in-place. |
| **set** | No | Can add or remove elements in-place. |

---

## 2. String Manipulation & Formatting

Strings in Python are immutable sequences of Unicode characters.

### Common String Methods
* **`.strip()`**: Removes leading and trailing whitespace (or specific characters if passed).
* **`.replace(old, new[, count])`**: Returns a new string with occurrences of `old` replaced by `new`.
* **`.split(sep=None)`**: Splits the string by a delimiter into a list. By default, splits by any whitespace.
* **`.join(iterable)`**: Concatenates elements of an iterable (e.g., list of strings) using the host string as a separator.
* **`.find(sub)`**: Returns the lowest index where substring `sub` is found, or `-1` if not found.
* **`.count(sub)`**: Returns the number of non-overlapping occurrences of substring `sub`.

```python
# Strip & Replace Examples
chai = "  Lemon Chai  "
print(chai.strip())                     # Output: "Lemon Chai"
print(chai.replace("Lemon", "Ginger"))   # Output: "  Ginger Chai  "

# Splitting Strings
chai_list = "Lemon, Ginger, Masala, Mint"
print(chai_list.split())                # Output: ['Lemon,', 'Ginger,', 'Masala,', 'Mint'] (splits on space)
print(chai_list.split(", "))            # Output: ['Lemon', 'Ginger', 'Masala', 'Mint'] (splits on exact separator)

# Joining Collections
chai_variety = ["Lemon", "Masala", "Ginger"]
print("".join(chai_variety))            # Output: "LemonMasalaGinger"
print(" ".join(chai_variety))           # Output: "Lemon Masala Ginger"
print("-".join(chai_variety))           # Output: "Lemon-Masala-Ginger"
```

### String Formatting
Modern Python uses **f-strings** (formatted string literals), but `.format()` is still common in legacy code.

```python
chai_type = "Masala"
quantity = 2

# Using .format()
order_template = "I ordered {} cups of {} chai"
print(order_template.format(quantity, chai_type))
# Output: "I ordered 2 cups of Masala chai"

# Modern f-strings (Recommended)
order_f = f"I ordered {quantity} cups of {chai_type} chai"
print(order_f)
```

### Special String Literals & Escape Sequences
* Use backslash `\` to escape special characters inside a string (e.g., `\"`, `\'`, `\n`, `\t`).
* Prefix a string with `r` to make it a **raw string**, which ignores escape sequences (useful for regex patterns or file paths).

```python
# Escaped Quotes & Newlines
quote = "He said, \"Masala chai is awesome\""
print(quote)  # Output: He said, "Masala chai is awesome"

newline_str = "Masala\nChai"
print(newline_str)
# Output:
# Masala
# Chai

# Raw Strings
raw_path = r"Masala\nchai"
print(raw_path)  # Output: Masala\nchai (literally prints the backslash and 'n')
```

---

## 3. Core Data Structures & Comprehensions

### 1. Lists (`[]`)
* Ordered, mutable sequence.
* Append: `O(1)`, Insert/Remove: `O(N)`.

### 2. Dictionaries (`{key: value}`)
* Unordered (ordered by insertion since Python 3.7), mutable mapping.
* Keys must be hashable (immutable objects like strings, numbers, or tuples containing only immutable types).
* Lookup/Insert/Delete: Average `O(1)`.

### 3. Sets (`{value}`)
* Unordered collection of unique, hashable items.
* Lookup/Add/Remove: Average `O(1)`.
* Useful for finding intersections (`&`), unions (`|`), and differences (`-`).

### Comprehensions
Comprehensions provide a concise way to create lists, dictionaries, or sets.

```python
# List Comprehension: [expression for item in iterable if condition]
squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares)  # Output: [0, 4, 16, 36, 64]

# Dictionary Comprehension
square_dict = {x: x**2 for x in range(5)}
print(square_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Set Comprehension
unique_lengths = {len(word) for word in ["apple", "banana", "pear", "apple"]}
print(unique_lengths)  # Output: {4, 5, 6}
```

---

## 4. Functions, Scope, & Decorators

### Variable Scope (LEGB Rule)
Python searches for variables in the following order:
1. **L**ocal: Defined inside the current function.
2. **E**nclosing: Defined in outer/nested functions (closures).
3. **G**lobal: Defined at the top level of the module/file.
4. **B**uilt-in: Built into Python (like `len`, `range`, `print`).

To modify a variable outside the local scope, use `global` or `nonlocal` keywords.

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        nonlocal x
        x = "modified enclosing"
    inner()
    print(x)  # Prints "modified enclosing"

outer()
```

### Argument Packing & Unpacking
* `*args`: Collects positional arguments as a tuple.
* `**kwargs`: Collects keyword arguments as a dictionary.

```python
def make_order(*args, **kwargs):
    print(f"Items: {args}")        # tuple
    print(f"Details: {kwargs}")    # dict

make_order("Chai", "Biscuit", table=4, paid=True)
# Output:
# Items: ('Chai', 'Biscuit')
# Details: {'table': 4, 'paid': True}
```

### Decorators
A decorator is a function that takes another function as an argument, extends its behavior without modifying it, and returns the modified function.

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

---

## 5. Critical Gotchas & Things to Remember

> [warning]
> **Gotcha 1: Mutable Default Arguments**
> Default arguments are evaluated **once** when the function is defined, not when it is called. Using a mutable object (like a list or dict) as a default will share that object across all calls.
> 
> *Incorrect:*
> ```python
> def add_item(item, list_=[]):
>     list_.append(item)
>     return list_
> 
> print(add_item(1))  # [1]
> print(add_item(2))  # [1, 2] -- Unexpected!
> ```
> 
> *Correct:*
> ```python
> def add_item(item, list_=None):
>     if list_ is None:
>         list_ = []
>     list_.append(item)
>     return list_
> ```

> [important]
> **Gotcha 2: Reference Sharing / Object Copying**
> Assignment (`b = a`) does not copy the object; it only creates a new reference.
> 
> ```python
> a = [1, 2, 3]
> b = a
> b.append(4)
> print(a)  # Output: [1, 2, 3, 4] -- 'a' was modified!
> ```
> To create a real copy, use `.copy()`, slicing `[:]`, or the `copy` module for nested structures (`deepcopy`).

> [caution]
> **Gotcha 3: Modifying a List while Iterating**
> Modifying a list (adding or removing items) while iterating over it can cause skipped items or out-of-bounds index issues.
> 
> *Incorrect:*
> ```python
> nums = [1, 2, 3, 4]
> for x in nums:
>     if x % 2 == 0:
>         nums.remove(x)  # Skips/breaks index positions
> ```
> 
> *Correct:*
> Iteration over a copy of the list instead:
> ```python
> for x in nums[:]:
>     if x % 2 == 0:
>         nums.remove(x)
> ```
> Or use a list comprehension to create a new filtered list (cleaner):
> ```python
> nums = [x for x in nums if x % 2 != 0]
> ```

> [tip]
> **Gotcha 4: Identity vs. Equality (`is` vs `==`)**
> - `==` checks for value equality (do they have the same data/values?).
> - `is` checks for identity (do they point to the exact same memory address?).
> 
> ```python
> a = [1, 2]
> b = [1, 2]
> print(a == b)  # True
> print(a is b)  # False (different objects in memory)
> ```