# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 10:09:55 2022

@author: Fan Luo
"""
"""
124. Binary Tree Maximum Path Sum

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence- 
has an edge connecting them. A node can only appear in the sequence at most once. 
Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxPathSum(self, root):
        res = [root]
        
        def dfs(root):
            if not root:
                return 0
            
            leftmax = dfs(root.left)
            rightmax = dfs(root.right)
            
            leftmax = max(0, leftmax)
            rightmax = max(0, rightmax)
            
            res[0] = max(leftmax + rightmax +  root.val, res[0])
            return root.val + max(leftmax, rightmax)
        
        dfs(root)
        return res[0]
    
if __name__ == '__main__':
    None