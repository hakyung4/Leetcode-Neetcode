class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Create an empty array that we'll return
        ans = []

        # B/c it's simply concatenation of two nums arrays, loop twice.
        for i in range(2):
            for n in nums:
                ans.append(n)

        return ans
