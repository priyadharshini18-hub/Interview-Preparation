# Creation of Trie Data structure

from collections import defaultdict

class TrieNode :
    def __init__(self):
        # self.val = val
        self.children = defaultdict(TrieNode)
        self.end = False

class Trie :
    def __init__(self):
        self.root = TrieNode()

    def add_to_trie(self, word):
        curr = self.root
        for letter in word :
            if letter not in curr.children : # Check if the current letter is already a children
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.end = True # To indicate the completion of the word

    def print_trie(self, result, ans, node):

        if node.end == True :
            result.append(ans)
            if len(node.children) is not 0 :
                self.print_trie(result, ans, node.children[key])

        else :
            for key in node.children.keys() :
                ans = ans + str(key)
                self.print_trie(result, ans, node.children[key])

    def display(self):
        result = []
        self.print_trie(result, '', self.root)
        for w in result :
            print(w)





word_list = ['apple', 'app', 'alpha', 'application', 'bat', 'ball', 'cat', 'meow', 'mat']

trie = Trie()

# Creation of Trie
for word in word_list :yea
    trie.add_to_trie(word)

# Print all the words in Trie
print('Words in Trie :')
trie.display()
# trie.print_trie([], '', trie.root)

# Find if a word is present

# Print all words with prefix 'app'
