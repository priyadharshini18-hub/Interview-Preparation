# Max Heap implementation using Array

def heapify(index, heap, heap_size):
    left = index*2 + 1
    right = index*2 + 2
    largest = index

    if left < heap_size and heap[left] > heap[largest] :
        largest = left
    if right < heap_size and heap[right] > heap[largest] :
        largest = right

    if heap[index] != heap[largest] :
        temp = heap[largest]
        heap[largest] = heap[index]
        heap[index] = temp
        heapify(largest, heap, heap_size) # Call Heapify again with the index of largest element
                                          # To make sure it is greater than its left and right children

# Heap Creation

heap = [5,6,8,9,2,10]
heap_size = len(heap)

print("Before Heapify : ")
print(heap)

for i in range(heap_size//2, -1, -1) : # Specify in range
                                       # START : Middle element
                                       # STOP : After reaching index 0
                                       # STEP : Decrement by 1
    heapify(i, heap, heap_size)

print("After Heapify : ")
print(heap)