if __name__ == "__main__":
  with open("day1p1input.txt") as fp:
    numbers = fp.readlines()
  actualNumbers = [int(n[1:]) if n[0] == "+" else int(n[1:]) * -1 for n in numbers]
  print(sum(actualNumbers))