# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 19:20:53 2022

@author: Fan Luo
"""
"""
36. Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
"""

class Solution:
    def isValidSudoku(self, board):
        N = 9
        
        # Row
        for r in range(N):
            row = [c for c in board[r] if c != "."]
            if len(row) != len(set(row)):
                return False
            
        # Col
        for c in range(N):
            col = [board[r][c] for r in range(N) if board[r][c] != "."]
            if len(col) != len(set(col)):
                return False
            
        # sub-box
        def subbox(R, C):
            l = set()
            for r in range(R, R + 3):
                for c in range(C, C + 3):
                    if board[r][c] == ".":
                        continue
                    if board[r][c] not in l:
                        l.add(board[r][c])
                    else:
                        return False
            return True
        
        for r in range(0, N, 3):
            for c in range(0, N, 3):
                if not subbox(r, c):
                    return False
        return True