class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # by putting each string in a set(), each set will have unique character. If it has different num of unique chars, meaning that length of sets is different, it means they are not isomorphic.
        # using zip() function: basically, zip() returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, 
        # and then the second item in each passed iterator are paired together etc.
        # ex) zip("egg", "add") will produce (('e', 'a'), ('g','d')). it doesn't add duplicate values. Make it set to compare the length of it with other sets.
        # so basically if length of each set of string 's' and 't' and length of the zip(s,t) are the same, then it's isomorphic. otherwise, it's not.
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))
