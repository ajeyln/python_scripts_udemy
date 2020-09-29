# Generate Fibonacci Number
def fibonacci():
    current,previous = 0,1
    while True:
        yield current
        current,previous = current + previous, current

fib = fibonacci()

# To generate first 21 fibonacci numbers
for i in range (21):
    print("{}: {}" .format(i+1,next(fib)))
print("*" * 120)

# to generate pi
def odd_number():
    n = 1
    while True:
        yield n
        n += 2

def pi_series():
    odd = odd_number()
    approximation = 0
    while True:
        approximation += (4 / next(odd))
        yield approximation
        approximation -= (4 / next(odd))
        yield approximation 

approx_pi = pi_series()

for i in range(100000):
    print(next(approx_pi))