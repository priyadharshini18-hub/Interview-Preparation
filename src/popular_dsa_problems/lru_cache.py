# Least Recently Used (LRU) cache.

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity
# get(int key) : Return the value of the key if the key exists, otherwise return -1
# put(int key, int value) : Update / add the value to the cache and maintain capacity
# The functions get and put must each run in O(1) average time complexity

from collections import OrderedDict

def get_from_cache(cache, key) :
    if key in cache :
        cache.move_to_end(key)
        return cache[key]
    else :
        return -1

def put_to_cache(cache, cache_size, key, value) :
    if key in cache :
        cache.move_to_end(key)

    else :
        if len(cache) >= cache_size :
            cache.popitem(last=False) # First item is least recently used
        cache[key] = value

def print_cache(cache) :
    # print('Cache after put')
    for i in cache.items() :
        print(i)

operations = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
ip = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
cache_size = ip[0][0]

cache = OrderedDict() # To maintain the insertion order

for i in range(1, len(operations)) :
    if operations[i] == 'put' :
        print('PUT : ', ip[i][0])
        put_to_cache(cache, cache_size, ip[i][0], ip[i][1])
        print_cache(cache)

    elif operations[i] == 'get' :
        print('GET : ', ip[i][0])
        res = get_from_cache(cache, ip[i][0])
        if res != -1 :
            print('HIT in cache : ', res)
        else :
            print('MISS in cache')


# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

