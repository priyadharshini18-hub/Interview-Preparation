# Given an array
# Transform the value into sum of all digits
# Repeat until array has single digit values
# Return the most frequent value in the array (if there is a tie return the higher value)

from collections import Counter

def sum_of_digits(data):
    return sum(int(d) for d in str(data))

def solution(readings):

    sum_array = []

    while True:
        sum_array.clear()
        all_single_digits = True  # Assume all numbers are single-digit until proven otherwise

        for i in range(len(readings)):
            if readings[i] >= 10:
                all_single_digits = False

            readings[i] = sum_of_digits(readings[i])
            sum_array.append(readings[i])

        if all_single_digits:
            break

    count = Counter(sum_array)

    most_frequent = max(count.items(), key=lambda x: (x[1], x[0]))  # Sort by frequency, then by value
    return most_frequent[0]


readings = [123, 456, 789, 234, 12, 56, 78]
result = solution(readings)
print("Most frequent sum of digits:", result)
