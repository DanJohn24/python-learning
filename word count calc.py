def wordCount(word):
    myFile = open("example1.txt")

    read = myFile.read()

    splitter = read.split()

    counter = 0

    for n in splitter:
        if (n == word):
            counter += 1
    return counter

    myFile.close()

word = input("Please input word: ")

print(wordCount(word))
