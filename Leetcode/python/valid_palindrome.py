import re
def valid(s):
    s = s.lower()
    s = re.sub('[^a-z0-9]', "", s)
    print(s)
    se, e = 0, len(s) - 1
    while se <= e:
        if s[se] != s[e]:
            return False
        else:
            se += 1
            e -= 1
    return True