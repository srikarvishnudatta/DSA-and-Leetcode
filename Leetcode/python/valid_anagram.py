def is_anagram(s, t):
    count_s1 = [0] * 27
    count_s2 = [0] * 27
    for s1 in s:
        count_s1[ord(s1) - ord('a')] += 1
    for s2 in t:
        count_s2[ord(s2) - ord('a')] += 1

    for i in range(27):
        if count_s1[i] != count_s2[i]:
            return False
    return True