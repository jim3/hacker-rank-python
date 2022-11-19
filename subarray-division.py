# ----------------------------------------------#
# ---------------subarray_division--------------#
# ----------------------------------------------#

day, month = 18, 7
arr = [
    2, 5, 1, 3, 4, 4, 3, 5, 1,
    1, 2, 1, 4, 1, 3, 3, 4, 2,
    1
]


def birthday(arr, day, month):
    pairs = 0
    for i in range(len(arr)):
        sub_array = arr[i:i+month]
        if sum(sub_array) == day:
            pairs += 1
    return pairs


x = birthday(arr, day, month)
print(x)
