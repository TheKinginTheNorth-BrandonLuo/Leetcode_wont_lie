#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 15:44:18 2020
## 6. Zigzag
@author: luofan
"""

class Solution(object):
    def convert(self, s, numRows):
        if numRows <= 1:
            return s
        zigzag = [''] * numRows
        row, step = 0, 1
        for i in s:
            if row == 0:
                step = 1
            if row == numRows - 1:
                step = -1
            zigzag[row] += i
            row += step
        return ''.join((zigzag))

test = "PAYPALISHIRING"
obl = Solution()
print(obl.convert(test, 3))