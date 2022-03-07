# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 16:50:33 2022

@author: Fan Luo
"""
"""
179. Largest Number

Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

Input: nums = [10,2]
Output: "210"
"""
class Solution:
    def largestNumber(self, nums):
        nums = list(map(str, nums))
        
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if int(nums[i] + nums[j]) < int(nums[j] + nums[i]):
                    nums[i], nums[j] = nums[j], nums[i]
                    
        return "0" if nums[0] == "0" else "".join(nums)