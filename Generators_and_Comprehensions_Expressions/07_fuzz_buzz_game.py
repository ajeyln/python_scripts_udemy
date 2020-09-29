# You need to print the value from 0 to 100
# whenever the number divisible by 3, then it should print as "fuzz"
# If the number is divisible 5, it should display as "buzz
# If the number id divided by 15, the result should be "fuzz_buzz"

# Simple method
for i in range(101):
    if i % 15 == 0:
        print("fuzz_buzz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print("fizz")
    else:
        print(i)

# for comprehension method
answer = ("fizz_buzz" if i % 15 == 0 else "buzz" if i % 5 == 0 else "fizz"
            if i % 3 == 0  else i for i in range (101))