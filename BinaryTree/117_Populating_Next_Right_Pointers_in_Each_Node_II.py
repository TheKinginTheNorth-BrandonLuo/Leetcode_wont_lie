# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 11:13:06 2022

@author: Fan Luo
"""
"""
117. Populating Next Right Pointers in Each Node II

Given a binary tree
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. 
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
"""
# Definition for a Node.
class TreeNode:
    def __init__(self, val = 0, left = None, right = None, next = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        if root is None:
            return None
        
        head = root
        
        while head:
            dummy = TreeNode(0)
            temp = dummy
            
            while head:
                if head.left is not None:
                    temp.next = head.left
                    temp = temp.next
                if head.right is not None:
                    temp.next = head.right
                    temp = temp.next
                head = head.next
            head = dummy.next
        return root

if __name__ == '__main__':
    None