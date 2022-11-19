""" 
The function accepts following parameters:
 1. INTEGER steps (number of steps on the hike)
 2. STRING path (a string describing the path)
The function is expected to return an INTEGER:
 3. INTEGER (the number of valleys traversed)

If we represent _ as sea level, a step up as / , and a step down as \ , the hike can be drawn as:

_/\      _
   \    /
    \/\/

The hiker enters and leaves one valley
 """

import math
import os


def countingValleys(steps, path):
    path_list = list(path)
    sealevel = 0
    num_valleys = 0

    for i in range(len(path_list)):
        if (path_list[i] == 'U'):
            sealevel += 1
            if (sealevel == 0):
                num_valleys += 1
        else:
            sealevel -= 1
    return num_valleys


result = countingValleys(8, 'UDDDUDUU')  # 1
print(result)
result = countingValleys(12, 'DDUUDDUDUUUD')  # 2
print(result)
