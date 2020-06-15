#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 12:19:21 2020

@author: luofan
"""

class Solution(object):
    def isPalindrome(self,x):
        tmp = 0
        j = x
        if x < 0:
            return False
        while j > 0:
            tmp = tmp * 10 + j % 10
            j = j // 10
        return tmp == x
obl = Solution()
print(obl.isPalindrome(123))
        