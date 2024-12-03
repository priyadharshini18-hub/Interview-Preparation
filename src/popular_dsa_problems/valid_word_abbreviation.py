'''
LeetCode 408 : Valid Word Abbreviation

A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths.
The lengths should not have leading zeros.

TC1

word : internationalization
abbr : i12iz4n
output : True

Explanation : "i nternational iz atio n"

TC2

word : apple
abbr : a2e
output : False

Explanation : "l" was missing in abbr

Following are not valid for the word SUBSTITUTION

s55n : " s ubsti tutio n"
s010n : Has leading zeros
s0ubstitution : Replaces an empty substring

'''

def check_abbr(word, abbr) :

    print('\nWord is', word)
    print('Abbreviation is', abbr)

    i = 0
    j = 0

    while i < len(word) and j < len(abbr) :
        if abbr[j].isdigit() :
            # To handle leading zero and empty substring
            if abbr[j] == '0' :
                print('Invalid Abbreviation')
                return
            skip = 0
            while abbr[j].isdigit() :
                skip = 10 * skip + int(abbr[j])
                j += 1
            i = i + skip

        elif word[i] != abbr[j] :
            print('Invalid Abbreviation')
            return
        else :
            i += 1
            j += 1

    print('Valid Abbreviation')
    return

word_list = ['internationalization', 'internationalization', 'apple', 'substitution', 'apple']
abbr_list = ['i12iz3n', 'i12iz4n', 'a2e', 's0ubstitution', 'a3e']

for word, abbr in zip(word_list, abbr_list) :
    check_abbr(word, abbr)



















