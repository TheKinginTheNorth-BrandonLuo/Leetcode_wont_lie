# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 15:42:39 2022

@author: Fan Luo
"""
"""
230. Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, 
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Input: root = [3,1,4,null,2], k = 1
Output: 1
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def kthSmallest(self, root, k):
        def inOrder(root):
            if root is None:
                return []
            
            in_left = inOrder(root.left)
            in_right = inOrder(root.right)
            root_val = [root.val]
            
            return in_left + root_val + in_right
        
        return inOrder(root)[k - 1]
    
if __name__ == '__main__':
    None