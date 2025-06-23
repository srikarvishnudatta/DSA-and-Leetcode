from collections import defaultdict


def majority_element(nums):
    # hashmap
    map = defaultdict(int)
    for num in nums:
        map[num]+=1
    n = len(nums)
    for num in nums:
        if map[num]>n//2:
            return num
    
    # voting algorithm
    count = 0
    candidate = 0
    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1  