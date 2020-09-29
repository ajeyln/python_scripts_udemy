text = "Have you ever failed in german exam"


# to make a list with capitalizing each character
def comp_cap():
    capitals = [char.upper() for char in text]
    print(capitals)

# using map
def map_caps():
    map_capitals = list(map(str.upper, text))
    print(map_capitals)

# capitalizing the each word
def comp_words():
    words = [word.upper() for word in text.split(" ")]
    print(words)

#using map
def map_words():
    map_word = list(map(str.upper, text.split(' ')))
    print(map_word)

def display_star():
    print("*" * 120)

if __name__ == '__main__':
    comp_cap()
    map_caps()
    display_star()
    comp_words()
    map_words()