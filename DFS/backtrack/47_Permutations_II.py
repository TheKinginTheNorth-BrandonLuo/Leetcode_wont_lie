# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 23:19:27 2022

@author: jiarong xia
"""
"""
47. Permutations II

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        def dfs(nums, res, path):
            if not nums and path not in res:
                res.append(path)
            else:
                for i in range(len(nums)):
                    dfs(nums[:i] + nums[i + 1:], res, path + [nums[i]])
                    
        dfs(nums, res, [])
        return res