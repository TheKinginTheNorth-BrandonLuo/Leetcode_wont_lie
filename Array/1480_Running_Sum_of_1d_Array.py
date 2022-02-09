# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 23:36:39 2022

@author: Fan Luo
"""
"""
1480. Running Sum of 1d Array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
"""

class Solution:
    def runningSum(self, nums):
        return [sum(nums[:i + 1]) for i in range(len(nums))]
    
    
    
class SecondSolution:
    def runningSum2(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            
        return nums