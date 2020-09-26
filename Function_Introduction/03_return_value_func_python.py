import random

def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)

highest = 1000
answer = random.randint(1, highest)
print(answer)

guess = 0
print("Please guess number between 1 & {}".format(highest))

while guess != answer:
    guess = get_integer(":")

    if guess == 0:
        break
    elif guess == answer:
        print("You guessed it correct!")
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")