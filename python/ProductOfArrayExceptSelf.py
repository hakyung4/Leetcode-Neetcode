class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # initialize array we will return with a length of nums cuz the length of both arrays is gonna be the same
        ans = [1] * len(nums)

        # the idea is assuming there are 2 more arrays, prefix, which basically multiplies all the elements before specific element(starting at the beginning of the array), including itself, and postfix, which basically multiplies all the elements before specific element(starting from the end of the array), and we can get appropriate results by multiplying and positioning those two arrays.
        # For example, if nums = [1, 2, 3, 4], prefix = [1, 2, 6, 24], postfix = [24, 24, 12, 4]

        # initialize prefix
        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]
        
        # doing the same thing with postfix, but looping backwards.
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            # multipying postfix by whatever was with the prefix array cuz if we simply store the postfix, it would simply overwrite the ans array.
            ans[i] *= postfix
            postfix *= nums[i]
        
        return ans
