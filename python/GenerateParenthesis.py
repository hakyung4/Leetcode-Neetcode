class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.generateParentheses(result, "", 0, 0, n)
        return result

    # helper function
    # result: store generated combinations
    # current: current combination being generated
    # open: the count of "(" included in the current combination
    # close: the count of ")" included in the current combination
    # n: total number of pairs of parentheses to be included
    def generateParentheses(self, result, current, open, close, n):

        # If length of current is equal to 2n, we have generated a valid combination
        if len(current) == 2 * n:
            result.append(current)
            return
        
        if open < n:
            # If the count of opening parentheses open is less than n, we can add an opening parenthesis to the current combination and make a recursive call to generateParentheses, incrementing the open count by 1.
            self.generateParentheses(result, current + '(', open + 1, close, n)
        
        if close < open:
            # If the count of closing parentheses close is less than the open count, we can add a closing parenthesis to the current combination and make a recursive call to generateParentheses, incrementing the close count by 1.
            self.generateParentheses(result, current + ')', open, close + 1, n)
