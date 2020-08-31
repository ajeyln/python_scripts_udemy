# Simple Unpacking Tuple
x, y, z = 1,2,152
print((x,y,z))
print(x)  # Unpacking Tuple
print(y)
print(z)
print()

# Unpacking Tuple and assigning mutiple value to a variable
for t in enumerate("abcdefgh"):
    print(t)
print()

# Unpacking Tuple and assigning multiple value to variables
for t in enumerate("Ajeya Nayak"):
    index, name = t
    print("{}:{}".format(index,name))
print()


