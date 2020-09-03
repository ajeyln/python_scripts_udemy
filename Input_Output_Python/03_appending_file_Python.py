# Write a program to append the times table to our jabberwocky poem 
# in sample.txt. We want the table from 2 to (similar to the output
# from the For loops part 2 lecture in section 6)
#
# The first colum of the number should be right justified. As an example,
#the 2 times table should took like this:
#  1 times 2 is 2
#  2 times 2 is 4
#  3 times 2 is 6
#  4 times 2 is 8
#  5 times 2 is 10
#  6 times 2 is 12
#  7 times 2 is 14
#  8 times 2 is 16
#  9 times 2 is 18
# 10 times 2 is 20
# 11 times 2 is 22
# 12 times 2 is 24

with open("Sample.txt","w") as number_file:
    for i in range(1,3):
        for j in range(1,13):
            print("{0:>2} times {1} is {2}".format(j,i, j * i),file=number_file)
        print("-" * 120,file=number_file)

#appending the data to file sample..txt
with open("Sample.txt","a") as number_file:
    for i in range(3,13):
        for j in range(1,13):
            print("{0:>2} times {1} is {2}".format(j,i, j * i),file=number_file)
        print("-" * 120,file=number_file)
