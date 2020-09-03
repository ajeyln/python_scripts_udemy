import shelve

fruits = shelve.open("fruit_name")
fruits["orange"] = "a sweet,orange citrus fruit",
fruits["apple"] = "good for making cider",
fruits["lemon"] = "a sour,yellow citrus fruit",
fruits["grape"] = "a small, sweet fruit growing in bunches",
fruits["lime"] = "a sour,yellow citrus fruit",


while True:
    dict_key = input("Enter a fruit:\t")
    if dict_key == "quit":
        break
    if dict_key in fruits:
        description = fruits[dict_key]
        print(description)
    else:
        print('We dont have fruit named {}'.format(dict_key))

"""for v in fruits.value():
    print(v)

print(fruits.values())

for i in fruits.items:
    print(i)

print(fruits.items())"""

fruits.close()