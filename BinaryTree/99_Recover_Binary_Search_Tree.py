# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 16:04:23 2022

@author: Fan Luo
"""
"""
99. Recover Binary Search Tree

You are given the root of a binary search tree (BST), 
where the values of exactly two nodes of the tree were swapped by mistake. 
Recover the tree without changing its structure.

Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def recoverTree(self, root):
        self.res = []
        
        def dfs(node):
            if not node:
                return 
            
            dfs(node.left)
            self.res.append(node)
            dfs(node.right)
            
        dfs(root)
        
        sorted_res = sorted(n.val for n in self.res)
        
        for i in range(len(sorted_res)):
            self.res[i].val = sorted_res[i]