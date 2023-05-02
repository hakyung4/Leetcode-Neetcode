class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in range(nums.count(val)): # loop how many vals in the array
            nums.remove(val) # remove that val one by one
        return len(nums) # return the len of array, which is k
