def searchMin(nums):
    l,r = 0, len(nums)-1
    min_element = float('inf')
    while l<r:
        if nums[l] < nums[r]:
            min_element = min(min_element, nums[l])
            break
        mid = (l+r)//2
        if nums[mid] >= nums[l]:
            l = mid + 1
        else:
            r = mid-1
    return min_element