class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Create a Hash Set
        hashSet = set()

        for n in nums:
            if n in hashSet:
                return True
            hashSet.add(n)
        
        return False
