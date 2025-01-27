class MinStack:
    """
    def __init__(self):
        self.stack = []
        return None

    def push(self, val: int) -> None:
        self.stack.append(val)
        # nullを返す
        return None

    def pop(self) -> None:
        self.stack.pop() # さいごの要素を削除する
        

    def top(self) -> int:
        return self.stack[-1] # さいごの要素を返す(お皿で言うと、一番上の皿を返す)

    def getMin(self) -> int: # 一番小さい値を返す
        return min(self.stack)
    """

    # 改善
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]: # 現在の最小値よりも小さい値が来た時に、min_stackに追加する
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]: # stackの最後の要素がmin_stackの最後の要素と一致する時に、min_stackからも削除する(毎回pushしてるわけではないから)
                self.min_stack.pop()
            self.stack.pop() # いつもstackから削除する

    def top(self) -> int:
        return self.stack[-1] if self.stack else None
    
    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None
        

"""
入力
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

出力
[null,null,null,null,-3,null,0,-2]

説明
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
"""
minstack = MinStack()
# minstack.push(-2)
print(minstack.push(-2))


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()