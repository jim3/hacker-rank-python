# -------------------------------- #
# ---------sales_by_match--------- #
# -------------------------------- #

from collections import Counter


def sockMerchant(n, l):
    counted = []
    num_pairs = []
    for i in l:
        if not i in counted:
            counted.append(i)
            num_pairs.append(l.count(i)//2)

    return sum(num_pairs)


def sockMerchantv2(n, l):
    return (sum([l.count(i)//2 for i in set(l)]))  # set(l) removes duplicates


def sockMerchantv3(n, l):
    return sum(num // 2 for num in Counter(l).values())


n = 7  # the number of socks in the pile
l = [10, 20, 20, 10, 10, 30, 50, 10, 20]  # (3 pairs)

result = sockMerchant(n, l)
print(f'There are {result} pairs of socks.')

result = sockMerchantv2(n, l)
print(f'There are {result} pairs of socks.')

l = [1, 2, 1, 2, 1, 3, 2]  # represents the color of each sock (2 pairs)
result = sockMerchantv3(n, l)
print(f'There are {result} pairs of socks.')
