# Product of min and max in a dataset

# Algo : Fast access to min and max elements : HEAP
# For every push -> add to min_heap and max_hep (neg value for max_heap, since default is min_heap from heapq library)
#     Also add the element to present set()
# For every pop -> remove from present : No direct way to remove from heapq
# Remove the stale elements from min_heap and max_heap
#     We only care about the element in index 0, so run the loop until the element at 0 is not in present
# Calculate the product


import heapq

x = [1,2,3,1]
operations = ['push', 'push', 'push', 'pop']
product = []
min_heap = []
max_heap = []
present = set()


for i in range(len(operations)) :
    if operations[i] == 'push':
        heapq.heappush(min_heap, x[i])
        heapq.heappush(max_heap, -x[i])
        present.add(x[i])

    elif operations[i] == 'pop' :
        # We cannot directly pop an element from heapq
        if x[i] in present :
            present.remove(x[i])

    while min_heap and min_heap[0] not in present : # We care only about the largest and smallest element at index 0
        heapq.heappop(min_heap)

    while max_heap and -max_heap[0] not in present :
        heapq.heappop(max_heap)

    if min_heap and max_heap :
        product.append(min_heap[0] * -max_heap[0])
    else :
        product.append(0)

    print(min_heap)
    print(max_heap)

print('Product of min and max in a dataset = ', product)

# Testcase 1
# x = [1,2,3,1]
# operations = [push, push, push, pop]
# return [1,2,3,6]

# Explanation :
# push 1 : [1]      -> min * max = 1
# push 2 : [1,2]    -> min * max = 2
# push 3 : [1,2,3]  -> min * max = 3
# pop 1 : [2,3]     -> min * max = 6

# Testcase 2
# x=[3,2]
# operations=[push,push]
# return [9,6]

# Explanation :
# push 3 : [3]      -> min * max = 9
# push 2 : [3,2]    -> min * max = 6

