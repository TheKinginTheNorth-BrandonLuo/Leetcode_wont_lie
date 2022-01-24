# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 21:00:11 2022

@author: Fan Luo
"""
"""
54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

class Solution(object):
    def spiralOrder(self, matrix):
        start_row, start_col = 0, 0
        end_row, end_col = len(matrix), len(matrix[0])
        res = []
        
        
        while start_row < end_row or start_col < end_col:
            # right
            if start_row < end_row:
                res.extend([matrix[start_row][i] for i in range(start_col, end_col)])
            start_row += 1
                
            # down
            if start_col < end_col:
                res.extend([matrix[i][end_col - 1] for i in range(start_row, end_row)])
            end_col -= 1
                
            # left
            if start_row < end_row: # note if end_col -1, start_col, -1, then 0 position will be null
                res.extend([matrix[end_row - 1][i] for i in range(end_col - 1, start_col - 1, -1)])
            end_row -= 1
                
            # up
            if start_col < end_col:
                res.extend([matrix[i][start_col] for i in range(end_row - 1, start_row - 1, -1)])
            start_col += 1
                
        return res
    
if __name__ == '__main__':
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(Solution().spiralOrder(matrix))