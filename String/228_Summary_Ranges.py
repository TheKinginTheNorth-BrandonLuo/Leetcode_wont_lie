# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 20:12:00 2022

@author: jiarong xia
"""
"""
228. Summary Ranges

You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
That is, each element of nums is covered by exactly one of the ranges, 
    and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
"""
class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return []
        
        res = []
        i = 0
        
        while i < len(nums):
            j = i
            while j < len(nums) - 1 and nums[j] + 1 == nums[j + 1]:
                j += 1
            if i == j:
                res.append(str(nums[i]))
            else:
                res.append("%s->%s" %(str(nums[i]), str(nums[j])))
            i = j + 1
        return res