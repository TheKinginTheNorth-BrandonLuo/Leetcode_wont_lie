# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 21:14:35 2022

@author: jiarong xia
"""
"""
200. Number of Islands
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
class Solution(object):
    def dfs(self, grid, r, c):
        grid[r][c] = '0'
        lst = [(r - 1, c),
               (r + 1, c),
               (r, c - 1),
               (r, c + 1)]
        
        for row, col in lst:
            if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[row]) and grid[row][col] == "1":
                self.dfs(grid, row, col)
    
    def numIslands(self, grid):
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    self.dfs(grid, r, c)
                    islands += 1
        return islands
    
if __name__ == '__main__':
    print(Solution().numIslands([
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]))