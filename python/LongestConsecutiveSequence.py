class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Storing length of longest consecutive sequence.
        length = 0
        
        # Storing the length of the current consecutive sequence.
        count = 0
        
        # Storing all the unique elements of an array by creating a hash set.
        numSet = set()
        
        for element in nums:
            numSet.add(element)
        
        for element in nums:
            previousConsecutiveElement = element - 1
        
            if not previousConsecutiveElement in numSet:
                # Element is the first value of a consecutive sequence.
                j = element
            
                while j in numSet:
                
                    # The next consecutive element will be j + 1.
                    j += 1

                # Update maximum length of consecutive subsequence.
                length = max(length , j - element)
    
        return length
