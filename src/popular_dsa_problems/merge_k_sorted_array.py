# Merge k Sorted Arrays in O(k)

import heapq

arr = [[20, 50, 80], [10, 40, 70], [30, 60, 90]] # Already sorted
k = len(arr)
merged_arr = []

heap = []

for i in range(k) :
    heapq.heappush(heap, (arr[i][0], i, 0))

while heap :
    min_value = (heapq.heappop(heap))
    merged_arr.append(min_value[0])
    if min_value[2]+1 < len(arr[min_value[1]]) :
        heapq.heappush(heap, (arr[min_value[1]][min_value[2]+1], min_value[1], min_value[2]+1 ))

print('Merged Array : ', merged_arr)

