class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []

        for index in range(len(nums)):
            # after the array being sorted, if the first elem is greater than 0, then there's no way there are three integers summing up to 0.
            if nums[index] > 0:
                break
            # if two numbers are the same consecutively, then we already computed possible result or at least we tried, so no need to do the same work.
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            # reason why left pointer is not starting at the index, but index + 1, is that nums[index] is gonna be fixed, and we are gonna find other two numbers that's gonna sum up to 0 with nums[index]. So, left pointer is basically starting at the next position of nums[index].
            left, right = index + 1, len(nums) - 1
            while left < right:
                # Simply move nums[index] to the left side just like simpe inequality in math, then it makes sense.
                if nums[left] + nums[right] < 0 - nums[index]:
                    left += 1
                elif nums[left] + nums[right] > 0 - nums[index]:
                    right -= 1
                else:
                    res.append([nums[index], nums[left], nums[right]]) # After a triplet is appended, we try our best to incease the numeric value of its first element or that of its second.
                    left += 1 # The other pairs and the one we were just looking at are either duplicates or smaller than the target.
                    right -= 1 # The other pairs are either duplicates or greater than the target.
                    # We must move on if there is less than or equal to one integer in between the two integers.
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1 # The pairs are either duplicates or smaller than the target.

        return res
