from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = ['(', '[', '{']
        close_brackets = [')', ']', '}']

        if len(s) % 2 != 0:
            return False
        
        for char in s:
            if not stack:
                if char in close_brackets:
                    return False
                else:
                    stack.append(char)
            else:
                if char in open_brackets: # ここ改善
                    stack.append(char)
                else:
                    if open_brackets.index(stack[-1]) == close_brackets.index(char):
                        stack.pop()
                    else:
                        return False
                    
        if not stack:
            return True
        else:
            return False
        
# Example
s1 = "()" # True
s2 = "()[]{}" # True
s3 = "(]" # False
s4 = "([])" # True
s5 = "))" # False
 
sol = Solution()
assert sol.isValid(s1) == True
assert sol.isValid(s2) == True
assert sol.isValid(s3) == False
assert sol.isValid(s4) == True
assert sol.isValid(s5) == False