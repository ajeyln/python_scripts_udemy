shoppinglist = ["milk","pasta","spam","eggs","bread","rice"]
for item in shoppinglist:
    print("Buy " + item)
print("-" * 120)

# exclued spam from the list
for item in shoppinglist:
    if item != "spam":
        print("Buy " + item)
print("-" * 120)

# using continue
for item in shoppinglist:
    if item == "spam":
        continue
    print("Buy " + item)
print("-" * 120)

# to find the position of the items in shopping list
shoppinglist = ["milk","pasta","spam","eggs","bread","rice"]
item_to_found = input("Enter the item name, for which position need to be find : \n")
found_at = None
for index in range(len(shoppinglist)):
    if shoppinglist[index] == item_to_found:
        found_at = index
        break
if found_at is not None:
    print("{} is found at the position  {}".format(item_to_found,(found_at + 1)))
else:
    print("{} is not found".format(item_to_found))
print("-" * 120)

# method 2
if found_at in shoppinglist:
    found_at = shoppinglist.index[item_to_found]
if found_at is not None:
    print("{} is found at the position {}".format(item_to_found,(found_at + 1)))
else:
    print("{} is not found".format(item_to_found))
print("-" * 120)

