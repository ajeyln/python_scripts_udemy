# To make a second guess game using random method
import random
def method1(answer):
    guess = int(input("Guess the number between 1 to {}: \n". format(highest)))
    if guess == answer:
        print("You guessed it first time")
    else:
        if guess < answer:
            print("Guess the higher number")
        else:
            print("Guess the lower number")
        guess = int(input())
        if guess == answer:
            print("Well done, you guessed it")
        else:
            print("Sorry, you have not guessed correctly")

def method2(answer):
    guess = int(input("Guess the number between 1 to {}: \n". format(highest)))
    while guess != answer:
        if guess == answer:
            print("You guessed it first time")
        else:
            if guess < answer:
                print("Guess the higher number")
            else:
                print("Guess the lower number")
            guess = int(input())
            if guess == answer:
                print("Well done, you guessed it")
            else:
                print("Sorry, you have not guessed correctly")

if __name__ == "__main__":
        highest = 10
        answer = random.randint(1 , highest)
        print(answer) # TODO: Delete this line after testing
        print("Please chose one of the option ")
        print("1: Guesses only twice")
        print("2: Guess until you got an answer")
        cnt = int(input("Enter your choice: \n"))
        if cnt == 1:
            method1(answer)
        elif cnt ==2:
            method2(answer)
        else:
            pass

