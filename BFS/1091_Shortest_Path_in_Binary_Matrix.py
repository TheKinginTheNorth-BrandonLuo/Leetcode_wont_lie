# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:50:25 2022

@author: Fan Luo
"""
"""
1091. Shortest Path in Binary Matrix

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

    All the visited cells of the path are 0.
    All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

Input: grid = [[0,1],[1,0]]
Output: 2
"""
import collections

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        q = [(0, 0, 1)]
        grid[0][0] = 1
        for i, j, d in q:
            if i == n-1 and j == n-1: return d
            for x, y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)):
                if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                    grid[x][y] = 1
                    q.append((x, y, d+1))
        return -1
    
class Solution2:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)]
        visited = set()
        queue = collections.deque([(0,0,1)])
        visited.add((0, 0))
        
        while queue:
            i, j, distance = queue.popleft()
            if i == n - 1 and j == n - 1:
                return distance
            for d1, d2 in directions:
                x, y = i + d1, j + d2
                if 0 <= x <  n and 0 <= y < n:
                    if (x, y) not in visited and grid[x][y] == 0:
                        visited.add((x, y))
                        queue.append((x, y, distance + 1))
        return -1