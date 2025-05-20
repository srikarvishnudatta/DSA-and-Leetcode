from collections import defaultdict


def group_anagrams(strs):
    res = defaultdict(list)
    for s in strs:
        count = [0 for _ in range(1, 27)]
        for alpha in s:
            count[ord(alpha) - ord('a')] += 1
        res[tuple(count)].append(s)
    return res.values()