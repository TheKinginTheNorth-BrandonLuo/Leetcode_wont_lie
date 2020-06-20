#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 10:37:10 2020

@author: luofan
"""

class Solution(object):
    def romanToInt(self, s):
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        high = 0
        ans = 0
        for c in s[::-1]:
            if dic[c] >= high:
                ans += dic[c]
                high = dic[c]
            else:
                ans -= dic[c]
        return ans
obl = Solution()
test = 'IV'
print(obl.romanToInt(test))