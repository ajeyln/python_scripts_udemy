available_parts = ["Computer", 
                   "Monitor", 
                   "Keyboard",
                   "Mouse",
                   "Mouse mat",
                   "hdmi cable"
                 ]
current_choice = "-"
computer_parts =  [] # create an empty list

while current_choice != "0":
    if current_choice in "123456":
        print("Adding {}".format(current_choice))
        if current_choice == "1":
            computer_parts.append("Computer")
        elif current_choice == "2":
            computer_parts.append("Monitor")
        elif current_choice == "3":
            computer_parts.append("Keyboard")
        elif current_choice == "4":
            computer_parts.append("Mouse")
        elif current_choice == "5":
            computer_parts.append("'Mouse mat")
        elif current_choice == "6":
            computer_parts.append("HDMI cable")
    else:
        print("Please add from the list below:")
        for index,part in enumerate(available_parts): # enumerate function added
            print("{}:{}".format(index+ 1,part))
    current_choice = input("Enter your choice:\n")
else:
    print(computer_parts)

# enumerate example 2
print()
for index, char in enumerate("abcdefg"):
    print("{}:{}".format(index,char))