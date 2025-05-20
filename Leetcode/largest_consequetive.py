def function(nums):
    hashset = set(nums)
    longest = 0
    for num in hashset:
        if num - 1 not in hashset:
            count = 1
            while (num + count) in hashset:
                count += 1
            longest = max(longest, count)
    return longest