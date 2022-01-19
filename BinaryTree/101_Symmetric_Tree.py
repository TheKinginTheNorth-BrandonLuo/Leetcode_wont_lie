# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 13:36:48 2022

@author: Fan Luo
"""
"""
101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Input: root = [1,2,2,3,4,4,3]
Output: true
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return True
        
        return self.isSymRecur(root.left, root.right)
        
        
        
    def isSymRecur(self, left, right):
        if left is None and right is None:
            return True
        
        if left is None or right is None or left.val != right.val:
            return False
        
        return self.isSymRecur(left.left, right.right) and self.isSymRecur(left.right, right.left)
    
if __name__ == '__main__':
    None