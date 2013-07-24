# written in Python 3.3 by Prime Paradigm (@pparadigm on GitHub)
# developed on a Win7 system
# last updated July 24, 2013 @ 11:14AM
#
# "FEATURES" TO IMPLEMENT
#
# 1. FIX It's AND it's BUG!!!! i.e. they count as two separate words, and
#    really shouldn't (NOTE: This has to do with the fact that "It's" in
#    titlecase returns "It'S")
# 2. Fix decending numerical frequency sort problems, i.e.: they don't get
#    sorted
# 3. Figure out what to do with "words" like "./././." or "..."; they cause the
#    program not to complete.
# 4. Figure out why falsetruths.txt is processed without issue, while
#    poisonbelt.txt is not.
#
# ---------

#!/usr/bin/python


roughCuts = []
secretDict = {}
wordFreq = {}
outputStr = ""
a = ""
abcCount = []
numCount = []
rawCount = []
nonAlnumChecklist = []


def main(out):
    caseFixer(cutCleaner(stringer()))
    outputDoc = open("wordfrequencies.txt", "w")
    fullCount = "Total number of unique words: " + str(len(wordFreq))
    for word in wordFreq.keys():
        outputLine = "%s x %s"%(word, wordFreq[word])
        out = "%s\n%s"%(outputLine, out)
    outputDoc.write("%s\n\n%s"%(fullCount, out))
    outputDoc.close()
    sorter()
    

# allows user to choose between a file input or pasting
def stringer():
    q = str(input("""
Please select:
1. Paste text
2. Parse a .txt file
"""))
    if q == "1":
        a = str(input("\nPaste text to check for word frequency below:\n"))
        return splitter(a)
    elif q == "2":
        fname = input("\nFile should be in the same directory as this program.\
                      \nEnter filename:\n")
        toParse = open(fname, "r")
        a = toParse.read()
        return splitter(a)
    else:
        print("Invalid response. Restarting.")
        stringer()


# removes spaces, newlines, doubledashes, and tabs, and returns a list
def splitter(a):
    print("\n\nGathering words...")
    for part in a.split(" "):
        for x in part.split("\n"):
            for y in x.split("--"):
                for char in y.split("\t"):
                    roughCuts.append(char)
                    for item in roughCuts:
                        if len(item) == 0:
                             roughCuts.remove(item)
# commented out until I understand why I put it in in the first place, or until
# I deem it useless
#
##                        elif not item.isalnum():
##                            count = len(item)
##                            for check in range(0,count):
##                                if item[check].isalnum():
##                                    nonAlnumChecklist.append(True)
##                                else:
##                                    nonAlnumChecklist.append(False)
##                            if not any(nonAlnumChecklist):
##                                roughCuts.remove(item)
    print("Done.")
    return roughCuts
    

# cutCleaner takes the roughCuts list, cleans the strings of unwanted 
# characters, lowercases titlecased words (while tracking them), and
# tallies the words
def cutCleaner(cuts):
    print("\nBeginning text-cleaning process...")
    for word in cuts:
        if word in wordFreq:
            wordFreq[word] = wordFreq[word] + 1
        elif not word[0].isalnum() or not word[-1].isalnum():
            if word == "":
                cuts.remove(word)
            else:
                while not word[0].isalnum():
                    word = word[1:]
                    if word == "":
                        cuts.remove[word]
                while not word[-1].isalnum():
                    word = word[:-1]
                    if word == "":
                        cuts.remove[word]
                if word[0].istitle():
                    titleCase(word)
                elif word in wordFreq:
                    wordFreq[word] = wordFreq[word] + 1
                else:
                    wordFreq[word] = 1
        else:
            if word.istitle():
                titleCase(word)
            else:
                wordFreq[word] = 1
    print ("Done.")
    return wordFreq, secretDict


# deals with pesky capitalization and counts
def titleCase(word):
    check = word.lower()
    if wordFreq.get(check, 0):
        wordFreq[check] = wordFreq[check] + 1
        if word in secretDict:
            secretDict[word] = secretDict[word] + 1
        else:
            secretDict[word] = 1
    else:
        wordFreq[check] = 1
        if secretDict.get(word, 0):
            secretDict[word] = secretDict[word] + 1
        else:
            secretDict[word] = 1


# re-capitalizes proper nouns, if they show up only as titlecased in the text
def caseFixer(dicTup):
    print("\nMaking sure always-capitalized nouns are capitalized...")
    wordDty = dicTup[0]
    secretDty = dicTup[1]
    for element in secretDty:
        if secretDty[element] == wordDty[element.lower()]:
            wordDty[element] = wordDty[element.lower()]
            del wordDty[element.lower()]
        else:
            pass
    print("Done.")
            

# allows the user to sort the file generated by the main in a specified manner
def sorter():
    a = eval(input("""\n\nCounting complete.\n
How would you like the results sorted?
1. alphabetical by word
2. descending numerical order by frequency
3. no sort\n"""))
    if a == 1:
        raw = open("wordfrequencies.txt", "r")
        for line in raw.readlines():
            abcCount.append(line)
        raw.close()
        abcCount.remove(abcCount[0])
        abcCount.remove(abcCount[1])
        abcCount.sort()
        abcFreq = open("wordfrequencies.txt", "w")
        abcFreq.write("Total number of unique words: " + str(len(abcCount)) + \
                      "\n\n")
        for item in abcCount:
            abcFreq.write(item)
        print("\nThe list has been sorted alphabetically. You can access the results by opening the wordfrequencies.txt file in the directory in which this program resides.")
    elif a == 2:
        raw = open("wordfrequencies.txt", "r")
        for line in raw.readlines():
            numCount.append(line)
        raw.close()
        numCount.remove(numCount[0])
        numCount.remove(numCount[1])
        sorted(numCount, reverse = True)
        numFreq = open("wordfrequencies.txt", "w")
        numFreq.write("Total number of unique words: " + str(len(numCount)) + \
                      "\n\n")
        for item in numCount:
            numFreq.write(item)
# debugging
##        print(numCount)
        print("\nThe list has been sorted numerically. You can access the results by opening the wordfrequencies.txt file in the directory in which this program resides.")
    elif a == 3:
        print("\nNo sort performed. You can access the results by opening the wordfrequencies.txt file in the directory in which this program resides.")
    else:
        print("Invalid input. Restarting.")
        sorter()
        
main(outputStr)
