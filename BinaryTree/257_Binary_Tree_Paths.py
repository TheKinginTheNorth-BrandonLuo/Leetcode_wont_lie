# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 17:27:27 2022

@author: Fan Luo
"""
"""
257. Binary Tree Paths

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def binaryTreePaths(self, root):
        if not root:
            return []
        def dfs(cur, res, path):
            if not cur.left and not cur.right:
                res.append(path)
            if cur.left:
                dfs(cur.left, res, path + "->" + str(cur.left.val))
            if cur.right:
                dfs(cur.right, res, path + "->" + str(cur.right.val))
        res = []
        dfs(root, res, ' ' + str(root.val))
        
        return res
    
if __name__ == '__main__':
    None