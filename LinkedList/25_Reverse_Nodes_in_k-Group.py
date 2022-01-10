# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 10:14:27 2022

@author: Fan Luo
"""

"""
25. Reverse Nodes in k-Group
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = dummy.next
        num = 1
        while cur.next:
            num += 1
            cur = cur.next
            
        while num >= k:
            cur = pre.next
            
            for i in range(k - 1):
                t = cur.next
                cur.next = t.next
                t.next = pre.next
                pre.next = t
                
            pre = cur
            num -= k
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
    print(S.reverseKGroup(head,2))