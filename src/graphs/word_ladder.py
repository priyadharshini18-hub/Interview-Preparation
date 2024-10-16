# Word Ladder (127)

# Given two words, beginWord and endWord, and a dictionary wordList
# Return the number of words in the shortest transformation sequence from beginWord to endWord
# 0 if no such sequence exists

from collections import defaultdict
from queue import Queue

def create_adjacencyList(wordList, adj) : # Create a dict for every word as key and 1 letter diff words as value
    for i in wordList :
        for j in wordList :
            if i != j :
                letter_diff = 0
                for letter1, letter2 in zip(i, j) :
                    if letter1 != letter2 :
                        letter_diff += 1
                    if letter_diff > 1 :
                        break
                if letter_diff == 1 :
                    adj[i].append(j)

def bfs(source, target, adj) : # Calling BFS would always give the shortest path
    q = Queue()
    visited_word = set()
    q.put(source)
    count = 0
    res = []

    while not q.empty() :
        curr = q.get()
        visited_word.add(source)
        for neighbour in adj[curr] :
            if neighbour == target : # Stop and return the count if the target is reached
                return count
            if neighbour not in visited_word :
                q.put(neighbour)
                visited_word.add(neighbour)
                count +=1

    return count

# Input

wordList = ["hot","dot","dog","lot","log","cog"]
source = "hit"
target = "cog"

if target not in wordList :
    print('Target not found')

else:
    adj = defaultdict(list)
    wordList.append(source)
    create_adjacencyList(wordList, adj)

    for i in adj.items() :
        print(i)

    print('Shortest Transformation Count : ' , bfs(source, target, adj))