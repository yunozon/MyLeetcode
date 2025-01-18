from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 行だけをチェックする
        seen = set()
        for row in board:
            for cell in row:
                if cell != ".":
                    if cell in seen:
                        return False
                    seen.add(cell)
            seen.clear()
        
        seen = set()
        # 列だけをチェックする
        for i in range(9):
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in seen:
                        return False
                    seen.add(board[j][i])
            seen.clear()

        # 3x3のボックスをチェックする
        seen = set()
        start_row = 0
        start_col = 0
        end_row = 3
        end_col = 3
        max_row = 9
        
        for row in range(start_row, end_row):
            for col in range(start_col, end_col):
                if board[row][col] != ".":
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
            
            if row == end_row - 1:
                start_row += 3
                end_row += 3
                start_col = 0
                end_col = 3
                seen = set()
            elif row == max_row - 1:
                start_row = 0
                end_row = 3
                start_col += 3
                end_col += 3
                seen = set()
            elif row == max_row - 1 and col == max_row - 1:
                break
        
        return True
                
    





# Example 1
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

# Example 2
board2 = [[".",".",".",".","5",".",".","1","."],
          [".","4",".","3",".",".",".",".","."],
          [".",".",".",".",".","3",".",".","1"],
          ["8",".",".",".",".",".",".","2","."],
          [".",".","2",".","7",".",".",".","."],
          [".","1","5",".",".",".",".",".","."],
          [".",".",".",".",".","2",".",".","."],
          [".","2",".","9",".",".",".",".","."],
          [".",".","4",".",".",".",".",".","."]]

solution = Solution()
assert solution.isValidSudoku(board) == True
assert solution.isValidSudoku(board2) == False