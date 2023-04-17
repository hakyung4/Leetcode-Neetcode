class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # in case count doesn't exist, initialize hashmap using defaultdict so that we don't have to deal with that edge case.
        # Defining a dictionary(hashmap) with values as a list
        res = defaultdict(list) # mapping char count to list of anagrams

        # go thru every string
        for s in strs:
            # initialize count array 
            count = [0] * 26 # there are 26 chars from a to z. map a -> 0, ..., z -> 25
            # go thru every single char in each string
            for c in s:
                # ord(c) : ascii val of current char, ord("a") : ascii val of lowercase a
                # increment count of each char
                count[ord(c) - ord("a")] += 1

            # group anagrams with this particular count
            # since list cannot be keys, make it tuple.
            res[tuple(count)].append(s)

        return res.values()
