import sys

def getin(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Enter value is not correct, Please enter again")
        except EOFError:
            sys.ext(1)

first_number = getin("Please enter first number")
second_number = getin("Please enter second number")

try:
    print("{} divided by {} is {}".format(first_number,second_number,first_number / second_number))
except ZeroDivisionError:
    print("The number cannot be divided by zero")

sys.exit(2)
