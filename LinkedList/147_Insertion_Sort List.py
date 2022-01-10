# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 10:14:27 2022

@author: Fan Luo
"""

"""
147. Insertion Sort List
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
It repeats until no input elements remain.
The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

Input: head = [4,2,1,3]
Output: [1,2,3,4]
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)
        pre = dummy
        node = head
        
        while node:
            cur = node
            node = node.next
            
            if cur.val < pre.val:
                pre = dummy
                
            while pre.next and cur.val > pre.next.val:
                pre = pre.next
            
            cur.next = pre.next
            pre.next = cur
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
    print(S.insertionSortList(head))
        