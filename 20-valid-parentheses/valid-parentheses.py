class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  
        # Stack represents "pending" opening brackets that need to be closed

        matchingSet = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        for c in s:
            if c in matchingSet:
                if stack and stack[-1] == matchingSet[c]:
                    stack.pop()
                else:
                   return False 
                #if opening bracket is not encountered first but instead a closing bracket is
            else:
                stack.append(c) 
                # opening brackets get puched because of this 
        return True if not stack else False 
        # if stack is empty after iteration else false 
        
            

        