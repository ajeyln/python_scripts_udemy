number = "9,223,372,036,854,775,807"
print(number.split(", "))
generated_lists = ['9',' ',
                   '2','2','3',' ',
                   '3','7','2',' ',
                   '0','3','6',' ',
                   '8','5','4',' ',
                   '7','7','5',' ',
                   '8','0','7',]
values = "".join(generated_lists)
print(values)
print()


values_list = values.split()
print(values_list)
print()

# use a for loop to produce a list of int rather than string
# we can either modify the contents of the "values_list" list in the place
# or create a new list of ints.

# replace the values in place
for index in range(len(values_list)):
    values_list[index] = int(values_list[index])

print(values_list)
print()

# create a new lists
integer_values = []
for value in values_list:
    integer_values.append(int(value))
print(integer_values)