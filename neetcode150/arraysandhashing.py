def hashDuplicates(nums : list[int]) -> bool:
    hashSet = set()
    for num in nums:
        if num in hashSet: return True
        hashSet.add(num)
    return False

def validAnagrams(s1: str, s2:str) -> bool:
    def validAnagrams1(s1:str, s2:str):
        return sorted(s1) == sorted(s2)
    result1 = validAnagrams1()

    def validAnagrams2(s1:str, s2:str):
        a1 = [0 for _ in range(0,27)]
        for ch in s1:
            a1[ord(ch) - 'a'] += 1
        for ch in s2:
            a1[ord(ch) - 'a'] -= 1
        for a in a1:
            if a!=0: return False
        return True

def twoSum(nums: list[int], target: int) -> bool:
    hashMap = {}
    for num in nums:
        if num in hashMap:
            hashMap[num] = 1
        else:
            hashMap[num] += 1
    for num in target:
        if abs(target - num) in hashMap:
            return True
    return False

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    map = defaultdict(list) # {key: list[str]}
    for str in strs:
        arr = [0 for _ in range(0,27)]
        for ch in str:
            arr[ord(ch) - 'a'] += 1
        map[tuple(arr)].append(str)
    return map

def topKFreqElements(nums: list[int], k: int) -> list[int]:
    count = {}
    freq = [[] for _ in range(0, len(nums) + 1)]
    for num in nums:
        count[num] = 1 + count.get(num, 0)
    for k,v in count.items():
        freq[v].append(k)
    res = []
    for i in range(len(nums) -1, 0, -1):
        for num in freq[i]:
            res.append(num)
            if len(res)==k: return res
    
def productOfArrayDiscludingSelf(nums: list[int]):
    left = 1
    right = 1
    arr = [0 * len(nums)]
    for i in range(len(nums)):
        arr[i] = left
        left *= nums[i]
    for i in range(len(nums)-1, 0, -1):
        arr[i] *= right
        right *= nums[i]
    return arr

def longestCommonSubSeqeuence(nums: list[int]):
    numSet = set(nums)
    longest = 0

    for num in nums:
        if num - 1 not in numSet:
            length = 1
            while num + length in numSet:
                length += 1
            longest = max(longest, length)
    return longest
