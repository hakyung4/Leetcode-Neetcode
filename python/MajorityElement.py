class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # create Counter object to see the frequencies of each number in nums 
        count = Counter(nums)
        for i in count:
            # as the problem stated, if the element appears more than len(nums) / 2 times, then that's the answer we wanna return.
            if count[i] > len(nums) / 2:
                ans = i
        
        return ans
