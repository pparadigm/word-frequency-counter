#!/usr/bin/python
# written in Python 3.3 by Marisa Smith (GitHub: @pparadigm)
# developed on Windows 8

# imports
# initialize global variables

       
# remove whitespace and unnecessary symbols from text
# tally words
# determine the case of a word
# store results


'''Fetch raw text from user.'''
while True:
    # have user choose between pasting and filename
    preference = str(input("Please select:\n"
                           "1. Paste text\n"
                           "2. Parse a .txt file.\n"
                           ">> "))
    if preference == "1":
        rawText = str(input("\nPlease paste text below:\n"))
        break
    elif preference == "2":
        # eventually have program check to see if file exists (except FileNotFoundError)
        filename = str(input("\nFile should be in the same "
                             "directory as this program.\n"
                             "Enter filename: "))
        fileToParse = open(filename, "r")
        rawText = fileToParse.read()
        break
    else:
        print("Invalid input. Restarting...\n")
