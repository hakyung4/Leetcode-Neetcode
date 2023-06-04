class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i not in {"+", "-", "*", "/"}:
                stack.append(int(i))
            else:
                num1, num2 = stack.pop(), stack.pop()
                if i == "+":
                    res = num1 + num2
                    stack.append(res)
                elif i == "-":
                    res = num2 - num1
                    stack.append(res)
                elif i == "*":
                    res = num1 * num2
                    stack.append(res)
                elif i == "/":
                    # don't really understand the line below but that's what I need to do in Python, not Python3.
                    res = int(float(num2) / num1)
                    stack.append(res)
        
        return stack[0]
