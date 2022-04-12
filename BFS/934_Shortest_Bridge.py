# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 20:27:16 2022

@author: Fan Luo
"""
"""
934. Shortest Bridge

You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

Input: grid = [[0,1],[1,0]]
Output: 1
"""
from collections import deque

class Solution:
    def shortestBridge(self, grid):
        N = len(grid)
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        visited = set()
        
        def invalid(r, c):
            return r < 0 or c < 0 or r == N or c == N
        
        # dfs function to fill hash set
        def dfs(r, c):
            if (invalid(r, c) or not grid[r][c] or (r, c) in visited):
                return 
            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        def bfs():
            res, queue = 0, deque(visited)
            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in directions:
                        new_r, new_c = r + dr, c + dc
                        if invalid(new_r, new_c) or (new_r, new_c) in visited:
                            continue
                        if grid[new_r][new_c]:
                            return res
                        queue.append([new_r, new_c])
                        visited.add((new_r, new_c))
                res += 1
                
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    dfs(r, c)
                    return bfs()