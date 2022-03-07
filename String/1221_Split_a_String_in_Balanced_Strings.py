# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 21:13:50 2022

@author: Fan Luo
"""
"""
1221. Split a String in Balanced Strings

Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it in the maximum amount of balanced strings.

Return the maximum amount of split balanced strings.

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
"""

"""
Two pointers problem
"""
class Solution:
    def balancedStringSplit(self, s):
        l_count, r_count, res = 0, 0, 0
        for c in s:
            if c == "L":
                l_count += 1
            else:
                r_count += 1
            if l_count == r_count:
                res += 1
        return res