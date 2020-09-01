even = set(range(0, 40, 2))
print("Even Set is")
print(even)
squares_tuple = (4, 6, 9, 16, 25)
print("Squares set is")
print(squares_tuple)
squares =  set(squares_tuple)
print(squares)

def conv_tup_set():# Converting tuples to sets
    squares_tuple = (4, 6, 9, 16, 25) 
    squares = set(squares_tuple)
    print(squares)

def union_set(): # to union or add two Sets
    print("Even Set is")
    print(even)
    print("Length of even set is {}".format(len(even)))

    print("Squares set is")
    print(squares)
    print("Length of squares set is{}".format(len(squares)))
    
    print('Union between square and even')
    print(even.union(squares))
    print('Union between square and even')
    print(len(even.union(squares)))

def intsect_set(): # common items or intersection of two sets
    print("Even Set is")
    print(even)
    print("Squares set is")
    print(squares)

    print('Intersection between square and even')
    print(even.intersection(squares))
    print(even & squares)
    print("-" * 120)
    print('Intersection between square and even')
    print(squares.intersection(even))
    print(squares & even)

def diff_set(): #Difference between two sets
    print("Even Set is")
    print(even)
    print("Squares set is")
    print(squares)

    print("even minus squares")
    print(sorted(even.difference(squares)))
    print(sorted(even - squares))
    print("-" * 120)
    print("square minus even")
    print(squares.difference(even))
    print(squares - even)

def symm_set():# Symmetric Sets
    print("Even Set is")
    print(even)
    print("Squares set is")
    print(squares)

    print("Symmetric even minus squares")
    print(sorted(even.symmetric_difference(squares)))
    print("Symmetric squares minus even")
    print(squares.symmetric_difference(even))

def rem_discard_set():
    print("Squares set is")
    print(squares)

    squares.discard(4)
    print("After discarding 4 from squares sets")
    print(squares)
    print("-" * 120)
    squares.remove(16)
    print("After removing 16 from squares sets")
    print(squares)
    print("-" * 120)
    squares.discard(8) # no error, does nothing
    print("After discarding 8 from squares sets")
    print(squares)
    print("-" * 120)
    print("After discarding 8 from squares sets")
    try:
        squares.remove(8) # without try method, It shows error
    except KeyError:
        print("The item 8 is not a member of the set")

if __name__ == "__main__":
    print("""Please chose any of the operation on set
           1. Converting Tuple to set
           2. Union of two sets
           3. Intesection of two sets
           4. Difference between two sets
           5. Symmentric between two sets
           6. Discard and remove operations""")
    choice = input()
    if choice == "1":
        conv_tup_set()
    if choice == "2":
        union_set()
    if choice == "3":
        intsect_set()
    if choice == "4":
        diff_set()
    if choice == "5":
        symm_set()
    if choice == "6":
        rem_discard_set()
