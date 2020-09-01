Locations = {0: "You are sitting infront of a computer and learning Python",
             1: "You are standing at the end of the road before a small brick building",
             2: "You are at the top of the hill",
             3: "you are inside a building, a well house for small stream",
             4: "You are in a valley beside a stream",
             5: "You are in forest"}

exists = [{"Q":0},
          {"W": 2, "E": 3, "N": 5, "S":4, "Q":0},
          {"N": 5, "Q":0},
          {"W": 1, "Q":0},
          {"N": 1, "W": 2, "Q":0},
          {"W": 2, "S":1, "Q":0}]

loc = 1
while True:
    availableExist = ""
    for direction in exists[loc].keys():
        availableExist += direction + ", "
    print(Locations[loc])

    if loc == 0:
        break

    direction = input("Available Exists are " +availableExist.upper())
    print()
    if direction in exists[loc]:
        loc = exists[loc][direction]
    else:
        print("you cannot go in that direction")