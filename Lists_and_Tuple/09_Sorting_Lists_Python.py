pangram = "The quick brown for jumps over the lazy dog"

letters = sorted(pangram) # to sort charecters in variable pangram
print()

#sorting numbers in variable in Temporary base
numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers =  sorted(numbers)
print(sorted_numbers)
print(numbers)
print()

#sorting numbers in variable permanent base
numbers.sort()
print(numbers)
print()

# sorting the string 
missing_letter = sorted("The quick brown fox jumped over the lazy dog")
print(missing_letter)

# Sorting the charecters without case sensitiv issue
missing_letter = sorted("The quick brown fox jumped over the lazy dog", key = str.casefold) 
print(missing_letter)

# Sorting the string
names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"
         ]
names.sort(key =  str.casefold)
print(names)



