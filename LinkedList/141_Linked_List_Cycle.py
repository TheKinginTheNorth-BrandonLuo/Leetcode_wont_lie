# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 00:00:44 2022

@author: Fan Luo
"""
"""
141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be 
reached again by continuously following the next pointer. Internally, pos is used to 
denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if fast == slow:
                return True
        return False
    
if __name__ == '__main__':
    S = Solution()
    l1 = ListNode(3)
    l2 = ListNode(2)
    l3 = ListNode(0)
    l4 = ListNode(-4)
    l5 = ListNode(5)
    head = l1
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = None
    print(S.hasCycle(head))