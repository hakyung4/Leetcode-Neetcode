class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        # initializing two pointers => i : gonna keep shifting starting from the end of a string. length: length of char
        # i: index of last elem
        i, length = len(s) - 1, 0

        # First, eliminate leading white spaces from the end of the string
        while s[i] == " ":
            # decrement the pointer b/c we are starting from the end of the string
            i -= 1
        
        # loop for counting the length of char while i is inbound
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        
        return length
