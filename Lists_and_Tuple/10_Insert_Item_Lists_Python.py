computer_parts = ["computer",
                  "Monitor",
                  "Keyboard",
                  "Mouse",
                  "Speaker",
                  "USB"
                  ]
print(computer_parts)

# If we want to replace the item in 4th position  with "trackball" in computer_parts
computer_parts[3] = "trackball"
print(computer_parts)
print()

# If we want to delete the items from 5 to till end and add an item  "hdmi cable" in computer_parts
# if we want to delete more than 2 position and add an item in variable then we need enclose the item within []
computer_parts[4:] = ["HDMI Cable"]
print(computer_parts)
print()

#if we are not enclocing the item within []
computer_parts[4:] = "HDMI Cable"
print(computer_parts)


