def two_sum(nums, target):
    d = {}
    for i in range(len(nums)):
        d[nums[i]] = i
    for i in range(len(nums)):
        if target - nums[i] in d and d.get(target - nums[i]) != i:
            print(nums[i], target - nums[i])
            return [i, d.get(target - nums[i])]
    return [0, 0]