# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 18:15:30 2022

@author: Fan Luo
"""
"""
110. Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

    a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
    
Input: root = [3,9,20,null,null,15,7]
Output: true
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isBalanced(self, root):
        if not root:
            return True
        def dfs(root):
            if root is None:
                return 0
            return max(dfs(root.left),dfs(root.right))+1
        
        return abs(dfs(root.left)-dfs(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)