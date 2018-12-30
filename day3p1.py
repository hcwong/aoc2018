def get_coords(claim):
  info = claim.split(" ")
  numbers = [int(x) for x in info[2].split(":")[0].split(",")]
  size = [int(x) for x in info[3].split("\n")[0].split("x")]
  return {"numbers": numbers, "size": size}

if __name__ == "__main__":
  def mark_sheet(info):
    start_x = info["numbers"][0]
    start_y = info["numbers"][1]
    end_x = start_x + info["size"][0] 
    end_y = start_y + info["size"][1]
    for i in range(start_x, end_x):
      for j in range(start_y, end_y):
        sheet[i][j] += 1


  with open("day3input.txt") as fp:
    claims = fp.readlines()
  # We make use of the fact that none of the claims exceed 1000
  sheet = [[0 for i in range(1001)] for j in range(1001)]
  [mark_sheet(get_coords(x)) for x in claims]
  counter = 0
  for i in range(1001):
    for j in range(1001):
      if sheet[i][j] > 1:
        counter += 1
  print(counter)