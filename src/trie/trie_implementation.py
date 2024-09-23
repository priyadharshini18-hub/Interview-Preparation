# Creation of Trie Data structure

from collections import defaultdict

class TrieNode :
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False

class Trie :
    def __init__(self):
        self.root = TrieNode()

    def insertion(self, word):
        curr = self.root
        for letter in word :
            if letter not in curr.children :
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.end = True

    def search_word(self, word):
        curr = self.root
        for letter in word :
            if letter not in curr.children :
                print(word + ' is not found in Tire')
                return
            curr = curr.children[letter]
        if curr.end == True :
            print(word + ' is found in Tire')
        else :
            print(word + ' is not found in Tire')

    def prefix_word_list(self, prefix):
        word = ''
        curr =  self.root
        for letter in prefix :
            if letter not in curr.children :
                print('Prefix - ' + prefix + ' not found in Trie')
                return None
            curr = curr.children[letter]
        print('\nPrefix wordlist :')
        self.prefix_helper(word, curr, prefix)

    def prefix_helper(self, word, curr, prefix):
        if curr.end == True:
            print(prefix+word)
        for child in curr.children :
            self.prefix_helper(word + str(child), curr.children[child], prefix)


word_list = ['apple', 'app', 'alpha', 'application', 'bat', 'ball', 'cat', 'meow', 'mat']

trie = Trie()
for word in word_list :
    trie.insertion(word)

# Find a word in Trie
trie.search_word('app')
trie.search_word('priya')

# Prefix words
trie.prefix_word_list('app')





