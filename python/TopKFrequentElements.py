class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # create counter object to count the frequency of each num
        count = Counter(nums)

        most_frequent_nums = count.most_common(k)
        # [(num1, num2), (num3, num4)]
        ans = []
        for i in range(len(most_frequent_nums)):
            ans.append(most_frequent_nums[i][0])
        # need to return [num1, num3]
        return ans
