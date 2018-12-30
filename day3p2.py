def my_remove(arr, el):
  if el in arr:
    arr.remove(el)

if __name__ == "__main__":
  def mark_sheet(info):
    start_x = info["numbers"][0]
    start_y = info["numbers"][1]
    end_x = start_x + info["size"][0] 
    end_y = start_y + info["size"][1]
    for i in range(start_x, end_x):
      for j in range(start_y, end_y):
        if sheet[i][j] != 0:
          my_remove(ids, sheet[i][j])
          my_remove(ids, info["id"])
          sheet[i][j] = info["id"]
        else:
          sheet[i][j] = info["id"]

  def get_coords(claim):
    info = claim.split(" ")
    id = info[0]
    numbers = [int(x) for x in info[2].split(":")[0].split(",")]
    size = [int(x) for x in info[3].split("\n")[0].split("x")]
    ids.append(id)
    return {"id": id, "numbers": numbers, "size": size}


  with open("day3input.txt") as fp:
    claims = fp.readlines()

  ids = []
  sheet = [[0 for i in range(1001)] for j in range(1001)]
  [mark_sheet(get_coords(x)) for x in claims]
  print(ids)
 