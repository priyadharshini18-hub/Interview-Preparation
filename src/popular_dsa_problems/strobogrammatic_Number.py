# Strobogrammatic Number

# rotated_numerals = [0, 1, -1, -1, -1, -1, 9, -1, 8, 6]
# num = '18088'
# left, right = 0, len(num) - 1
#
# while left <= right:
#     left_numeral, right_numeral = int(num[left]), int(num[right])
#     if rotated_numerals[left_numeral] != right_numeral:
#         print('no')
#         exit()
#     left += 1
#     right -= 1
# print('yes')

rotated = {0, 1, 8, 6, 9}
num = ['18088', '69', '111', '962', '8', '8180']

for n in num :
    left = 0
    right = len(n) - 1
    strobo = 0

    while left <= right :
        left_ch = int(n[left])
        right_ch = int(n[right])

        if left_ch not in rotated or right_ch not in rotated :
            strobo = 1
            break

        if (left_ch == 6 and right_ch != 9) or (left_ch == 9 and right_ch != 6) :
            strobo = 1
            break

        if (left_ch in {0, 1, 8} and left_ch != right_ch) :
            strobo = 1
            break

        left += 1
        right -= 1

    if strobo == 0 :
        print(n, 'is a Strobo Grammatic Number')
    else :
        print(n, 'is not a Strobo Grammatic Number')
