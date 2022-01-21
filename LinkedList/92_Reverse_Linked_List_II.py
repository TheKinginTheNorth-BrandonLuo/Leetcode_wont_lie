# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 00:00:21 2022

@author: Fan Luo
"""
"""
92. Reverse Linked List II

Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list.

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for i in range(left - 1):
            pre = pre.next
            
        cur = pre.next
        for i in range(right - left):
            post = cur.next
            cur.next = post.next
            post.next = pre.next
            pre.next = post
        return dummy.next
    

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
    print(S.reverseBetween(head,2, 4))