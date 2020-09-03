# Modify the program so that the exits is a dictionary rather than a list,
#with the keys being the numbers of the locations and the values being
#dictionaries holding the exits (as they do at present). no change should be need to the actual code
# once that is working create another dictionary that contains words  that 
#players may use.These words will be the keys, and their values will be 
#a single letter that the program can use to determine which way to go.

Locations = {0: "You are sitting infront of a computer and learning Python",
             1: "You are standing at the end of the road before a small brick building",
             2: "You are at the top of the hill",
             3: "you are inside a building, a well house for small stream",
             4: "You are in a valley beside a stream",
             5: "You are in forest"}

exists = {0: {"Q":0},
          1: {"W": 2, "E": 3, "N": 5, "S":4, "Q":0},
          2: {"N": 5, "Q":0},
          3: {"W": 1, "Q":0},
          4: {"N": 1, "W": 2, "Q":0},
          5: {"W": 2, "S":1, "Q":0}}

vocabulary = { "QUIT":   "Q",
                "NORTH": "N",
                "SOUTH": "S",
                "EAST":  "E",
                "WEST": "W"}
loc = 1
while True:
    availableExist = ",".join(exits[loc].keys())
    print(Locations[loc])
    if loc == 0:
        break

    direction = input("Available Exists are " +availableExist.upper())
    print()
    # parse the user input,using our vocabulary dictionary if necessary
    if len(direction) > 1:#more than one letter, so check vocab
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break
                
    if direction in exists[loc]:
        loc = exists[loc][direction]
    else:
        print("you cannot go in that direction")