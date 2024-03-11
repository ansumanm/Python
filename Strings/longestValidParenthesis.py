def longestValidParenthesis(s: str) -> int:
  substr = '()'

  index = 0
  max_length = 0
  while index < len(s):
    # Find ()
    print(f"{s[index:index+2]}")
    if s[index:index+2] != substr:
      index += 1
      continue
    else:
      start = index
      # Now valid parenthesis
      while s[index:index+2] == substr and index < len(s):
        index += 2
      
      stop = index
      max_length = max(max_length, (stop - start))

  return max_length

def lvp2(s: str) -> int:
  for i in range(0, len(s)):
    for j in range(len(s) - 1, i, -1):
      if s[i] == '(' and s[j] == ')':
        print(f"{i} {j} {s[i:j+1]}")
        return len(s[i:j+1])

  return 0

if __name__ == '__main__':
  str1 = "(()"

  # print(f"{longestValidParenthesis(str1)}")
  print(f"{lvp2(str1)}")

  print(f"str1 {str1[:]}")
