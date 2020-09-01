fruits = {
           "orange" :"a sweet,orange citrus fruit",
           "apple" :"good for making cider",
           "lemon" :"a sour,yellow citrus fruit",
           "grape" :"a small, sweet fruit growing in bunches",
           "lime" :"a sour,yellow citrus fruit",
           }

def simple_operation():
    print("To find the details in Fruits dictionary")
    print(fruits)
    print()
    print('To find description for "lemon" in Fruits dictionary')
    print(fruits["lemon"])
    print()
    print('To add a fruit name "pear" in in Fruits dictionary')
    fruits["pear"] = "an odd shaped apple"
    print(fruits)
    print()
    print('To change description of fruit "lime" in in Fruits dictionary')
    fruits["lime"] = "great with tequilla"
    print(fruits)
    print()
    print('Deleting a Key "Apple" from fruits')
    del(fruits["apple"])
    print(fruits)
    print()
    print("Clearing the fruits dictionary")
    fruits.clear()
    print(fruits)

def find_description():
    print("To Find the description of a fruit")
    while True:
        dict_key = input("Please Enter Fruit name:\n")
        if dict_key == "quit":
            break
        if dict_key in fruits:
            description = fruits.get(dict_key)
            print(description)
        else:
            print("The details of {} doesn't exist".format(dict_key))

if __name__ == "__main__":
    print("""Select any one the below options
           1. To find the description of fruit
           2. To Display simple operation""")
    choice = input("Enter Your choice here: ")
    if choice == "1":
        print("*" * 120)
        find_description()
    elif choice == "2":
        print("*" * 120)
        simple_operation()