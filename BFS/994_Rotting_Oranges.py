# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 18:17:36 2022

@author: Fan Luo
"""
"""
994. Rotting Oranges

You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
"""

from collections import deque

class Solution:
    def orangesRotting(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh, minute = 0, 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        directions = [[0, 1],[1, 0],[-1, 0],[0, -1]]
        
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if (new_r < 0 or new_r == ROWS) or (new_c < 0 or new_c == COLS) or grid[new_r][new_c] != 1:
                        continue
                    grid[new_r][new_c] = 2
                    q.append((new_r, new_c))
                    fresh -= 1
            minute += 1
            
        return minute if fresh == 0 else -1