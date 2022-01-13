# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 10:14:27 2022

@author: Fan Luo
"""

"""
143. Reorder List
You are given the head of a singly linked-list. The list can be represented as:
    L0 → L1 → … → Ln - 1 → Ln
    
Reorder the list to be on the following form:
    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
    
Input: head = [1,2,3,4]
Output: [1,4,2,3]
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        if head and head.next and head.next.next:
            slow = head
            fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            left = head    
            right = slow.next
            slow.next = None
        
            # reverse right linked list
            dummy = ListNode(0)
            dummy.next = right
            p = right.next
            right.next = None
            while p:
                tmp = p
                p = p.next
                tmp.next = dummy.next
                dummy.next = tmp
            right = dummy.next

            p1 = left
            p2 = right
            while p2:
                tmp1 = p1.next
                tmp2 = p2.next
                p1.next = p2
                p2.next = tmp1
                p1 = tmp1
                p2 = tmp2
                
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
    print(S.reorderList(head))
                
                
        
        
        
            
        