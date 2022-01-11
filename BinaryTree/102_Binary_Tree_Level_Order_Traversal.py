# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 10:29:30 2022

@author: Fan Luo
"""
"""
102. Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        queue = [root]
        next_queue = []
        level = []
        res = []
        
        while queue != []:
            for root in queue:
                level.append(root.val)
                if root.left is not None:
                    next_queue.append(root.left)
                if root.right is not None:
                    next_queue.append(root.right)
            res.append(level)
            level = []
            queue = next_queue
            next_queue = []
        return res
        