""" Write a function to calculate the sum of all numbers passed as it's arguments.
Your function should be called as sum_number and should take a single argument : the value to sum up to.
To pass in this on-line interpreter, your function must contain a Docstring
The parameter and return value must be annotated. Be careful here, you may want to review the lecture
Function annotation """


def sum_numbers(*args: float) -> float:
    """ calculates the sum of all the numbers passed as arguments """
    result = 0
    for arg in args:
        result += arg
    return result

print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))