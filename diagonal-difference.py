# Given a square matrix, calculate the absolute difference between the sums of its diagonals

def diagonalDifference(arr):
    sum1 = 0
    sum2 = 0
    for i in range(len(arr)):
        sum1 += arr[i][i]
        sum2 += arr[i][len(arr)-i-1]
    return abs(sum1-sum2)


arr = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9],
]

print(diagonalDifference(arr))

