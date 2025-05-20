def maxArea(height):
    area = 0
    n = len(height)
    left = 0
    right = n - 1
    while left < right:
        calc = (right - left) * (min(height[right], height[left]))
        area = max(area, calc)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return area