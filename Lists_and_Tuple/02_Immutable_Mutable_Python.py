print("Immutable Objects Examples")
# The id of String, int and boolean can't be changed and the id of new variable created with same data won't be changed
result = True
another_result = result
print(id(result)) # the id of variable result and another_result can't be changed
print(id(another_result))
print()

result = False # boolean
print(id(result))
print()

result = "Correct" # String
another_result = result 
print(id(result))
print(id(another_result))
print()

# if the we cahnage the data in variable the id will get changed
result += "ish"
print(id(result))
print(id(another_result))
print()


print("Mutable Objects Examples")
# the data of list,dict & set can be changable, But id of the variable cannt be changed
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