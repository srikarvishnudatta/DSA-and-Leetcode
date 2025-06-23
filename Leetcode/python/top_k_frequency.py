from collections import defaultdict


def top_k_frequency(nums, k):
    n = len(nums)
    bucket = [[] for _ in range(n + 1)]
    freq = defaultdict(int)
    for num in nums:
        freq[num] += 1
    for key, value in freq.items():
        bucket[value].append(key)
    res = []
    for i in range(len(bucket) - 1, 0, -1):
        for num in bucket[i]:
            res.append(num)
            if len(res) == k:
                return res