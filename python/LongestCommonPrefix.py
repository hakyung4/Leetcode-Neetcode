class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # if all strings start with different char, meaning there's no common prefix, simply return empty string.
        # so, initialize our result as an empty string
        res = ""

        # need to iterate strings simultaneously.
        for i in range(len(strs[0])):
            # compare the first char
            for s in strs:
                # check if i is still inbound  b/c length of each string might be different and one could be shorter than the first string, which will cause an error.
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            # update res
            res += strs[0][i]

        return res
