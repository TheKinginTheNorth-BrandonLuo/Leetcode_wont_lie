# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 16:48:04 2022

@author: Fan Luo
"""
"""
51. N-Queens

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
"""
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        col = set()
        pos_diagnal = set()
        neg_diagnal = set()
        
        res = []
        board = [["."] * n for i in range(n)]
        
        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r + c) in pos_diagnal or (r - c) in neg_diagnal:
                    continue
                    
                col.add(c)
                pos_diagnal.add(r + c)
                neg_diagnal.add(r - c)
                
                board[r][c] = "Q"
                
                dfs(r + 1)
                
                col.remove(c)
                pos_diagnal.remove(r + c)
                neg_diagnal.remove(r - c)
                
                board[r][c] = "."
                
        dfs(0)
        return res