# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 10:29:30 2022

@author: Fan Luo
"""
"""
94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Input: root = [1,2,3,4,5,6,7]
Output: [4,2,5,1,6,3,7]
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root):
        if root is None:
            return []
        stack = []
        res = []
        while root is not None or stack !=[]:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res
                    
