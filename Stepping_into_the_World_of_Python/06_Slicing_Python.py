# Displaying Charecters by slicing with positive and negative index number
#         012345678901234
parrot = "Norwegian Blue"
print(parrot[0:6]) # Norweg
print(parrot[3:5]) # we
print(parrot[0:9]) #Norwegian
print(parrot[:9]) #Norwegian , Start Value is empty

print(parrot[10:14]) #Blue
print(parrot[10:]) #Blue , End Value is empty

print(parrot[:6])
print(parrot[6:])

print(parrot[:6] + parrot[6:]) # Concatination of two sliced string
print(parrot[:]) # what if start and end value is empty

# Slicing through Negative indexing
print(parrot[0:6]) # Norweg, Used Postive index number
print(parrot[-14:-8]) # Norweg, used Negative index number

print(parrot[-4:-2]) #Bl 
print(parrot[-4:12]) #Bl







