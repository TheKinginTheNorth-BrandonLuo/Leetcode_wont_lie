# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 20:08:19 2022

@author: Fan Luo
"""
"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
    typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true
"""
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        dic1 = {}
        dic2 = {}
        for i in s:
            dic1[i] = dic1.get(i, 0) + 1
            
        for i in t:
            dic2[i] = dic2.get(i, 0) + 1
            
        if dic1 == dic2:
            return True
        else:
            return False