# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 20:02:21 2022

@author: Fan Luo
"""
"""
84. Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
    return the area of the largest rectangle in the histogram.

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
"""

class Solution:
    def largestRectangleArea(self, heights):
        stack, mx = [], 0
        
        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > h:
                print("stack is:", stack)
                H = heights[stack.pop()]
                print("H is :", H)
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                mx = max(mx, width * H)
                print("max is: ", mx)
            stack.append(i)
            
        return mx
    
if __name__ == '__main__':
    print(Solution().largestRectangleArea([2,1,5,6,2,3]))