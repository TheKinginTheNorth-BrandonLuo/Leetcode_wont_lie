# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 14:19:49 2022

@author: Fan Luo
"""
"""
199. Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def rightSideView(self, root):
        if root is None:
            return []
        
        queue = [root]
        level = []
        res = []
        
        while queue != [] and root is not None:
            for node in queue:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            res.append(node.val)
            queue = level
            level = []
        return res
    
if __name__ == '__main__':
    None

