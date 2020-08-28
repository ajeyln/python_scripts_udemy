available_parts = ["Computer", 
                   "Monitor", 
                   "Keyboard",
                   "Mouse",
                   "Mouse mat",
                   "hdmi cable"
                 ]
current_choice = "-"
computer_parts =  [] # create an empty list
valid_choice = [str(i) for i in range(1,len(available_parts) + 1)]
print(valid_choice)
while current_choice != "0":
    if current_choice in valid_choice:
        print("Adding {}".format(current_choice))
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            # it's already in, so remove it
            computer_parts.remove(chosen_part)
            print("Removing {}".format(chosen_part))
        else:
            print("Adding {}".format(chosen_part))
            computer_parts.append(chosen_part)
        print("Your list contain now {}".format(computer_parts))
    else:
        print("Please add from the list below:")
        for index,part in enumerate(available_parts): # enumerate function added
            print("{}:{}".format(index+ 1,part))
    current_choice = input("Enter your choice:\n")
else:
    print(computer_parts)