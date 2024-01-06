def main():
  my_list = list(range(0, 10))
  print(my_list)

  for index in range(len(my_list) - 1, -1, -1):
    print(my_list[index])

main()