# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 11:06:57 2022

@author: Fan Luo
"""
"""
116. Populating Next Right Pointers in Each Node

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. 
The binary tree has the following definition:
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        
class Solution(object):
    def connect(self, root):
        if root is None or root.left is None:
            return root
        
        
        root.left.next = root.right
        
        if root.next:
            root.right.next = root.next.left
        
        self.connect(root.left)
        self.connect(root.right)
        return root
    
if __name__ == '__main__':
    None
