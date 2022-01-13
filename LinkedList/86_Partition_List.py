# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 10:14:27 2022

@author: Fan Luo
"""

"""
86. Partition List
Given the head of a linked list and a value x, 
partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
    
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def partition(self, head, x):
        h1 = l1 = ListNode(0)
        h2 = l2 = ListNode(0)
        
        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
            
        l2.next = None
        l1.next = h2.next
        return h1.next
    
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
    print(S.partition(head,2))