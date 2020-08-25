age = int(input("How old are you? \n"))

# comparision with "and" condition
if age >= 16 and age <= 65:
    print("Have a good good day at work")
else:
    print("Enjoy you free time")
print("-" * 120)

# comparision with "0r" condition
if age <= 16 or age >= 65:
    print("Enjoy you free time")
else:
    print("Have a good good day at work")
print("-" * 120)


# simplified chain comaprision
if 16 <= age <= 65:
    print("Have a good good day at work")
else:
    print("Enjoy you free time")
