def read_file():
    poem = open("Avva_Mother_Lankesh.txt","r")
    for line in poem:
        print(line)
    with open("Avva_Mother_Lankesh.txt","r") as poem:
        line = poem.readline()
        while line:
            print(line,end="")
            line = poem.readline()

def find_word_file():
    with open("Avva_Mother_Lankesh.txt","r") as poem:
        word = input("Enter Your word in the poem:\n")
        print('Your word "{0}" is in line'.format(word))
        for line in poem:
            if word in line.lower():
                print(line,end="")

def display_string_line_reverse():
    with open("Avva_Mother_Lankesh.txt","r") as poem:
        lines = poem.readlines() # read the entire line and reverse
        print(lines)
    print("*" * 120)
    print("The Charecter and line in the Poem in reverse order")
    for line in lines:
            print(line[::-1],end="")

def display_line_reverse():
    with open("Avva_Mother_Lankesh.txt","r") as poem:
        lines = poem.read() # read the string in the reverse and reverse
    print(lines)

    print("The Charecter and line in the Poem in reverse order")
    for line in lines:
        print(line[::-1],end="")

if __name__ == "__main__":
    print("""Please chose any of the following
           1. Display content in the File
           2. Display the line which contains the word
           3. Display the line in reverse order
           4. Display both line and string in reverse order""")
    choice = input()
    if choice in "1234":
        if choice == "1":
            read_file()
        elif choice == "2":
            find_word_file()
        elif choice == "3":
            display_line_reverse()
        else:
            display_string_line_reverse()


