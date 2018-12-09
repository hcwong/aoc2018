from collections import Counter

if __name__ == "__main__":
  with open("day2p1input.txt") as fp:
      ids = fp.readlines()
  result = [0, 0]
  for x in ids:
    counter = Counter(x)
    isTwoAdd = False
    isThreeAdd = False
    for _, value in counter.items():
      if value == 2 and not isTwoAdd:
        result[0] += 1
        isTwoAdd = True
      elif value == 3 and not isThreeAdd:
        result[1] += 1
        isThreeAdd = True
  print(result[0] * result[1])
