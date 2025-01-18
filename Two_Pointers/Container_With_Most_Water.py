from typing import List
import time
import signal

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # brute force
        res = 0
        for l in range(len(height)):
            for r in range(l+1, len(height)):
                area = (r-l) * min(height[l], height[r])
                res = max(res, area)

        return res
    
    def maxArea2(self, height: List[int]) -> int:
        # two pointers
        res = 0
        l, r = 0, len(height) - 1 # left, rightの初期化
        """
        一旦、具体例から考えて、一般化する
        height1 = [1,8,6,2,5,4,8,3,7]
        まず、l=0で、r=8の時、area = 1 * 8 = 8. 1 = min(height[l], height[r]), 8 = r-l
        res = 8
        そして、lの場所とrの場所を比べた時に、lの方が小さいので、lを右に動かす
        そして、l=1, r=8の時、area = (8 - 1) * 7 = 49.
        res = 49にする、そして、今度はrの方がlより小さいので、rを左に動かす
        これを繰り返して、rとlが同じ場所になった時に、終了する
        """
        while l < r: # 初期条件は満たす
            area = (r-l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return res

        
    


def load_height_from_file(filename):
    """Loads height data from a file."""
    height = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                try:
                # height.extend(map(int, line.strip().split(',')))  # Assuming comma-separated values
                    line = line.strip().replace('[', '').replace(']', '')
                    height.extend(map(int, line.split(',')))
                except ValueError:
                    print(f"Error: Invalid data in file '{filename}'.")
                    return None
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    return height


# Example
height1 = [1,8,6,2,5,4,8,3,7]
height2 = [1, 1]
height3 = [4,3,2,3]
# Load height4 from a file
height4 = load_height_from_file("height4.txt")

solution = Solution()

# Test1
assert solution.maxArea2(height1) == 49

# Test4
start_time = time.time()
print(solution.maxArea2(height4))
print("--- %s seconds ---" % (time.time() - start_time))

