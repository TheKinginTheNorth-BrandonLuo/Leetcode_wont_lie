#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:19:27 2020
11. Container with most water
@author: luofan
"""

class Solution(object):
    def maxArea(self, height):
        ans = 0
        l = 0
        r = len(height) - 1
        while l < r:
            ans = max(ans, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans
obl = Solution()
test = [1,8,6,2,5,4,8,3,7]
print(obl.maxArea(test))
