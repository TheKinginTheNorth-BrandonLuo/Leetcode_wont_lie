# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 14:45:22 2022

@author: Fan Luo
"""
"""
1293. Shortest Path in a Grid with Obstacles Elimination

You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
"""
import collections

class Solution:
    def shortestPath(self, grid, k):
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        queue = collections.deque([(0, 0, k, 0)])
        visited = set()
        
        while queue:
            r, c, left_obstacle, path = queue.popleft()
            if (r, c, left_obstacle) in visited or left_obstacle < 0:
                continue
            if (r, c) == (ROWS - 1, COLS - 1):
                return path
            visited.add((r, c, left_obstacle))
            if grid[r][c] == 1:
                left_obstacle -= 1
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < ROWS and 0 <= new_c < COLS:
                    queue.append((new_r, new_c, left_obstacle, path + 1))
                    
        return -1