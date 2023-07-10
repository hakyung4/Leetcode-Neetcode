class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        # making an array to store (position, speed) in reverse order since each car is limited to the car in front of it.
        # idea is we can store each fleet's leading car in the stack, then return stack's length.
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        # everytime, we will store its time for eaching to the destination: formula is float(target - p) / s. then we append it to the stack. 
        for p, s in pair:  # Reverse Sorted Order
            stack.append(float(target - p) / s)
            # for the first car, no operation is needed. then append second car's time, if it's less than the first car, we will pop it because it won't be another leading fleet. If it is larger, then keep it on the stack.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
