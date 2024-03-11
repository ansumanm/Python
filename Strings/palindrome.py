def check_palindrome(s: str) -> bool:
  j = 0
  for i in range(len(s) - 1, -1, -1):
    if s[i].lower() != s[j].lower():
      return False
    j += 1
    
  return True

if __name__ == '__main__':
  print(check_palindrome('Malayalam'))
  print(check_palindrome("asf fsa"))