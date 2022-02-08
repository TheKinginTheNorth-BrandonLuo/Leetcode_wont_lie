# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 22:49:45 2022

@author: Fan Luo
"""
"""
46. Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""

class Solution:
    def permute(self, nums):
        res = []
        
        def dfs(nums, res, path):
            if not nums:
                res.append(path)
            else:
                for i in range(len(nums)):
                    dfs(nums[:i] + nums[i + 1:], res, path + [nums[i]])
                    
        dfs(nums, res, [])
        return res