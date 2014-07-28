#!/usr/bin/python
# written in Python 3.3 by Marisa Smith (GitHub: @pparadigm)
# developed on Windows 8

import TextProcessor
# initialize global variables (if any)

    
# determine the case of a word
# store results


def tallier(listedWords):
    '''Count instances of each word.'''
    tallies = {}
    # Each time the for loop encounters a word, it will be recorded
    for instance in listedWords:
        if instance in tallies:
            tallies[instance] += 1
        else:
            tallies[instance] = 1
    return(tallies)


'''Program initialization loop: fetch raw text from user.'''
while True:
    # Have user choose between pasting and filename
    preference = str(input("Please select:\n"
                           "1. Paste text\n"
                           "2. Parse a .txt file.\n"
                           ">> "))
    if preference == "1":
        rawText = str(input("\nPlease paste text below:\n"))
        break
    elif preference == "2":
        try:
            filename = str(input("\nFile should be in the same "
                                 "directory as this program.\n"
                                 "Enter filename: "))
            fileToParse = open(filename, "r")
            rawText = fileToParse.read()
            break
        except FileNotFoundError:
            print("\nError: file not found. Check for correct spelling and "
                  "ensure that the file you are intending to use is in the "
                  "proper directory.\n")
    else:
        print("Invalid input. Restarting...\n")


def main():        
    process = TextProcessor.TextProcessor()
    wordList = process.wordExtractor(rawText)
    rawCounts = tallier(wordList)

    
main()
