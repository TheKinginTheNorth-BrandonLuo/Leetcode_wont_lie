# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 20:05:24 2022

@author: Fan Luo
"""
"""
1019. Next Greater Node In Linked List

You are given the head of a linked list with n nodes.

For each node in the list, find the value of the next greater node. 
That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.

Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). 
If the ith node does not have a next greater node, set answer[i] = 0.

Input: head = [2,1,5]
Output: [5,5,0]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def nextLargerNodes(self, head):
        stack = []
        res = []
        index = 0
        
        while head is not None:
            res.append(0)
            cur = head.val
            while stack and stack[-1][0] < cur:
                last_value = stack.pop()
                res[last_value[1]] = cur
            
            stack.append((cur, index))
            index += 1
            head = head.next
            
        return res