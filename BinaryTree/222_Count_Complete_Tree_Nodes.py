# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 14:12:05 2022

@author: Fan Luo
"""
"""
222. Count Complete Tree Nodes

Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, 
is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. 
It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.
Input: root = [1,2,3,4,5,6]
Output: 6
"""

"""
Well we could use pre-order or other order traversal but will cost O(n) time
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def countNodes(self, root):
        if root is None:
            return 0
        
        nodes = 0
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        
        if left_height == right_height:
            nodes = 2 ** left_height - 1 + self.countNodes(root.right) + 1
        else:
            nodes = 2 ** right_height - 1 + self.countNodes(root.left) + 1
        return nodes
        
        
        
    def getHeight(self, root):
        height = 0
        while root != None:
            height += 1
            root = root.left
        return root