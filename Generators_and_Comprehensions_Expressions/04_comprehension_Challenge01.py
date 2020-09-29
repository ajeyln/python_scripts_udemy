# to rewrite the codes in comprehension method , instead of a for loop ( it's mentioned in # comment section)

text = input("Please Enter a text:")

output = []
for x in text.split():
    output.append(len(x))
print(output)

# type your solution here
answer = [len(x) for x in text.split()]
print(answer)

# IT could be useful to store the original words in the list, as well.
# The for loop would look like this (note the extra parentheses, so that we get tuples in the list
output = []
for x in text.split():
    output.append((x, len(x)))
print(output)

# type your solution here

answer = [(x, len(x)) for x in text.split()]
print(answer)

# to avoid duplicate, we can use set comprehension instead list comprehension
answer = {(x, len(x)) for x in text.split()}
print(answer)