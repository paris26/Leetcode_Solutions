class Solution(object):
    def maxArea(self, height):
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            area = width * min(height[left] , height[right])

            max_area = max(area, max_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area