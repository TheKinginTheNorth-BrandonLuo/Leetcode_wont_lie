#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 15:51:51 2020
#5. Longest Palindromic Substring
@author: luofan
"""

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2 or s == s[::-1]:
            return s
        start, maxlength = 0, 1
        for i in range(1, len(s)):
            odd = s[i - maxlength - 1: i + 1]
            even = s[i - maxlength: i + 1]
            if i - maxlength - 1 >= 0 and odd == odd[::-1]:
                start = i - maxlength - 1
                maxlength += 2
            elif i - maxlength >= 0 and even == even[::-1]:
                start = i- maxlength
                maxlength += 1
        return s[start:start + maxlength]
obl = Solution()
test = 'xzabcbatq'
print(obl.longestPalindrome(test))