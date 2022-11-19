# The function is expected to return a STRING.
# The function accepts STRING s as parameter.


def pangrams(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    replace_str = sorted(s.replace(' ', '').lower())
    str = ''.join(dict.fromkeys(replace_str))
    if (sorted(str) == sorted(alphabet)):
        return 'pangram'
    else:
        return 'not pangram'


s = 'We promptly judged antique ivory buckles for the next prize'
# s = 'We promptly judged antique ivory buckles for the prize'
result = pangrams(s)
print(result)
