# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 16:51:51 2022

@author: Fan Luo
"""
"""
108. Convert Sorted Array to Binary Search Tree
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def sortedArrayToBST(self, nums):
        
        def toBST(nums, start, end):
            if start > end:
                return None
            
            mid = (start + end) // 2
            node = TreeNode(nums[mid])
            node.left = toBST(nums, start, mid - 1)
            node.right = toBST(nums, mid + 1, end)
            return node
        return toBST(nums, 0, len(nums - 1))
            
if __name__ == '__main__':
    None
            