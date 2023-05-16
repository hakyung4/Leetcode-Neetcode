class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
       # The idea is to start with the container of the longest width and move the sides inwards one by one to see if we can get a larger area by shortening the width but getting a taller height. But how do we know which side to move?
        # The key insight here is that moving the longer side inwards is completely unnecessary because the height of the water is bounded by the shorter side. In other words, we will never be able to get a greater area by moving the longer side inwards because the height will either stay the same or get shorter, and the width will keep decreasing.
        # So we can skip all those calculations and instead move the shorter side inwards. This way, we might get a taller height and a larger area. So at each step, we calculate the area then move the shorter side inwards. When the left and right sides meet, we are done and we can return the largest area calculated so far.
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            area = (right - left) * min(height[right], height[left])
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
