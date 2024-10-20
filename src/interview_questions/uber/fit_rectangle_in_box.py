# You are given an operations array containing 2 operations:

# 1. [0,a,b] create and save rectangle of size axb
# 2. [1,a,b] answer the question : could every one of the earlier saved rectangles fit in the box of size axb.
# It is possible to rotate the rectangles by 90 degree - axb : bxa

# Note we are trying to fit each rectangle into the box separately
# Task is to return an array of Boolean representation to second type of operation in the order they appear

# Eg - [[0,1,3],[0,4,2],[1,3,4],[1,3,2]]
# Result- [true, false]

def can_fit_rectangles(operations):
    max_width = 0
    max_height = 0
    result = []

    for op in operations:
        if op[0] == 0:  # Save a rectangle
            a, b = op[1], op[2]
            width = max(a, b)
            height = min(a, b)

            # Update the max width and height encountered so far
            max_width = max(max_width, width)
            max_height = max(max_height, height)

        elif op[0] == 1:  # Query whether all rectangles fit in a box of size a x b
            a, b = op[1], op[2]
            box_width = max(a, b)
            box_height = min(a, b)

            # Check if the max width and height of any rectangle can fit in the box
            if max_width <= box_width and max_height <= box_height:
                result.append(True)
            else:
                result.append(False)

    return result


# Example usage
operations = [[0, 1, 3], [0, 4, 2], [1, 3, 4], [1, 3, 2]]
result = can_fit_rectangles(operations)
print(result)
