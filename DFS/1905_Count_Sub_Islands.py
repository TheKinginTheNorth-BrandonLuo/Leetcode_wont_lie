# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 15:01:27 2022

@author: Fan Luo
"""
"""
1905. Count Sub Islands

You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.

Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
"""
class Solution:
    def countSubIslands(self, grid1, grid2):
        ROWS, COLS = len(grid1), len(grid1[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid2[r][c] == 0:
                return
            
            grid2[r][c] = 0
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        
        # make land in grid2 to water if land in grid1 is water
        for r in range(ROWS):
            for c in range(COLS):
                if grid1[r][c] == 0 and grid2[r][c] == 1:
                    dfs(r, c)
        
        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] == 1:
                    dfs(r, c)
                    count += 1
        
        return count