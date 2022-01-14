# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 19:02:29 2022

@author: Fan Luo
"""
"""
234. Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome.

Input: head = [1,2,2,1]
Output: true
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head):
        slow = head
        fast = head
        stack = []
        
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
            
        if fast:
            slow = slow.next
            
        while slow:
            p = stack.pop()
            if slow.val != p:
                return False
            slow = slow.next
        return True
    
if __name__ == '__main__':
    None