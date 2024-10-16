# Prefix Sum helps to
# Quickly find the sum of any subarray using just two array lookups
# Helps in reducing the time complexity of summing over subarrays from O(n) to O(1)

# Prefix sum in Array : O(n)

input = [-2, 0, 3, -5, 2, -1]
n = len(input)
prefix_sum = [0]*(n+1) # To indicate there are no elements to the left of input[0]

for i in range(n) :
    prefix_sum[i+1] = prefix_sum[i] + input[i]

print('Input array : ', input)
print('Prefix sum array : ', prefix_sum)

# Sum of an array in Range
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right

range = [(0,5), (1,4), (2,5)]
for i in range :
    left = i[0]
    right = i[1]
    sum = prefix_sum[right+1] - prefix_sum[left]
    print('Sum of elements in range ', left, ':' , right , ' = ', sum)

# Contiguous Array
# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1

ip = [1, 0, 1, 1, 1, 0, 0]
ip_len = len(ip)
pf = dict()
temp_sum = 0
longest = -1

for i in range(ip_len) :
    print('i=', i)
    if ip[i] == 1 :
        temp_sum += 1
    elif ip[i] == 0 :
        temp_sum -= 1

    if temp_sum == 0 and i+1 > longest :
        longest = i+1
        print(pf.items())
        print('longest', longest)
        continue

    if temp_sum not in pf :
        pf[temp_sum] = i
    else:
        if i - pf[temp_sum] > longest :
            longest = i - pf[temp_sum]


    print(pf.items())
    print('longest', longest)

print('Longest Contiguous Array Length is ', longest)






# In array of size N with all initial values as 0, Perform the given ‘m’ add operations of 100 from index ‘a’ to ‘b’
# Evaluate the highest element in the array
# An add operation adds 100 to all the elements from a to b (both inclusive)
