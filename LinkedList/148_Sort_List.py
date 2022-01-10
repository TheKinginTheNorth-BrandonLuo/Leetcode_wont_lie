# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 10:14:27 2022

@author: Fan Luo
"""

"""
148. Sort List
Given the head of a linked list, return the list after sorting it in ascending order.
Input: head = [4,2,1,3]
Output: [1,2,3,4]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def sortList(self, head):
        pre = head
        slow = head
        fast = head
        
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
            
        pre.next = None
        
        return self.merge(self.sortList(head), self.sortList(slow))
    
    def merge(self, head1, head2):
        dummy = ListNode(0)
        T = dummy
        
        while head1 and head2:
            if head1.val < head2.val:
                T.next = head1
                T = head1
                head1 = head1.next
            else:
                T.next = head2
                T = head2
                head2 = head2.next
        T.next = head1 or head2
        return dummy.next
    
if __name__ == '__main__':
    S = Solution()
    l1 = ListNode(4)
    l2 = ListNode(2)
    l3 = ListNode(1)
    l4 = ListNode(3)
    l5 = ListNode(5)
    head = l1
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = None
    print(S.sortList(head))