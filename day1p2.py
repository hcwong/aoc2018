if __name__ == "__main__":
  with open("day1p1input.txt") as fp:
    numbers = fp.readlines()
  actualNumbers = [int(n[1:]) if n[0] == "+" else int(n[1:]) * -1 for n in numbers]
  freq = 0
  counter = set()
  counter.add(0)
  isRepeated = False
  while not isRepeated:
    for n in actualNumbers:
      freq += n
      if freq in counter:
         isRepeated=True
         break 
      else: counter.add(freq)
  print(freq)
    