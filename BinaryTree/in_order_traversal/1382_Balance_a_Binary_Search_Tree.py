# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 22:29:02 2022

@author: Fan Luo
"""
"""
1382. Balance a Binary Search Tree

Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def balanceBST(self, root):
        def inOrder(root):
            if not root:
                return []
            return inOrder(root.left) + [root.val] + inOrder(root.right)
        
        def buildTree(nums):
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = buildTree(nums[:mid])
            root.right = buildTree(nums[mid + 1:])
            return root
        
        return buildTree(inOrder(root))