# to display the multiplication table from 1 to 20
for i in range(1,21):
    for j in range(1,21):
        print("{0} times {1} is {2}" .format(i,j,i*j))
    print("-" * 100)