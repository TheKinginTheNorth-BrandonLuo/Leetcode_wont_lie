# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 14:17:35 2022

@author: Fan Luo
"""
"""
542. 01 Matrix

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
"""
import collections

class Solution:
    def updateMatrix(self, mat):
        ROWS, COLS = len(mat), len(mat[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        queue = collections.deque()
        res = [[-1 for _ in range(COLS)] for _ in range(ROWS)]
        
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    res[r][c] = 0
                    queue.append((r, c))
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < ROWS and 0 <= new_c < COLS and res[new_r][new_c] == -1:
                    res[new_r][new_c] = res[r][c] + 1
                    queue.append((new_r, new_c))
                    
        return res
                    
        