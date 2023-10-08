# Initialize an empty list to store the words
word_list = []

# Open the text file for reading (replace 'your_file.txt' with your file's path)
with open('words.txt', 'r') as file:
    # Read each line from the file
    for line in file:
        # Strip leading and trailing whitespace and append to the list
        word_list.append(line.strip())

# Now, word_list contains the words from the file as separate list elements
# You can print the list or perform further operations on it
# print(word_list)
SOLVED = False
while not SOLVED:
    guess = input("What word did you guess:")
    resultLetter1 = input("What the first letter green, yellow or grey?:")
    resultLetter2 = input("What the second letter green, yellow or grey?:")
    resultLetter3 = input("What the third letter green, yellow or grey?:")
    resultLetter4 = input("What the fourth letter green, yellow or grey?:")
    resultLetter5 = input("What the fifth letter green, yellow or grey?:")
    if resultLetter1 == 'green':
        i=0
        while i<len(word_list):
            if word_list[i][0] != guess[0]:
                word_list.remove(word_list[i])
                i-=1
            i+=1
    if resultLetter2 == 'green':
        i=0
        while i<len(word_list):
            if word_list[i][1] != guess[1]:
                word_list.remove(word_list[i])
                i-=1
            i+=1
    if resultLetter3 == 'green':
        i=0
        while i<len(word_list):
            if word_list[i][2] != guess[2]:
                word_list.remove(word_list[i])
                i-=1
            i+=1
    if resultLetter4 == 'green':
        i=0
        while i<len(word_list):
            if word_list[i][3] != guess[3]:
                word_list.remove(word_list[i])
                i-=1
            i+=1
    if resultLetter5 == 'green':
        i=0
        while i<len(word_list):
            if word_list[i][4] != guess[4]:
                word_list.remove(word_list[i])
                i-=1
            i+=1
    if resultLetter1 == 'yellow':
        i=0
        while i < len(word_list):
            if guess[0] not in word_list[i]:
                word_list.remove(word_list[i])
                i-=1
            else:
                if word_list[i][0] == guess[0]:
                    word_list.remove(word_list[i])
                    i-=1
            i+=1
    if resultLetter2 == 'yellow':
        i=0
        while i < len(word_list):
            if guess[1] not in word_list[i]:
                word_list.remove(word_list[i])
                i-=1
            else:
                if word_list[i][1] == guess[1]:
                    word_list.remove(word_list[i])
                    i-=1
            i+=1
    if resultLetter3 == 'yellow':
        i=0
        while i < len(word_list):
            if guess[2] not in word_list[i]:
                word_list.remove(word_list[i])
                i-=1
            else:
                if word_list[i][2] == guess[2]:
                    word_list.remove(word_list[i])
                    i-=1
            i+=1
    if resultLetter4 == 'yellow':
        i=0
        while i < len(word_list):
            if guess[3] not in word_list[i]:
                word_list.remove(word_list[i])
                i-=1
            else:
                if word_list[i][3] == guess[3]:
                    word_list.remove(word_list[i])
                    i-=1
            i+=1
    if resultLetter5 == 'yellow':
        i=0
        while i < len(word_list):
            if guess[4] not in word_list[i]:
                word_list.remove(word_list[i])
                i-=1
            else:
                if word_list[i][4] == guess[4]:
                    word_list.remove(word_list[i])
                    i-=1
            i+=1
    

    if resultLetter1 == "grey":
        i=0
        while i < len(word_list):
            if guess[0] in word_list[i]:
                word_list.remove(word_list[i])
                i-=1
            i+=1
    if resultLetter2 == "grey":
        i=0
        while i < len(word_list):
            if guess[1] in word_list[i]:
                word_list.remove(word_list[i])
                i-=1
            i+=1
    if resultLetter3 == "grey":
        i=0
        while i < len(word_list):
            if guess[2] in word_list[i]:
                word_list.remove(word_list[i])
                i-=1
            i+=1
    if resultLetter4 == "grey":
        i=0
        while i < len(word_list):
            if guess[3] in word_list[i]:
                word_list.remove(word_list[i])
                i-=1
            i+=1
    if resultLetter5 == "grey":
        i=0
        while i < len(word_list):
            if guess[4] in word_list[i]:
                word_list.remove(word_list[i])
                i-=1
            i+=1
    print(word_list)
    state = input("did you solve it(y/n):")
    if state == "y":
        SOLVED = True