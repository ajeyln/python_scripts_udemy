def is_palindrome(string):
    return(string[::-1]).casefold() == string.casefold()

def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
        print(string)
    return is_palindrome(string)

word = input("Please input any word:")
if is_palindrome(word):
    print("'{}' is palindrome".format(word))
else:
    print("'{}' is not palindrome".format(word))