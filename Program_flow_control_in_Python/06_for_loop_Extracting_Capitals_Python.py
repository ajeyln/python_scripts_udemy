#to separate number and special charecter from string
number = "9,223;372:036 854,775;807"
separators = ""
for char in number:
    if not char.isnumeric():
        separators = separators + char
print(separators)
values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
print(sum([int(val) for val in values]))

print("*" * 120 )
quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
 
# Use a for loop and an if statement to print just the capitals in the quote above.
for char in quote:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(char)

#write a program to prin out all the numbers from 0 to 100 are divisible by 7
# This solution uses a step value for the range function
for i in range(0, 101, 7):
    print(i)

# This solution uses a slice
for i in range(101)[::7]:
    print(i)

for i in range(0,100):
    if(i % 7) == 0:
        print(i)