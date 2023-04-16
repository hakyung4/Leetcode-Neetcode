class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # basically gonna compute the max in reverse order.
        # Initially, the max value is -1
        # basically, new max = max(oldMax, arr[i])

        rightMax = -1
        
        # Reverse iteration
        for i in range(len(arr) - 1, -1, -1):
            # recompute the max
            newMax = max(rightMax, arr[i])
            # replace current array value with rightMax
            arr[i] = rightMax
            # update current rightMax with current max value(newMax)
            rightMax = newMax
        
        return arr
