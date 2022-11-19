# A space explorer's ship crashed on Mars! They send a series of SOS messages to Earth for help.

def marsExploration(s):
    count = 0
    for i in range(0, len(s), 3):
        if s[i] != 'S':
            count += 1
        if s[i+1] != 'O':
            count += 1
        if s[i+2] != 'S':
            count += 1
    return count


result = marsExploration('SOSSPSSQSSOR')
print(result)

