class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
#   1. Initialize left, right pointers to the first and last bars of the height array, respectively.
#   2. Initialize variables left_max and right_max to zero.
#   3. While the left pointer is less than or equal to the right pointer, compare the heights of the bars pointed to by the left and right pointers.
#   4. If the height of the left bar is less than or equal to the height of the right bar, check if the height of the left bar is greater than the left_max variable. If it is, update left_max, otherwise, add left_max - height[left] to the "water" variable. Move the left pointer to the next bar.
#   5. If the height of the right bar is less than the height of the left bar, check if the height of the right bar is greater than the right_max variable. If it is, update right_max, otherwise, add right_max - height[right] to the "water" variable. Move the right pointer to the previous bar.
#   6. Return the value of the "water" variable.
        if not height:
            return 0
        left, right, left_max, right_max, water = 0, len(height) - 1, 0, 0, 0
        while left <= right:
            if height[left] <= height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        return water
        
