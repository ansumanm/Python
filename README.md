Here's the markdown document corrected for markdown formatting errors:

```markdown
# Python 3 String Operations Reference Sheet

## Basic String Operations

### Creating a String
- Single quotes: `str1 = 'Hello'`
- Double quotes: `str2 = "World"`
- Triple quotes: `str3 = '''Hello World'''`

### Concatenating Strings
- Using `+` operator: `str4 = str1 + str2`
- Using `join()`: `str5 = ''.join([str1, str2])`

### Accessing Characters
- By index: `char = str1[0]` (first character)
- Negative index: `char = str1[-1]` (last character)

### Slicing Strings
- Syntax: `substring = str1[start:end]`
- Example: `first_three = str1[0:3]`

## Common String Methods

### Finding Substrings
- `find(substring)`: Returns the lowest index of the substring if found, else -1.
- `index(substring)`: Like `find()`, but raises a `ValueError` if not found.

### Replacing Substrings
- `replace(old, new)`: Returns a new string where all occurrences of `old` have been replaced by `new`.

### Splitting and Joining
- `split(separator)`: Splits the string at the specified separator and returns a list.
- `join(iterable)`: Joins the elements in the given iterable - a list, tuple, etc.

### Case Conversion
- `upper()`: Converts all characters to uppercase.
- `lower()`: Converts all characters to lowercase.
- `title()`: Converts the first character of each word to uppercase.

### Stripping Whitespace
- `strip()`: Removes whitespaces from both ends.
- `lstrip()`: Removes leading whitespace.
- `rstrip()`: Removes trailing whitespace.

### Checking String Content
- `isdigit()`: Checks if all characters are digits.
- `isalpha()`: Checks if all characters are alphabetic.
- `isalnum()`: Checks if all characters are alphanumeric.
- `isspace()`: Checks if all characters are whitespace.

## Formatting Strings

### Old Style (% Operator)
- Syntax: `"%s %s" % (str1, str2)`
- Example: `formatted = "%d apples" % 5`

### New Style (`format` method)
- Syntax: `"{} and {}".format(str1, str2)`
- Example: `formatted = "{} apples".format(5)`

### f-Strings (Python 3.6+)
- Syntax: `f"{variable1} and {variable2}"`
- Example: `formatted = f"{5} apples"`

## String Literals

### Raw Strings
- Syntax: `r"Raw\nString"` (no escaping)

### Unicode Strings
- Syntax: `u"Unicode"` (Python 2 compatibility)

Remember, strings in Python are immutable, which means once a string is created, it cannot be modified.

# Python 3 In-built Data Structures Reference Sheet

## Overview
Python offers several built-in data structures that are optimized for various uses. These include lists, tuples, sets, and dictionaries.

## Lists
- **Mutable sequences** typically used to store collections of homogeneous items.
- **Creation**: `my_list = [1, 2, 3]` or `my_list = list()`
- **Common Operations**:
  - Append: `my_list.append(item)`
  - Remove: `my_list.remove(item)` # Remove first occurrence of the item from the list
  - Pop: `my_list.pop()` # Remove last element
  - Insert: `my_list.insert(index, item)`
  - Index: `index = my_list.index(item)`
  - Count: `count = my_list.count(item)`
  - Sort: `my_list.sort()`
  - Reverse: `my_list.reverse()`

## Tuples
- **Immutable sequences** typically used to store collections of heterogeneous data.
- **Creation**: `my_tuple = (1, 'hello', 3.14)` or `my_tuple = tuple()`
- **Common Operations**:
  - Access: `element = my_tuple[index]`
  - Count: `count = my_tuple.count(item)`
  - Index: `index = my_tuple.index(item)`

## Sets
- **Unordered collections of unique elements**. Useful for membership testing, removing duplicates, and mathematical operations like intersection, union, difference, and symmetric difference.
- **Creation**: `my_set = {1, 2, 3}` or `my_set = set()`
- **Common Operations**:
  - Add: `my_set.add(item)`
  - Remove: `my_set.remove(item)`
  - Union: `union_set = my_set.union(other_set)`
  - Intersection: `intersection_set = my_set.intersection(other_set)`
  -

 Difference: `difference_set = my_set.difference(other_set)`
  - Symmetric Difference: `sym_diff_set = my_set.symmetric_difference(other_set)`

## Dictionaries
- **Mutable mappings of keys to values**. Ideal for storing and retrieving data by keys.
- **Creation**: `my_dict = {'key1': 'value1', 'key2': 'value2'}` or `my_dict = dict()`
- **Common Operations**:
  - Access: `value = my_dict[key]`
  - Add/Update: `my_dict[key] = new_value`
  - Remove: `del my_dict[key]`
  - Keys: `keys = my_dict.keys()`
  - Values: `values = my_dict.values()`
  - Items: `items = my_dict.items()`
  - Get: `value = my_dict.get(key, default_value)`

## Additional Notes
- **List Comprehensions**: Provide a concise way to create lists. Syntax: `[expr for item in iterable]`
- **Dictionary Comprehensions**: Similar to list comprehensions but for dictionaries. Syntax: `{key: value for (key, value) in iterable}`
- **Set Comprehensions**: Syntax similar to lists and dictionaries but with curly braces. Syntax: `{expr for item in iterable}`

Python's data structures are powerful and provide a wide range of functionality for handling various data types and operations.

## Looping/Iterating Through Data Structures

### Looping Over Lists
- Basic For Loop: `for item in my_list: print(item)`
- With Index: `for index, item in enumerate(my_list): print(index, item)`

### Looping Over Tuples
- Basic For Loop: `for item in my_tuple: print(item)`
- With Index: `for index, item in enumerate(my_tuple): print(index, item)`

### Looping Over Sets
- Basic For Loop: `for item in my_set: print(item)`

### Looping Over Dictionaries
- Over Keys: `for key in my_dict: print(key)`
- Over Values: `for value in my_dict.values(): print(value)`
- Over Key-Value Pairs: `for key, value in my_dict.items(): print(key, value)`

### Advanced Looping Techniques
- List Comprehensions: `[expression for item in iterable]`
- Nested Loops: `for item1 in iterable1: for item2 in iterable2: # process`
- While Loops: `while condition: # process`
- Infinite Loop With Break: `while True: if exit_condition: break`
- Loop With `continue`: `for item in iterable: if some_condition: continue`

# Python 'If' Checks in Data Structures Reference Card

## Checking in Lists, Tuples, and Sets

### Check if Item Exists
```python
if item in my_list:
    # Do something
```

### Check if List is Empty
```python
if not my_list:
    # List is empty
```

## Checking in Dictionary

### Check if Key Exists
```python
if key in my_dict:
    # Do something
```

### Check if Dictionary is Empty
```python
if not my_dict:
    # Dictionary is empty
```

### Check if Value Exists
```python
if value in my_dict.values():
    # Do something
```

## Additional Checks

### Check if All/Any Elements Meet a Condition (Lists, Sets, Tuples)
#### All elements meet the condition
```python
if all(condition(item) for item in iterable):
    # Do something
```

#### If any element meets the condition:
```python
if any(condition(item) for item in iterable):
    # Do something
```

### Check for a Specific Number of Occurrences (Lists, Tuples)
```python
if my_list.count(item) == n:
    # Do something
```
```
