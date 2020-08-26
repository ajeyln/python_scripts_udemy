# to check the square of 9 numbers
i = 0
while i < 10:
    print("{} of square is {}".format(i, i * i))
    i += 1

# to execute the direction
available_exists = ["north","south","east","west"]
chose_exit = ""
while chose_exit not in available_exists:
    chose_exit = input("Please chose a direction: \n")
    if chose_exit.casefold() == "quit":
        print("Game over")
        break
print("aren't you glad you got out of there")