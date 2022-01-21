# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 00:00:45 2022

@author: Fan Luo
"""
"""
61. Rotate List

Given the head of a linked list, rotate the list to the right by k places.

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        tail = head
        
        length = 1
        while head.next:
            head = head.next
            length += 1
            
        head.next = tail
        head = head.next
        
        for i in range(length - k % length - 1):
            head = head.next
            
        res = head.next
        head.next = None
        return res
    
if __name__ == '__main__':
    None