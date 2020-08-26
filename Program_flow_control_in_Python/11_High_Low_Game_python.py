low = int(input("Enter Lowest Number:\n"))
high = int(input("Enter Highest Number: \n"))
print("Please think the number between {} and {}".format(low,high))
print("Press Enter to start")
guesses = 1
while True:
    print("\tNow, Guessing number between {} and {} by computer".format(low,high))
    guess = low + (high - low) // 2
    indicator = input("Computer's guess is {}. Should computer guess higher or lower ? Enter h  for high , l  for Low . If the answer is correct type c \n". format(guess)).casefold()
    if indicator == "h" :
        #Guess Higher,The low end of the range becomes 1 greater than the guess
        low = guess + 1
    elif indicator == "l":
        #Guess Lower,The high end of the range becomes 1 lesser than the guess
        high = guess - 1
    elif indicator == "c":
        print("The Compuer gussed it correct within {} guesses !" .format(guesses))
        break
    else:
        print("Please enter h,l or c")
    guesses += 1

    

    