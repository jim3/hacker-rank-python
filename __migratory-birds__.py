# ------------------ #
#   Migratory_Birds  #
# ------------------ #

def migratoryBirds(arr):
    arr.sort()
    birds = {}

    for x in arr:
        if x in birds:
            birds[x] += 1
        else:
            birds[x] = 1

    return max(birds, key=birds.get)


arr = [1, 4, 4, 4, 5, 3]
print(migratoryBirds(arr))
