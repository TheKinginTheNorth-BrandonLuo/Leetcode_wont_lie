# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 22:45:41 2022

@author: Fan Luo
"""
"""
1721. Swapping Nodes in a Linked List

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head, k):
        cur = head
        res = []
        
        while cur:
            res.append(cur.val)
            cur = cur.next
            
        res[k - 1], res[-k] = res[-k], res[k - 1]
        
        dummy = cur = ListNode(0)
        for i in res:
            cur.next = ListNode(i)
            cur = cur.next
            
        return dummy.next
    
class SecondSolution:
    def swapNodes2(self, head, k):
        length = 0
        
        cur, p1, p2 = head, head, head
        
        while cur:
            length += 1
            cur = cur.next
            
        k2 = length - k
        
        while k > 1:
            k -= 1
            p1 = p1.next
            
        while k2 > 0:
            p2 = p2.next
            k2 -= 1
            
        p1.val, p2.val = p2.val, p1.val
        return head