n =int(input("Enter the value: "))
for i in range (1, (n + 1)):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))

# Width is assigned after format {0:2} , where 0 is index and 2 is width of charecter
for i in range (1, (n + 1)):
   print("No. {0:2} squared is {1:4} and cubed is {2:6}".format(i, i ** 2, i ** 3))

# If we want the align the formated value to be in left align
for i in range (1, (n + 1)):
    print("No{0:2} squared is {1:<4} and cubed is {2:<5}".format(i, i ** 2, i ** 3))

# If we want the align the formated value to be from center
for i in range (1, (n + 1)):
    print("No.{0:2} squared is {1:^4} and cubed is {2:^5}".format(i, i ** 2, i ** 3))

# If we have decimal point in formatted value
# we can use {0:2.5f},Here 0 is index and 2 is space allocated to before decimal number and 5 is width after decimal point
print("Pi is approximately {0:12}".format(22 / 7)) # as default the python will take 15 charecters after decimal point
print("Pi is approximately {0:12f}".format(22 / 7)) # as default the python will take 15 charecters after decimal point
print("Pi is approximately {0:<12.50f}".format(22 / 7)) 
print("Pi is approximately {0:<52.50f}".format(22 / 7)) 
print("Pi is approximately {0:<62.50f}".format(22 / 7)) 
print("Pi is approximately {0:<72.50f}".format(22 / 7)) 


