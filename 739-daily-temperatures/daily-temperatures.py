class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stackI, stackT = stack.pop() #you pop whichever value you enter into the result 
                res[stackI] = i - stackI #inserting at the stack index value 
            stack.append([i, t])
        return res

# i, t is the next value you are comparing with the current top of the stack
# after popping, you store the result in the result array
# otherwise, you keep on appending it on the stack to form a "monotonic stack"

#it is important to note that THE STACK PUSH AND POP WILL GO ON TILL THE WHILE LOOP IS RUNNING