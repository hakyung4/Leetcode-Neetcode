class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # if the length of two strings are not the same, the it's def not anagram
        if len(s) != len(t):
            return False
        
        # create two hashmaps for frequencies for each char in two strings
        countS, countT = {}, {}
        # not creating a seprate loop for 't' b/c the length of two strings are the same and we are doing the same thing for both.
        for i in range(len(s)):
            # increment count of character. get() function basically saying get the frequency of the char and if there's none -> default Value is 0.
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        # comparing two hashmaps
        return countS == countT
