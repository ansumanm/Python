def isPalindrome(substr : str) -> bool:
  if len(substr) == 1: 
    return True
  
  i = 0
  for j in range(len(substr) -1 , -1, -1):
    if substr[i] != substr[j]:
      return False
    i = i+1
  return True

def lPS(s: str) -> str:
  if len(s) == 1:
    return s
  
  maxSubstr = ""

  for start in range(0, len(s)):
    if (len(s) - start) < len(maxSubstr):
      break
    for end in range(len(s)+1, start, -1):
      if (end - start) < len(maxSubstr):
        break
      substr = s[start:end]
      # print(substr)
      if isPalindrome(substr):
        if len(maxSubstr) < len(substr):
          maxSubstr = substr

  # No palindrome found, return 1 char
  return maxSubstr


if __name__ == "__main__":
  print(lPS("babad"))
  print(lPS("cbbd"))
  print(lPS("a"))
  print(lPS("ac"))
  print(lPS("bb"))
  # s = "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"
  # print(lPS(s))
  # print(lPS("aacabdkacaa"))
