if __name__ == "__main__":
  with open("day2p1input.txt") as fp:
    ids = fp.readlines()
  # Bad O(n^2) solution
  def common_chars(s1, s2):
    return ''.join([a for a,b in zip(s1, s2) if a == b])
  
  def is_differ_by_1(s1, s2):
    diff = 0
    for a, b in zip(s1, s2):
      if a != b:
        diff += 1
    return diff == 1

  str1 = ""
  str2 = ""
  for i in range(250):
    for j in range(i, 250):
      if is_differ_by_1(ids[i], ids[j]):
        str1 = ids[i]
        str2 = ids[j]
  print(common_chars(str1, str2))