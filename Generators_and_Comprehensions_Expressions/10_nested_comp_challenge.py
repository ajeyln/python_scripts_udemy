# The challenge is to use a nested comprehension, to produce the same values.
# You can iterate over the list, to produce the same output as the for loop, or just print out the list.

for i in range(1, 11):
    for j in range(1, 11):
        print(i, i * j)

print("*" * 120)
for x, y in [(i, i * j) for i in range(1, 11) for j in range(1, 11)]:
    print(x,y)