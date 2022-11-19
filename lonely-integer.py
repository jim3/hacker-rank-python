# Lonely Integer
# Given an array of integers, where all elements but one occur twice, find the unique element.

def lonely_integer(arr):
    arr = sorted(arr)
    print(arr)
    if len(arr) < 3:
        return arr[0]
    elif arr[0] != arr[1]:
        return arr[0]
    else:
        return lonely_integer(arr[2:])

arr = [18, 49, 15, 30, 56, 20, 49, 67, 82, 69, 84, 63, 93,
       87, 66, 17, 38, 32, 17, 32, 94, 66, 67, 63, 48, 64, 84, 82,
       87, 18, 79, 64, 79, 15, 71, 94, 59, 5, 22, 59, 4, 98, 81, 4,
       98, 73, 69, 88, 30, 81, 48, 56, 71, 20, 93, 22, 73, 5, 88
]

result = lonely_integer(arr)
print(result) # 38
