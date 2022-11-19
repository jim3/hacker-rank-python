# ----------permuting_two_arrays----------#

def twoArrays(k, A, B):
    A.sort()
    B.sort()
    B.reverse()

    n = len(A)

    for idx in range(n):
        if A[idx] + B[idx] < k:
            return 'NO'

    return 'YES'


A = [1, 2, 2, 1]
B = [3, 3, 3, 4]
k = 10

result = twoArrays(k, A, B)
print(result)
# A = [2, 1, 3]
# B = [7, 8, 9]
