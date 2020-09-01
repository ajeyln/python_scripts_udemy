# create a program that takes some text and returns a list of
#all the charecters in the text that are not vowels, sorted in
#alphabetical order.

#You can either enter the text from the keyboard or
#initialise a string variable with string.

sampleText = "Python is a very powerful language"
vowels = frozenset("aeiou")
# vowels = {"a","e","i","o"."u"}
finalset = set(sampleText).difference(vowels)
print(finalset)

finallist = sorted(finalset)
print(finallist)
print("*" * 120)

# to find subset and superset
even = set(range(0, 40, 2))
print(even)
squares_tuples = (4, 6, 16)
squares = set(squares_tuples)
print(squares)

if squares.issubset(even):
    print("Squares is subset of even")
if even.issuperset(squares):
    print("even is superset of squares")
