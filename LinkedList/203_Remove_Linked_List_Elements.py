# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 21:22:49 2022

@author: Fan Luo
"""
"""
203. Remove Linked List Elements

Given the head of a linked list and an integer val, 
remove all the nodes of the linked list that has Node.val == val, and return the new head.

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        
        while pre.next:
            if pre.next.val == val:
                pre.next = pre.next.next
            else:
                pre = pre.next
                
        return dummy.next
    
if __name__ == '__main__':
    None



