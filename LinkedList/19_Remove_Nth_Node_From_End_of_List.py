# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 19:18:01 2022

@author: Fan Luo
"""
"""
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        
        length = 1
        while head.next:
            head = head.next
            length += 1
            
        for i in range(length - n):
            cur = cur.next
            
        cur.next = cur.next.next
        
        return dummy.next
    
if __name__ == '__main__':
    S = Solution()
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    head = l1
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = None
    print(S.removeNthFromEnd(head,2))