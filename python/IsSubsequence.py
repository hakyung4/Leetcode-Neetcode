class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # i, j => works like eye pointers. initialized at the beginning of each string.
        i, j = 0, 0

        # run the loop while both of the pointers are inbound
        while i < len(s) and j < len(t):
            # if they have the same character, move to pointer to the next. basically incrementing both pointers.
            if s[i] == t[j]:
                i += 1
            # otherwise we didn't find the char at the position i. So, only increment j.
            # Regardless of comparison, j is always going to be incremented, so just incrementing it outside if statement.
            j += 1

            # if i is equal to the length of s, meaning that it reached to the end of string => for every char in string s, 
            # we were able to find the matching char in string t.
        return True if i == len(s) else False
