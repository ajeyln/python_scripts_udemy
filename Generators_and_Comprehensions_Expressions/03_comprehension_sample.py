print(__file__)
numbers = [1, 2, 3, 4, 5, 6]
squares = ([number ** 2 for number in numbers])
print(squares)
print("*" * 120)
text = "Have you ever failed in german exam"
# to make a list with capitalizing each charecter t

capitals = [char.upper() for char in text]
print(capitals)
print("*" * 120)

words = [word.upper() for word in text.split(" ")]
print(words)
print("*" * 120)

number = int(input(" Please Enter the number, for which i will tell the square: "))
squares = ([number ** 2 for number in numbers] )

index_pos = numbers.index(number)
print(squares[index_pos])