class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # idea: have two pointers: left and right, which starts at the beginning and the end of the string.
        # First, check if left pointer is less than right pointer and the character each pointer points to is alphanumeric character.
        # If so, convert the char to lowercase and compare them, and increment the left pointer while decrementing right pointer.
        # If it's not alphanumeric char, shift the pointer.
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
