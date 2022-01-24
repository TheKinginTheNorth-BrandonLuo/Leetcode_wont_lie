# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 20:52:58 2022

@author: Fan Luo
"""
"""
240. Search a 2D Matrix II

Write an efficient algorithm that searches for a target value in an m x n integer matrix. 
The matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.
    
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        col = len(matrix[0]) - 1
        row = 0
        
        while col >= 0 and row <= len(matrix)-1:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False
    
if __name__ == '__main__':
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    print(Solution().searchMatrix(matrix, 5))
    