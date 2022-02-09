# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 18:09:17 2022

@author: Fan Luo
"""
"""
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node 
    down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1