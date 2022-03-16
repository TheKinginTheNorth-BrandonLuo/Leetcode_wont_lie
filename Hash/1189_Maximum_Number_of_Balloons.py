# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 22:43:14 2022

@author: Fan Luo
"""
"""
1189. Maximum Number of Balloons

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Input: text = "nlaebolko"
Output: 1
"""
import collections

class Solution:
    def maxNumberOfBalloons(self, text):
        count = collections.Counter(text)
        count_ballon = collections.Counter("balloon")
        
        return min([count[char]//count_ballon[char] for char in count_ballon])