# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 15:15:51 2022

@author: Fan Luo
"""
"""
107. Binary Tree Level Order Traversal II

Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. 
(i.e., from left to right, level by level from leaf to root).

Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]
"""
"""
What I can thought is in-order traverse tree and reverse this order
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def levelOrderBottom(self, root):
        if root is None:
            return []
        
        queue = []
        next_queue = []
        level = []
        res = []
        
        while queue != []:
            for root in queue:
                level.append(root.val)
                if root.left:
                    next_queue.append(root.left)
                if root.right:
                    next_queue.append(root.right)
            res.append(level)
            queue = next_queue
            next_queue = []
            level = []
            
        return res[::-1]
    
if __name__ == '__main__':
    None