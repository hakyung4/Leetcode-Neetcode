class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # Add 0 at the beginning and end of flowerbed to handle edge cases.
        flowerbed = [0] + flowerbed + [0]
        # Initialize a variable called count to 0 to keep track of the number of flowers planted.
        count = 0
        # Iterate over flowerbed starting from the second element and ending at the second to last element:
        for i in range(1, len(flowerbed) - 1):
            # Check if the current plot and its neighbors are all empty (equal to [0, 0, 0]).
            if flowerbed[i-1:i+2] == [0, 0, 0]:
                # Plant a flower and update count
                flowerbed[i] = 1
                count += 1
            # If count is greater than or equal to n, return True as we have planted enough flowers.
            if count >= n:
                return True
        # Return False if not enough flowers have been planted
        return False
