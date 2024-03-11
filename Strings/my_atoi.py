"""
String to integer
"""
from typing import Union

def my_atoi(s: str) -> int:
  # Strip white spaces.
  s = s.strip()
  
  if not s:
    return 0
  
  sign = 1
  # Check for sign
  if s[0] in ('+', '-'):
    sign = -1 if s[0] == '-' else 1
    s = s[1:]

  # Convert characters to integers until a non numeric character is encountered.
  result = 0
  for char in s:
    if char.isdigit():
      result = result * 10 + int(char)
    else:
      break

  result *= sign

  # Clamp the result to 32-bit integer range.
  INT_MAX = 2**31 -1
  INT_MIN = -2**31

  if result > INT_MAX:
    return INT_MAX
  if result < INT_MIN:
    return INT_MIN
  
  return result

def my_atoi2(s: str) -> Union[int, None]:
  # Optimized
  s = s.strip()

  allowable_char_set = "1234567890+-"

  for c in s:
    if c not in allowable_char_set:
      return None
  
  sign = 1
  if s[0] in ('+', '-'):
    sign = -1 if s[0] == '-' else 1
    s = s[1:]

  result = int(s) * sign
  return result

if __name__ == "__main__":
  print(my_atoi("123456"))
  print(my_atoi2("12asdf3456"))
  print(my_atoi2("-12456"))
