# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 21:42:33 2022

@author: Fan Luo
"""
"""
316. Remove Duplicate Letters

Given a string s, remove duplicate letters so that every letter appears once and only once. 
You must make sure your result is the smallest in lexicographical order among all possible results.


Input: s = "bcabc"
Output: "abc"

Input: s = "cbacdcbc"
Output: "acdb"
"""
class Solution:
    def removeDuplicateLetters(self, s):
        lookup = {}
        for i in range(len(s)):
            lookup[s[i]] = i
            
        stack = []
        seen = set()
        
        for i in range(len(s)):
            if s[i] in seen:
                continue
            
            while stack and stack[-1] > s[i] and lookup[stack[-1]] > i:
                seen.remove(stack[-1])
                stack.pop()
                
            stack.append(s[i])
            seen.add(s[i])
            
        return "".join(stack)