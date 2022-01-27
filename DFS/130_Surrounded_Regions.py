# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 22:38:03 2022

@author: Fan Luo
"""
"""
130. Surrounded Regions

Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

"""
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        ROWS, COLS = len(board), len(board[0])
        
        def capture(r, c):
            if r >= 0 and c >= 0 and r < ROWS and c < COLS and board[r][c] == 'O':
                board[r][c] = 'T'
                capture(r - 1, c)
                capture(r + 1, c)
                capture(r, c - 1)
                capture(r, c + 1)
                
        # 1. Capture boarder "O" and convert to "T"
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1])):
                    capture(r, c)
                    
        # 2. Convert non-boarder "O" to "X"
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                    
        # 3. Convert back "T" to "O"
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
                    
if __name__ == '__main__':
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    print(Solution().solve(board))
    print(board)