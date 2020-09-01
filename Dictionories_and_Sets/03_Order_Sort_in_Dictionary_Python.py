fruits = {
           "orange" :"a sweet,orange citrus fruit",
           "apple" :"good for making cider",
           "lemon" :"a sour,yellow citrus fruit",
           "grape" :"a small, sweet fruit growing in bunches",
           "lime" :"a sour,yellow citrus fruit",
           }

def display_wosort_key():
    print("Displaying description of a fruits without sorting Keys")
    for value in fruits:
        print(value + " - " + fruits[value])
        
def display_sort_key():
    print("Displaying description of a fruits with sorting Keys")
    ordered_keys = list(fruits.keys())
    ordered_keys.sort()
    for key in ordered_keys:
        print(key + " - " + fruits[key])

if __name__ == "__main__":
    print("""Choose any of the below
          1. Description without sortted Keys
          2. Description with sortted Keys""")
    choice = input()
    if choice == "1":
        display_wosort_key()
    elif choice == "2":
        display_sort_key()
    
