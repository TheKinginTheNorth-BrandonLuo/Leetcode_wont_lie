# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 17:22:35 2022

@author: Fan Luo
"""
"""
114. Flatten Binary Tree to Linked List

Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def flatten(self, root):
        if not root:
            return
        
        left = root.left
        right = root.right
        root.left = None
        
        self.flatten(left)
        self.flatten(right)
        
        root.right = left
        
        while root.right:
            root = root.right
            
        root.right = right
        
if __name__ == '__main__':
    None