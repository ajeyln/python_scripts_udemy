# Modify the program so that the exits is a dictionary rather than a list,
#with the keys being the numbers of the locations and the values being
#dictionaries holding the exits (as they do at present). no change should be need to the actual code
# once that is working create another dictionary that contains words  that 
#players may use.These words will be the keys, and their values will be 
#a single letter that the program can use to determine which way to go.

import shelve

locations = shelve.open("locations")

locations["0"] = {"desc": "You are sitting infront of a computer and learning Python",
                  "exits": {},
                  "namedExits": {}}

locations["1"] = {"desc": "You are standing at the end of the road before a small brick building",
                  "exits": {"W": "2", "E": "3", "N": "5", "S": "4", "Q": "0"},
                  "namedExits": {"2": "2", "3": "3", "5": "5", "4": "4"}}
                
locations["2"] = {"desc":"You are at the top of the hill",
                  "exits": {"N": "5", "Q":"0"},
                  "namedExits": {"5": "5",}}

locations["3"] = {"desc":"you are inside a building, a well house for small stream",
                  "exits": {"W": "1", "Q": "0"},
                  "namedExits": {"1": "1",}}

locations["4"] = {"desc": "You are in a valley beside a stream",
                  "exits": {"N": "1", "W": "2", "Q": "0"},
                  "namedExits": {"1": "1", "2": "2"}}

locations["5"] = {"desc": "You are in forest",
                  "exits": {"N": "1", "W": "2", "Q": "0"},
                  "namedExits": {"1": "1", "2": "2"}}

locations.close()

vocabulary = shelve.open("Vocabulary")
vocabulary["QUIT"] = "Q",
vocabulary["NORTH"] = "N",
vocabulary["SOUTH"] = "S",
vocabulary["EAST"] = "E",
vocabulary["ROAD"] = "1"
vocabulary["HILL"] = "2"
vocabulary["BUILDING"] = "3"
vocabulary["VALLEY"] = "4"
vocabulary["FOREST"] = "5"

vocabulary.close()