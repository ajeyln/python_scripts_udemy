even = [2, 4 , 6, 8]
odd = [1, 3, 5, 7, 9]

# adding 2 list
even.extend(odd)
print(even)
another_even = even
print(another_even)

#sorting
even.sort() # sorting 
even.sort(reverse=True)# sorting in reversing order
print(another_even)
print(even)