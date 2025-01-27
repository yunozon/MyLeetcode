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
        
    # another solution
    def isValid2(self, s: str) -> bool:
        stack = []
        closeToOpen = {')':'(', ']':'[', '}':'{'} # 以前はopenとcloseのリストを作っていたが、こちらの方が簡潔

        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]: # stackがあって、かつ、最後が開きカッコと一致するとき、popする(閉じ括弧をキーとしている。)
                    stack.pop()
                else:
                    return False

            else:
                stack.append(char)
                
        return True if not stack else False


        
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

dict = {'a': 1, 'b': 2}
print(dict["a"])