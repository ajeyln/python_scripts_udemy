# separator in list
name = "Ajey"
age = "29"

print(name,age,"Bangalore",2020)
print(name,age,"Bangalore",2020, sep = ", ") # If want to separate list of item with ,
print()

# joining items in list
flowers = [ 
           "Daffodil",
           "Evening primrose",
           "Hydrangea",
           "Lavender",
           "Sunflower",
           "Tiger Lily",
]
print(flowers)
separator = "|"
output = separator.join(flowers)
print(output)
print()

# Spliting the string to lists
panagram = "The quick brown fox jumps over the lazy dog "
print(panagram)

words = panagram.split()
print(words)
print()

number = "9,223,372,036,854,775,807"
print(number.split(", "))
