# To make a second guess game using if. elif and else condition
answer = 6
def method1():
    guess = int(input("Guess the number between 1 to 10 \n"))
    if guess < answer:
        print("Guess the higher number")
        guess = int(input())
        if guess == answer:
            print("Well done, you guessed it")
        else:
            print("Sorry, you have not guessed correctly")
    elif guess > answer:
        print("Guess the lower number")
        guess = int(input())
        if guess == answer:
            print("Well done, you guessed it")
        else:
            print("Sorry, you have not guessed correctly")
    else:
        print("You guessed it first time")

#method 2
def method2():
    guess = int(input("Guess the number between 1 to 10 \n"))
    if guess != answer:
        if guess > answer:
            print("Guess the lower number")
        else:
            print("Guess the higher number")
        guess = int(input())
        if guess == answer:
            print("Well done, you guessed it")
        else:
            print("Sorry, you have not guessed correctly")
    else:
        print("You guessed it first time")

#method 3
def method3():
    guess = int(input("Guess the number between 1 to 10 \n"))
    if guess == answer:
        print("You guessed it first time")
    elif guess < answer:
        print("Guess the higher number")
    else:
        print("Guess the lower number")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")

if __name__ == "__main__":
    method1()
    print("*" * 120)
    method2()
    print("*" * 120)
    method3()