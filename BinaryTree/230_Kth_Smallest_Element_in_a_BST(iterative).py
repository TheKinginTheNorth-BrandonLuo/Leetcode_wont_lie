# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 15:23:39 2022

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
        n = 0
        stack = []
        cur = root
        
        while cur or stack: # when stack all been poped, then we go to right subtree, but this time cur is still exist
            while cur:
                stack.append(cur)
                cur = cur.left
                
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur.right