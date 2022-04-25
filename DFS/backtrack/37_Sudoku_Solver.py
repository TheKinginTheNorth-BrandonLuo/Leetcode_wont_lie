# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 17:37:10 2022

@author: Fan Luo
"""
"""
37. Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
"""
class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = [set() for _ in range(9)]
        COLS = [set() for _ in range(9)]
        BOXES = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    n = int(board[r][c])
                    ROWS[r].add(n)
                    COLS[c].add(n)
                    box_id = r // 3 * 3 + c // 3
                    BOXES[box_id].add(n)
                    
        self.solved = False
        
        def backtrack(i, j):
            if i == 9:
                self.solved = True
                return
            
            new_i = i + (j + 1) // 9
            new_j = (j + 1) % 9
            
            if board[i][j] != ".":
                backtrack(new_i, new_j)
            else:
                box_id = i // 3 * 3 + j // 3
                for n in range(1, 10):
                    if n not in ROWS[i] and n not in COLS[j] and n not in BOXES[box_id]:
                        ROWS[i].add(n)
                        COLS[j].add(n)
                        BOXES[box_id].add(n)
                        board[i][j] = str(n)
                        backtrack(new_i, new_j)
                        
                        if self.solved:
                            break
                        
                        if not self.solved:
                            ROWS[i].remove(n)
                            COLS[j].remove(n)
                            BOXES[box_id].remove(n)
                            board[i][j] = "."
                            
        backtrack(0, 0)
        
if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    output = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
    Solution().solveSudoku(board)
    print(board == output)