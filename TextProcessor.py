class TextProcessor:
    def wordExtractor(self, textString):
        '''Takes string, seperates it into words. Returns a list of those words.

        A word is defined as an alphanumeric string containing at least one
        character and no symbols but perhaps a dash (-) and/or apostrophe
        (' or ’). Currently, this function splits on a character-by-character
        basis, so double-dashes (--) will end up in the final output, even
        though this is not my intent in the long run.

        Examples:
        'Mr.' --> ['Mr']
        'S.T.A.C' --> ['S', 'T', 'A', 'C']
        '1,340.54' --> ['1', '340', '54']
        'Wow--I was impressed.' --> ['Wow--I', 'was', 'impressed']
        '''
        self.word = ''
        self.words = []
        for self.character in textString:
            # The rationale: Not all non-alphabetic characters appear outside of
            # words, for example: the hyphen in 'non-alphanumeric,' the
            # apostrophe in 'don't,' and the numbers in a word such as 'A19,'
            # which may designate a room number. It is my intent that this
            # function extracts words as humans read them from literature, in
            # their full form.
               # Characters:
            if (self.character.isalnum() or
               # Symbols:
                self.character == "'" or self.character == '’' or
                self.character == "-"):
                self.word += self.character
            # Ensures skipping of empty 'words'
            elif len(self.word) >= 1:
                self.words.append(self.word)
                self.word = ''
            else:
                continue
        return self.words
