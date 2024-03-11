def reverse(s: str) -> str:
  r = ''
  for i in range(len(s) -1, -1, -1):
    r = r + s[i]
  return r

if __name__ == "__main__":
  s = "SomeString"
  print(reverse(s))