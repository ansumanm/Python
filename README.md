# Python 3 String Operations Reference Sheet

## Basic String Operations

### Creating a String
- Single quotes: `str1 = 'Hello'`
- Double quotes: `str2 = \"World\"`
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
- `index(substring)`: Like `find()`, but raises an `ValueError` if not found.

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
- Syntax: `\"%s %s\" % (str1, str2)`
- Example: `formatted = \"%d apples\" % 5`

### New Style (`format` method)
- Syntax: `\"{} and {}\".format(str1, str2)`
- Example: `formatted = \"{} apples\".format(5)`

### f-Strings (Python 3.6+)
- Syntax: `f\"{variable1} and {variable2}\"`
- Example: `formatted = f\"{5} apples\"`

## String Literals

### Raw Strings
- Syntax: `r\"Raw\nString\"` (no escaping)

### Unicode Strings
- Syntax: `u\"Unicode\"` (Python 2 compatibility)

Remember, strings in Python are immutable, which means once a string is created, it cannot be modified.

