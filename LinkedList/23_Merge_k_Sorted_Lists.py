# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 10:14:27 2022

@author: Fan Luo
"""

"""
23. Merge k Sorted Lists
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        
        res = lists[0]
        for i in range(1, len(lists)):
            res = self.mergeTwiLists(res, lists[i])
        return res
        
    def mergeTwiLists(self, h1, h2):
        dummy = ListNode(0)
        pre = dummy
        
        if not h1:
            return h2
        if not h2:
            return h1
        
        while h1 and h2:
            if h1.val < h2.val:
                pre.next = h1
                h1 = h1.next
            else:
                pre.next = h2
                h2 = h2.next
            pre = pre.next
            
        if h1:
            pre.next = h1
        else:
            pre.next = h2
        return dummy.next
    
if __name__ == '__main__':
    None
