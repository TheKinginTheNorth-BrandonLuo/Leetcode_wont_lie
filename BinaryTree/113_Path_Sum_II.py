# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 19:20:24 2022

@author: Fan Luo
"""
"""
113. Path Sum II

Given the root of a binary tree and an integer targetSum, 
return all root-to-leaf paths where the sum of the node values in the path equals targetSum. 
Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pathSum(self, root, targetSum):
        res = []
        self.dfs(root, targetSum, res, [])
        return res
        
    def dfs(self, root, targetSum, res, path):
        if not root:
            return
        
        if not root.left and not root.right:
            if targetSum == root.val:
                res.append(path + [root.val])
        self.dfs(root.left, targetSum - root.val, res, path + [root.val])
        self.dfs(root.right, targetSum - root.val, res, path + [root.val])
