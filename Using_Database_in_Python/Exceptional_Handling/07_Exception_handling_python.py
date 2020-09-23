def factorial(num):
# to find the factorial of n number
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)

if __name__ == "__main__":
    num = int(input("Please enter a number:"))
    try:
        print(factorial(num))
    except (RecursionError):
        print("We are not find the factorial for large number")

    print("Program Terminated")
