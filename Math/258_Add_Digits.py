# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 22:23:27 2022

@author: Fan Luo
"""
"""
258. Add Digits

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
"""

class Solution:
    def addDigits(self, num: int) -> int:
        # 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,.....
        # 0,1,2,3,4,5,6,7,8,9,1, 2, 3, 4, 5, 6, 7,......
        
        return (num - 1) % 9 + 1 if num else 0
