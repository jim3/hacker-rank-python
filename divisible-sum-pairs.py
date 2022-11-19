# ------------ divisible sum pairs ------------ #
n = 6
k = 3
ar = [1, 3, 2, 6, 1, 2]


def divisibleSumPairs(n, k, ar):
    pairs = 0
    sum = 0
    for i in range(len(ar)):
        for j in range(len(ar)):
            sum = ar[i] + ar[j]
            if i < j and sum % k == 0:
                pairs += 1
    return pairs

    
x = divisibleSumPairs(n, k, ar)
print(x)
