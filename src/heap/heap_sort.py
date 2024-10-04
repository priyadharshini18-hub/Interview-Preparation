# Heap Sort from Max Heap

# Build the heap using heapify
# Sort the built Max heap by swapping arr[0] and arr[n-1] and heapify again

def heapify(arr, n, index) :
    largest = index
    left = index * 2 + 1
    right = index * 2  + 2

    if left < heap_size and arr[largest] < arr[left] :
        largest = left

    if right < heap_size and arr[largest] < arr[right] :
        largest = right

    if largest != index :
        arr[largest], arr[index] = arr[index], arr[largest]
        heapify(arr, heap_size, largest) # To make sure curr largest is grater than its left and right children

def heapsort(arr, heap_size) :
    # Build the heap

    for i in range(heap_size // 2, -1, -1) :
        heapify(arr, heap_size, i) # Bottom up heapify

    print('Array after Heapify : ', arr)

    for i in range(heap_size-1, 0, -1) :
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0) # top down heapify

input = [12, 11, 13, 5, 6, 7]
heap_size = len(input)
print('Input Array : ', input)

# Heap sort
heapsort(input, heap_size)
print('Array after Heap sort : ', input)


