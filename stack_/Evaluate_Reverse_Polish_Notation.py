from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        symbols = { # 記号が来たら、それに対応する計算をする
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y),
        }
        for token in tokens:
            if token.isdigit() or token[1:].isdigit(): # もしくは、token.lsdigit() or len(token) > 1 
                stack.append(int(token))
            else:
                stack[-2] = symbols[token](stack[-2], stack[-1])
                stack.pop()
        return stack.pop()
    

# Example
"""
Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""

# Example 1
# tokens = ["2","1","+","3","*"]
# tokens = ["4","13","5","/","+"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# output = 9になるようにstackを使って計算する
# 一旦、具体例だけを考えて一般化は後で考える
stack = []
symbols = { # 記号が来たら、それに対応する計算をする
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: int(x / y),
}

for i, token in enumerate(tokens):
    print(f"{i}回目 : {stack}")
    if token.isdigit() or token[1:].isdigit(): # 数字の時 [1:]は、負の数の時のため
        stack.append(int(token))
    else:
        """
        y = stack.pop() # 数字を取り出す
        x = stack.pop() # 数字を取り出す
        stack.append(symbols[token](x, y)) # 取り出して計算して、結果をstackに追加する
        """
        stack[-2] = symbols[token](stack[-2], stack[-1]) # 一つ前の要素と計算して、結果をstackに追加する
        stack.pop()

result = stack.pop()
print(result)



