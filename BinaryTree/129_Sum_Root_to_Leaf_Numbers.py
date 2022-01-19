# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 17:57:27 2022

@author: Fan Luo
"""
"""
129. Sum Root to Leaf Numbers

You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def sumNumbers(self, root):
        def dfs(cur, n):
            if not cur:
                return 0
            
            n = 10 * n + cur.val
            if not cur.left and not cur.right:
                return n
            return dfs(cur.left, n) + dfs(cur.right, n)
        return dfs(root, 0)
    
if __name__ == '__main__':
    None