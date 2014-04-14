#!/usr/bin/python
# written in Python 3.3 by Marisa Smith (GitHub: @pparadigm)
# developed on Windows 8

# imports
# initialize global variables

       
# remove whitespace and unnecessary symbols from text
# tally words
# determine the case of a word
# store results


def wordExtractor():
    '''Extract words from a string by removing whitespace and unnecessary
       symbols.

       Note: will split numbers like 1,337 and 1.337 at the decimal and
       comma.'''
    word = ''
    words = []
    cut = False
    for character in rawText:
        # The rationale: Not all non-alphabetic characters appear outside of
        # words, for example: the hyphen in 'non-alphanumeric,' the apostrophe
        # in 'don't,' and the numbers in a word such as 'A19,' which may
        # designate a room number. It is my intent that this function extracts
        # words as humans read them from literature, in their full form.
           # Characters:
        if (character.isalnum() or
           # Symbols:
            character == "'" or character == '’' or character == "-"):
            word += character
        # Ensures skipping of empty 'words'
        elif len(word) >= 1:
            words.append(word)
            word = ''
        else:
            continue
    return words


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
        # Eventually have program check to see if file exists (except FileNotFoundError)
        filename = str(input("\nFile should be in the same "
                             "directory as this program.\n"
                             "Enter filename: "))
        fileToParse = open(filename, "r")
        rawText = fileToParse.read()
        break
    else:
        print("Invalid input. Restarting...\n")

wordList = wordExtractor()
