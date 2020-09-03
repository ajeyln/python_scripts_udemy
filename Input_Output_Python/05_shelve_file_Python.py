import shelve

with shelve.open("fruit_name") as fruits:
    fruits["orange"] = "a sweet,orange citrus fruit",
    fruits["apple"] = "good for making cider",
    fruits["lemon"] = "a sour,yellow citrus fruit",
    fruits["grape"] = "a small, sweet fruit growing in bunches",
    fruits["lime"] = "a sour,yellow citrus fruit",
    print(fruits)
    print(fruits["lime"])
    print(fruits["grape"])

#method 2
bike_model = shelve.open("bike")
bike_model["make"] = "Honda"
bike_model["model"] = "250 dream"
bike_model["colour"] = "red"
bike_model["engine_size"] = 250
print(bike_model)
print(bike_model["engine_size"])
print(bike_model["colour"])