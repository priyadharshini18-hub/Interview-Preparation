# Given that integers are read from a data stream. Find the median of elements read so far in an efficient way.
# Time Complexity - Insertion of 1 data into heap : O(logn) Find Median : O(1)

import heapq

def add_data(max_h1, min_h2, data):
    if max_h1 and data > -max_h1[0] :
        heapq.heappush(min_h2, data)
    else :
        heapq.heappush(max_h1, -1 * data)

    # Balance the size of the heaps
    if len(max_h1) > len(min_h2) + 1 :
        heapq.heappush(min_h2, -1 * heapq.heappop(max_h1))
    elif len(min_h2) > len(max_h1) + 1 :
        heapq.heappush(max_h1, -1 * heapq.heappop(min_h2))

    find_median(max_h1, min_h2)

def find_median(max_h1, min_h2):
    if len(max_h1) > len(min_h2) :
        print('Median is ', -1 * max_h1[0])
    elif len(min_h2) > len(max_h1) :
        print('Median is ', min_h2[0])
    else :
        print('Median is ', (-1 * max_h1[0] + min_h2[0]) / 2)

# data_stream = [5, 15, 1, 3]
# data_stream = [2, 2, 2, 2]
data_stream = [3, 4, 10, 6, 8]

curr_data = []
max_h1 = [] # Max heap to store the 1st half of the data. POP : Max element before middle index
min_h2 = [] # Min heap to store the 2nd half of the data. POP : Min element after middle index

for data in data_stream :
    curr_data.append(data)
    print('Current data in the stream is ', curr_data)
    add_data(max_h1, min_h2, data)

