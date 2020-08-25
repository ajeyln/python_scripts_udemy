# in 
parrot = "Norwegin Blue"
letter = input("Enter a charecter: ")
if letter in parrot.capitalize(): # capitalize()- to make sentence upper case
    print("{} is in {}".format(letter,parrot))
else:
    print("I don't have that letter") 
print("*" * 120)

# not in
activity = input("What would you like you today? \n")
if "cinema" not in activity.casefold():# casefold() - to make sentence lower case
    print("But I want to go to Cinema ")
else:
    print("Can i Come with you?")