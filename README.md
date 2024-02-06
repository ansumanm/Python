# Python Reference Sheet

# Table of Contents
1. [Basic String Operations](#basic-string-operations)
2. [Common String Methods](#common-string-methods)
3. [Formatting Strings](#formatting-strings)
4. [String Literals](#string-literals)
5. [Basic List Operations](#basic-list-operations)
6. [List Transformation](#list-transformation)
7. [Finding Elements](#finding-elements)
8. [Advanced Operations](#advanced-operations)
9. [Weak Hashmap](#weak-hashmap)
10. [Deque](#deque)

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

# Python 3 In-built Data Structures

## Overview
Python offers several built-in data structures that are optimized for various uses. These include lists, tuples, sets, and dictionaries.

## Basic List Operations

### Creating a List
- `my_list = []` or `my_list = list()`

### Adding Elements
- Append: `my_list.append(element)`
- Insert: `my_list.insert(index, element)`

### Removing Elements
- Remove by value: `my_list.remove(element)`
- Remove by index: `del my_list[index]` or `popped_element = my_list.pop(index)`
- Remove last element: `last_val = my_list.pop()`

### Accessing Elements
- Access by index: `element = my_list[index]`
- Slicing: `sub_list = my_list[start:end]` # start is inclusive, where as end is exclusive.
- Examples:
```python
# Basic Slicing: Get elements from index 1 to 3.
my_list = [0, 1, 2, 3, 4, 5]
slice1 = my_list[1:4]  # Output: [1, 2, 3]

# Get the entire list
full_slice = my_list[:]  # Output: [0, 1, 2, 3, 4, 5]

# Negative slicing: Start from end
slice_from_end = my_list[-3:]  # Output: [3, 4, 5]

# Step Size: Skip elements
every_second_element = my_list[::2]  # Output: [0, 2, 4]

# Reverse a list
reversed_list = my_list[::-1]  # Output: [5, 4, 3, 2, 1, 0]
```


## Finding Elements

### Minimum and Maximum
- Find min value: `min_number = min(my_list)`
- Find max value: `max_number = max(my_list)`

### Getting Indexes
- Find index of element: `index = my_list.index(element)`

## List Information

### Length of List
- `length = len(my_list)`

### Count Occurrences
- `count = my_list.count(element)`

## Sorting and Reversing

### Sorting a List
- In-place sort: `my_list.sort()`
- Sorted copy: `sorted_list = sorted(my_list)`

### Reversing a List
- In-place reverse: `my_list.reverse()`
- Reversed copy: `reversed_list = my_list[::-1]`

## Advanced Operations

### List Comprehensions
- `[expression for item in my_list if condition]`

### Looping Over a List
- `for item in my_list:`

### Converting to Other Data Types
- To string: `str(my_list)`
- To tuple: `tuple(my_list)`

## List Transformation
Transforming a list in Python to another list typically involves applying some operation or function to each element of the original list and creating a new list with these transformed elements. This can be done in several ways, such as using list comprehensions, the `map()` function, or a loop. Here are some examples demonstrating different methods:

### 1. Using List Comprehension

List comprehension is a concise way to create lists. It consists of brackets containing an expression followed by a `for` clause, then zero or more `for` or `if` clauses.

**Example**: Suppose you want to square each number in a list.

```python
original_list = [1, 2, 3, 4, 5]
transformed_list = [x**2 for x in original_list]
print(transformed_list)  # Output: [1, 4, 9, 16, 25]
```

### 2. Using the `map()` Function

The `map()` function applies a given function to each item of an iterable (like a list) and returns a map object (which is an iterator).

**Example**: Converting a list of numbers to strings.

```python
original_list = [1, 2, 3, 4, 5]
transformed_list = list(map(str, original_list))
print(transformed_list)  # Output: ['1', '2', '3', '4', '5']
```

### 3. Using a Loop

You can also use a for-loop to iterate through the original list and build a new list by applying some operation.

**Example**: Adding 10 to each element in a list.

```python
original_list = [1, 2, 3, 4, 5]
transformed_list = []
for item in original_list:
    transformed_list

.append(item + 10)
print(transformed_list)  # Output: [11, 12, 13, 14, 15]
```

### 4. Using Lambda Functions with `map()`

For more complex transformations, you can use lambda functions with `map()`.

**Example**: Multiplying each number by 2 and subtracting 3.

```python
original_list = [1, 2, 3, 4, 5]
transformed_list = list(map(lambda x: x * 2 - 3, original_list))
print(transformed_list)  # Output: [-1, 1, 3, 5, 7]
```

### 5. Using List Comprehension with Conditional Logic

You can incorporate conditions into list comprehensions to perform more complex transformations.

**Example**: Keeping only even numbers and squaring them.

```python
original_list = [1, 2, 3, 4, 5]
transformed_list = [x**2 for x in original_list if x % 2 == 0]
print(transformed_list)  # Output: [4, 16]
```

### Conclusion

The method you choose depends on the specific transformation you need and your preference for readability and conciseness. List comprehensions and `map()` are generally more succinct and Pythonic for straightforward transformations. For more complex operations, a loop or lambda functions might be more suitable.


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

## While Loop

```python
while True:
    # Code block to execute

    # Condition to continue/exit the loop
    if not condition:
        break
```

## `range` Function
The `range()` function in Python is used to generate a sequence of numbers, making it a staple in loop constructions. It can be used in multiple ways:

### Syntax
1. **Single Argument**: `range(stop)`
   - Generates numbers from 0 to `stop-1`.
   - Example: `range(5)` yields `0, 1, 2, 3, 4`.

2. **Two Arguments**: `range(start, stop)`
   - Creates numbers from `start` to `stop-1`.
   - Example: `range(2, 6)` yields `2, 3, 4, 5`.

3. **Three Arguments**: `range(start, stop, step)`
   - Starts from `start`, increments by `step`, stops before `stop`.
   - Example: `range(2, 10, 2)` yields `2, 4, 6, 8`.
4. **Generate numbers in reverse**
   ```python
   # Example: Generate numbers from 10 down to 1
   for i in range(10, 0, -1):
     print(i)
   ```

### Characteristics
- Produces numbers lazily for efficiency.
- Commonly used in `for` loops.
- Returns a range object, convertible to a list.

## Inner Loops in Python
Inner loops are loops within another loop (outer loop), allowing for more complex data processing.

### Usage
- Common in algorithms for comparing pairs or processing multi-dimensional data.
- The inner loop runs in its entirety for each iteration of the outer loop.

### Example
```python
for i in range(3):  # Outer loop
    for j in range(3):  # Inner loop
        print(i, j)
```


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

# Weak Hashmap
A weak hash map, known as a "WeakHashMap" in some languages like Java, and as a "WeakKeyDictionary" or "WeakValueDictionary" in Python, is a special type of hash map with "weak" keys or values. In such maps, the entries (keys and/or values) are stored using weak references. This means that an entry in a weak hash map does not prevent the key (or value) from being garbage collected.

### Key Characteristics of Weak Hash Maps:
1. **Garbage Collection**: Entries in a weak hash map can be automatically removed during garbage collection if their keys (or values) are no longer strongly referenced elsewhere in the program.
2. **Memory Efficiency**: This characteristic makes weak hash maps useful for caching and memory-sensitive applications where you want to avoid memory leaks.
3. **Use Cases**: Often used for keeping track of objects that have some associated metadata as long as the object is in use elsewhere.

### WeakHashmap in Java:
In Java, `WeakHashMap` is a part of the standard library. It keeps weak references to its keys, allowing them to be garbage collected when they are no longer used elsewhere.

```java
WeakHashMap<KeyType, ValueType> weakHashMap = new WeakHashMap<>();
```

### Weak References in Python:
In Python, the `weakref` module provides support for weak references, including `WeakKeyDictionary` and `WeakValueDictionary`. These are similar to the standard `dict` but the keys or values are weakly referenced.

#### Example of WeakKeyDictionary:
```python
import weakref

# Create a weak key dictionary
weak_key_dict = weakref.WeakKeyDictionary()

class MyClass:
    pass

# Create an object and add it to the dictionary
obj = MyClass()
weak_key_dict[obj] = "Some Data"

# As long as 'obj' is referenced, it stays in the dictionary
print(weak_key_dict)

# If the object is deleted, it will be automatically removed from the dictionary
del obj
print(weak_key_dict)  # Dictionary will be empty
```

#### Example of WeakValueDictionary:
```python
# Create a weak value dictionary
weak_value_dict = weakref.WeakValueDictionary()

obj = MyClass()
weak_value_dict['my_key'] = obj

# Object is accessible as long as it's not garbage collected
print(weak_value_dict['my_key'])

# If the object is deleted, its entry is removed from the dictionary
del obj
print(weak_value_dict)  # Dictionary will be empty
```

# Deque

The `deque` (double-ended queue) is a data structure from the `collections` module in Python that supports adding and removing elements from either end with fast and efficient operations. It is implemented to perform append and pop operations from both ends in O(1) time complexity, making it suitable for queues and stacks where such operations are frequent.

### Key `deque` APIs and Their Usage:

1. **Initialization**
   - `deque(iterable=None, maxlen=None)`: Creates a new deque object that is initialized left-to-right (using the iterable argument) with data from iterable. If iterable is not specified, the new deque is empty. `maxlen` is an optional argument that sets the maximum length of the deque. If it is exceeded, older items are automatically removed from the opposite end.

2. **Adding Elements**
   - `append(x)`: Adds `x` to the right side of the deque.
   - `appendleft(x)`: Adds `x` to the left side of the deque.
   - `extend(iterable)`: Adds all elements from `iterable` to the right side of the deque.
   - `extendleft(iterable)`: Adds all elements from `iterable` to the left side of the deque (note that this results in the elements being added in reverse order from the iterable).

3. **Removing Elements**
   - `pop()`: Removes and returns an element from the right side of the deque. Raises an IndexError if no elements are present.
   - `popleft()`: Removes and returns an element from the left side of the deque. Raises an IndexError if no elements are present.
   - `clear()`: Removes all elements from the deque.

4. **Peeking**
   - Deques do not have a direct method for peeking at items without removing them, but you can access elements by index (e.g., `deque[-1]` for the rightmost item, `deque[0]` for the leftmost item).

5. **Deque Properties and Methods**
   - `maxlen`: Property that returns the maximum size of the deque or `None` if unbounded.
   - `rotate(n=1)`: Rotates the deque `n` steps to the right. If `n` is negative, it rotates to the left.
   - `count(x)`: Counts the number of deque elements equal to `x`.
   - `reverse()`: Reverses the elements of the deque in-place.
   - `copy()`: Creates a shallow copy of the deque.

### Usage Examples

```python
from collections import deque

# Creating and populating a deque
dq = deque([1, 2, 3], maxlen=5)
dq.append(4)  # deque becomes [1, 2, 3, 4]
dq.appendleft(0)  # deque becomes [0, 1, 2, 3, 4]
dq.extend([5, 6])  # deque becomes [2, 3, 4, 5, 6] because of maxlen

# Removing elements
dq.pop()  # Returns 6, deque becomes [2, 3, 4, 5]
dq.popleft()  # Returns 2, deque becomes [3, 4, 5]

# Rotating elements
dq.rotate(1)  # deque becomes [5, 3, 4]
dq.rotate(-1)  # deque becomes [3, 4, 5]

# Accessing elements
first_item = dq[0]  # Access the first item (leftmost)
last_item = dq[-1]  # Access the last item (rightmost)
```

The `deque` is highly versatile and can be used in various scenarios requiring efficient FIFO (First In First Out) or LIFO (Last In First Out) data handling, such as implementing queues, stacks, or even for use in algorithms requiring fast appends and pops from both ends of a collection.

In these Python examples, `WeakKeyDictionary` and `WeakValueDictionary` automatically remove entries when their weakly referenced keys or values are no longer in use, helping to conserve memory.
