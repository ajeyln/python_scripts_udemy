""" write a function called factorial, that will produce the factorial of the number passed as its argument.
You must include a Docstring and function annotation. in your function.

Print the first 36 factorial (0 to 35)"""
def factorial(n: int) -> int:
    """Return n! (0! is 1)."""
    if n <= 1:
        return 1

    result = 2
    for x in range(3, n + 1):
        result *= x

    return result


for i in range(36):
    print(i, factorial(i))