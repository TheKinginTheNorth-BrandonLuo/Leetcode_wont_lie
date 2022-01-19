# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 14:01:31 2022

@author: Fan Luo
"""

"""
95. Unique Binary Search Trees II

Given an integer n, return all the structurally unique BST's (binary search trees), 
which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def generateTrees(self, n):
        def dfs(start, end):
            if start > end:
                return [None]
            
            res = []
            for i in range(start, end + 1):
                left = dfs(start, i - 1)
                right = dfs(i + 1, end)
                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        res.append(root)
                        
            return res
        return dfs(1, n)
        
if __name__ == '__main__':
    None    