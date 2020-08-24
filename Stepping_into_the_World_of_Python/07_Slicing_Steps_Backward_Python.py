# Displaying Charecters by Slicing by steps and backward method
#         012345678901234
parrot = "Norwegian Blue"
print(parrot[0:6:2]) # Nre
print(parrot[0:6:3]) # Nw

numbers = "9,223;372:036 854 775;807"
separators = numbers[1::4]
print(separators)
values = "".join (char if char not in separators else " " for char in numbers).split()
print([int(val) for val in values])
print()

# If we want to display the charecter in reverse order (backward)
letters = "abcdefghijklmnopqrstuvwxyz"
print(letters[25:0:-1]) # -1 Display the charecters one step backward
print(letters[25::-1])
print(letters[::-1]) # Here start value becomes the last index and end value first index as steps in backward

# Create a slice that produce the charecter qpo
print(letters[16:13:-1])
print(letters[-10:13:-1])
print(letters[-10:-13:-1])
print()

# Create a slice to produce edcba
print(letters[4::-1])
print(letters[-22::-1])
print()

# Slice the string to produce the last 8 charecter in reverse order
print(letters[:-9:-1])