class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        Map = {")": "(", "]": "[", "}": "{"} # hashmap - close bracket : open bracket
        stack = [] # create a stack using an array

        for c in s: # traverse each character in s
            if c not in Map: #appending open brackets.
                stack.append(c)
                continue

            # not stack: we had close bracket but stack is empty, which means there's no corresponding open bracket.
            # stack[-1] != Map[c]: check if open brackets are closed in the correct order. they will be different if they are not closed in the correct order.
            # if one of them is true, then we won't need to check further; immediately return false.
            if not stack or stack[-1] != Map[c]:
                return False
                
            # going to pop the corresponding open bracket if it matches with current close bracket
            stack.pop()

        # stack is going to be empty if it satisfies all the conditions to be a valid input string, meaning it must return true if stack is empty, so return 'not stack'
        return not stack
