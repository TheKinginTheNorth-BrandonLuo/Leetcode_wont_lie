# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 15:49:22 2022

@author: Fan Luo
"""

"""
99. Recover Binary Search Tree

You are given the root of a binary search tree (BST), 
where the values of exactly two nodes of the tree were swapped by mistake. 
Recover the tree without changing its structure.

Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def recoverTree(self, root):
        """
        Do not return anything, 
        modify root in-place instead.
        """
        self.n1 = None
        self.n2 = None
        self.pre = None
        self.searchTree(root)
        self.n1.val, self.n2.val = self.n2.val, self.n1.val
        
        
    def searchTree(self, root):
        if root:
            self.searchTree(root.left)
            if self.pre and self.pre.val > root.val:
                if self.n1 == None:
                    self.n1 = self.pre
                self.n2 = root
            self.pre = root
            self.searchTree(root.right)
            
if __name__ == '__main__':
    None