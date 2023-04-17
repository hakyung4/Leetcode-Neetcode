class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevMap = {} # val : index

        for i, n in enumerate(nums): # enumerate(nums) => will be in index and value form
            # get the difference
            diff = target - n
            if diff in prevMap:
                # if the difference between target and n is in hashmap, that means we found a pair. so we return the index of that difference and n.
                return [prevMap[diff], i]
            # otherwise, update hashmap
            prevMap[n] = i
        
        return
