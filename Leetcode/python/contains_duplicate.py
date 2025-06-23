
def contains_duplicate(nums):
    hashmap = {}
    for i in nums:
        if i in hashmap:
            return True
        hashmap[i] = i
    return False