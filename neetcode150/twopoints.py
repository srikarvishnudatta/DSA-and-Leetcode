def validPalindrome(s: str):
    start = 0
    end = len(s) - 1
    while start <= end:
        if s[start] != s[end]: return False
        start += 1
        end -= 1
    return True

def twoSumSorted(nums: list[int], target: int):
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[left] + nums[right] == target: return left, right
        if nums[left] + nums[right] > target: left += 1
        else: right -=1

def containMostWater(nums: list[int]) -> int:
    left = 0
    right = len(nums)-1
    water = 0
    while left < right:
        area = min(nums[left], nums[right]) * (right - left)
        water = max(water,area)

        if(nums[left] < nums[right]): left += 1
        else: right -= 1
    return water

def maxProfit(prices: list[int]) -> int:
        left, right = 0,0
        n = len(prices)
        profit = 0
        while right<n:
            if prices[right] < prices[left]: 
                left = right
            profit = max(profit, prices[right] - prices[left])
            right += 1
        return profit


