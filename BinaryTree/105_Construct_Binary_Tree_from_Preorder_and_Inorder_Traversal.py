# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 17:16:26 2022

@author: Fan Luo
"""
"""
105. Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree 
    and inorder is the inorder traversal of the same tree, construct and return the binary tree.
    
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1:index + 1], inorder[:index])
        root.right = self.buildTree(preorder[index + 1], inorder[index + 1:])
        
        return root
    
if __name__ == '__main__':
    None