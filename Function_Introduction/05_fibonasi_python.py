def fibonacci(n):
    # return the 'n'th fibonacci number
    if 0 <= n <= 1:
        return n

    num1,num2 = 0, 1
    result = None
    for fab in range(n - 1):
        result = num1 + num2
        num1 = num2
        num2 = result

    return result


number = int(input("Enter any number: "))

print(fibonacci(number))

for i in range(36):
    print(i,":", fibonacci(i))

