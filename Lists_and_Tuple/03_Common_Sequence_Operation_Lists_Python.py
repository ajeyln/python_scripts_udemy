shoping_list = ["milk", 
                "pasta", 
                "eggs",
                "spam",
                "bread"
                "rice"
                 ]

another_list = shoping_list
print(id(shoping_list))
print(id(another_list))

print()
shoping_list += ["cookies"]
print(id(shoping_list))
print(id(another_list))

a = b = c = d = e = f = another_list
print(a)
print("Adding cream")
b.append("cream")
print(c)
print(d)

# simple sequence Operations
print()
even = [2, 4 , 6, 8]
odd = [1, 3, 5, 7, 9]

# to find min and max
print(min(even))
print(max(even))
print(min(odd))
print(max(odd))
print()

# to find the number of digit in list
print(len(even))
print(len(odd))
print()

# to find the count of letters
print("mississippi".count("iss")) # to find the count the string "iss"