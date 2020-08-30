menu = [
    ["egg","bacon"],
    ["egg","sausage","bacon"],
    ["egg","spam"],
    ["egg","bacon","sausage","spam"],
    ["spam","bacon","sausage","spam"],
    ["spam","sausage","spam","bacon","spam","tomato","spam"],
    ["spam","egg","spam","spam","bacon","spam",],
]
# to find the list without "spam"
for meal in menu:
    if "spam" not in meal:
        print(meal)
    print()
    for item in meal:
        print(item)
    else:
        print("{} has a spam score of {}".format(meal,meal.count("Spam")))
print()

# if we want to delete "spam" from list method - 1
for meal in menu:
    for index in range(len(meal) -1, -1, -1):
        if meal[index] == "spam":
            del meal[index]
    print(meal)
print()

# if we want to delete "spam" from list method - 2
for meal in menu:
    for item in meal:
        if item != "spam":
            print(item)
