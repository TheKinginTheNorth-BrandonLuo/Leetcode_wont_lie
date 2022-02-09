# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 23:17:24 2022

@author: Fan Luo
"""
"""
329. Longest Increasing Path in a Matrix

Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
"""
class Solution:
    def longestIncreasingPath(self, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}
        
        def dfs(r, c, preval):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= preval):
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            
            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            
            dp[(r, c)] = res
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
                
        return max(dp.values())