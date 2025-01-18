from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        encoder_str = ""
        for s in strs:
            encoder_str += str(len(s)) + "#" + s
        return encoder_str

    def decode(self, s: str) -> List[str]:
        i = 0 # 文字列の位置を指定するための変数
        decoded_strs = []
        # #と#の間の数字を取得
        while i < len(s):
            j = i # jは、区切り文字の#の位置をさがすための変数
            while j < len(s) and s[j] != "#":
                j += 1
            # そうではなくて、#が見つかった場合
            length = int(s[i:j]) # 文字列の長さを取得 #の前の数字
            decoded_strs.append(s[j+1:j+1+length]) # 文字列を取得 #の後の文字列から、文字列の長さ分だけ取得
            i = j + 1 + length
        return decoded_strs

# Test Cases
solution = Solution()
# Example 1
assert solution.encode(["hello", "world"]) == "5#hello5#world"
assert solution.decode("5#hello5#world") == ["hello", "world"]

    
