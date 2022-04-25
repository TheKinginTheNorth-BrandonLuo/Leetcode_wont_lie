# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 21:06:50 2022

@author: Fan Luo
"""
"""
938. Range Sum of BST

Given the root node of a binary search tree and two integers low and high, 
return the sum of values of all nodes with a value in the inclusive range [low, high].

Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rangeSumBST(self, root, low, high):
        res = [0]
        def dfs(node, low, high, res):
            if not node:
                return
            if low <= node.val <= high:
                res[0] += node.val
            if node.val > low:
                dfs(node.left, low, high, res)
            if node.val < high:
                dfs(node.right, low, high, res)
        dfs(root, low, high, res)
        return res[0]
            