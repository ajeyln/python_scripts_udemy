# Delete the value which exclude between 100 and 200 
print("Deleting the value which is not in between 100 and 200")
data = [4,104,105,110,120,130,5,130,150,
        160,170,183.355,185,187,188,191,350,360]

min_valid = 100
max_valid = 200
sorted_data = sorted(data)


print("Deleting the value which is less than {}".format(min_valid))

# process the low values in the list
stop = 0
for index, value in enumerate(sorted_data):
    if value >= min_valid:
        stop = index
        break
print(stop)
del sorted_data[:stop]
print(sorted_data)
print()

# process the high values in the list
print("Deleting the value which is greater than {}".format(max_valid))

start = 0
for index in range(len(sorted_data) - 1 , -1 , -1):
    if sorted_data[index] <= max_valid:
        start = index + 1
        break
print(start)
del sorted_data[start:]
print(sorted_data)