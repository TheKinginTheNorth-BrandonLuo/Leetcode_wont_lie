# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 10:29:30 2022

@author: Fan Luo
"""
"""
144. Binary Tree Preorder Traversal

Given the root of a binary tree, return the preorder traversal of its nodes' values.

Input: root = [1,null,2,3]
Output: [1,2,3]
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def preorderTraversal(self, root):
        if root is None:
            return []
        stack = root
        res = []
        while stack != []:
            root = stack.pop()
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return res