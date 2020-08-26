numbers = [1 , 45 , 31 , 12, 60]

for number in numbers:
    if number % 8 == 0:
        # reject the list
        print("The numbers are unacceptable")
        break
else:
    print("All those numbers are acceptable")
   

# when low and high are same
low = int(input("Enter Lowest Number:\n"))
high = int(input("Enter Highest Number: \n"))
print("Please think the number between {} and {}".format(low,high))
guesses = 1
while low != high:
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
else:
    print("You thought of number {}" .format(low))
    print("The Compuer gussed it correct within {} guesses !" .format(guesses))
