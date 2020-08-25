#To check whether old enough to vote
print("To check whether old enough to vote")
name = input("Enter Your Name:")
age = int(input("How old are you? {}: ".format(name)))
# method 1
if age >= 18:
    print("{}, You are old enough to vote".format(name))
else:
    print("{},  Please come back after {} years".format(name, (18 - age)))
print()
# method 2
if age < 18:
    print("{},  Please come back after {} years".format(name, (18 - age)))
else:
    print("{}, You are old enough to vote".format(name))
print("*" * 120)

# To make a guess game using if. elif and else condition
answer = 8
guess = int(input("Guess the number between 1 to 10 \n"))
if guess < answer:
    print("Guess the higher number")
elif guess > answer:
    print("Guess the lower number")
else:
    print("You guessed it first time")
print("*" * 120)


# small program  to compare two tree names
print("to compare two tree names")
tree1 = input('put your first tree name here: ')
tree2 = input('put your second tree name here:')
 
# comparing the trees names
if tree1 == tree2:
    print("The tress are the same")
else:
    print("The trees are different")
print("*" * 120)

# to compare two numbers
print("to compare two numbers")
x = int(input("Enter first Number:"))
y = int(input("Enter second Number:"))
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is smaller than y")
else:
    print("x equals y")

