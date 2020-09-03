# dependent file, you need to run base file first
import shelve

with shelve.open("recipes") as recipes:
    temp_list = recipes["blt"]
    temp_list.append("butter")
    recipes["blt"] = temp_list

    temp_list = recipes["pasta"]
    temp_list.append("tomato")
    recipes["pasta"] = temp_list

    for snack in recipes:
        print(snack, recipes[snack])
        



