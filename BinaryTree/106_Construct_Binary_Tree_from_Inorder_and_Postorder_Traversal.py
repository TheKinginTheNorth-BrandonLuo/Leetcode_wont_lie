# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 17:02:38 2022

@author: Fan Luo
"""
"""
106. Construct Binary Tree from Inorder and Postorder Traversal
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree 
    and postorder is the postorder traversal of the same tree, construct and return the binary tree.
    
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
            
        node = TreeNode(postorder[-1])
        index = inorder.index(postorder[-1])
        
        node.left = self.buildTree(inorder[:index], postorder[:index])
        node.left = self.buildTree(inorder[index + 1:], postorder[index:-1])
        
        return node
            
if __name__ == '__main__':
    None