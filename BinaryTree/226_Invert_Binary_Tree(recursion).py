# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 13:31:50 2022

@author: Fan Luo
"""
"""
226. Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution(object):
    def invertTree(self, root):
        if root is None:
            return root
        
        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)
        
        return root
    
if __name__ == '__main__':
    None
        
        
