#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 16:08:11 2020
#1. Two Sum
@author: luofan
"""

class Solution(object):
    def twoSum(self, nums, target):
        hash_table = {}
        for i in range(len(nums)):
            if target - nums[i] in hash_table:
                return[hash_table[target - nums[i]],i]
            else:
                hash_table[nums[i]] = i
obl = Solution()
test = [2,7,11,15]
print(obl.twoSum(test,9))