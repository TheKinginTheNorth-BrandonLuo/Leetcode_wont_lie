# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 16:49:10 2022

@author: Fan Luo
"""
"""
52. N-Queens II

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
"""
class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        pos_diagnal = set()
        neg_diagnal = set()
        
        board = [["."] * n for i in range(n)]
        self.count = 0
        
        def backtrack(r):
            if r == n:
                self.count += 1
                return
            
            for c in range(n):
                if c in col or (r + c) in pos_diagnal or (r - c) in neg_diagnal:
                    continue
                    
                col.add(c)
                pos_diagnal.add(r + c)
                neg_diagnal.add(r - c)
                board[r][c] = "Q"
                
                backtrack(r + 1)
                
                col.remove(c)
                pos_diagnal.remove(r + c)
                neg_diagnal.remove(r - c)
                board[r][c] = "."
                
        backtrack(0)
        return self.count
    
    
if __name__ == '__main__':
    print(Solution().totalNQueens(4))