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

def groupAnagrams():
    
    return