import sys

def my_range(n: int):
    print("My_range starts")
    start = 0
    while start < n:
        print("my_range is running {}".format(start))
        yield start
        start += 1

_=input("line 11")
big_range = my_range(5)
_=input("line 15")

print("big_range is {} bytes".format(sys.getsizeof(big_range)))

#create a list containing all the values in big_range
big_list = []

for val in big_range:
    _=input("line 21 - inside loop")
    big_list.append(val)

print("big_list is {} bytes".format(sys.getsizeof(big_list)))
print(big_range)
print(big_list)