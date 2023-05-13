class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # creating left and right pointers.
        left, right = 0, len(numbers) - 1

        while left < right:
            # get the current sum
            curSum = numbers[left] + numbers[right]

            # if the current sum is greater than target, then we need to decrement the right pointer by 1 cuz the new current sum needs to be smaller than current current sum.
            if curSum > target:
                right -= 1
            
            # otherwise, this.
            elif curSum < target:
                left += 1

            # If curSum == target    
            else:    
                return [left + 1, right + 1]
