# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 16:41:41 2022

@author: Fan Luo
"""
"""
109. Convert Sorted List to Binary Search Tree

Given the head of a singly linked list where elements are sorted in ascending order, 
convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the 
depth of the two subtrees of every node never differ by more than 1.

Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def sortedListToBST(self, head):
        if head is None:
            return None
        
        def buildTree(head, tail):
            if head == tail:
                return
            
            slow = head
            fast = head
            
            while fast.next is not tail and fast.next.next is not tail:
                slow = slow.next
                fast = fast.next.next
                
            root = TreeNode(slow.val)
            root.left = buildTree(head, slow)
            root.right = buildTree(slow, tail)
            return root
        return buildTree(head, None)