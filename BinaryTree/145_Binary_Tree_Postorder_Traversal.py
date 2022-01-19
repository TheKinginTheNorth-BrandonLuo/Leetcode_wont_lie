# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 13:45:15 2022

@author: Fan Luo
"""
"""
145. Binary Tree Postorder Traversal

Given the root of a binary tree, return the postorder traversal of its nodes' values.

input: [1,2,3,4,5,6,7]
output: [4,5,2,6,7,3,1]
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def postorderTraversal(self, root):
        if root is None:
            return []
        
        stack = [root]
        res = []
        
        while stack != []:
            root = stack.pop()
            if root:
                res.append(root)
                stack.append(root.left)
                stack.append(root.right)
        return res[::-1]
    
if __name__ == '__main__':
    None