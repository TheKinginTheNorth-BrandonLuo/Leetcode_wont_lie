# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 17:24:54 2022

@author: Fan Luo
"""
"""
78. Subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""
class Solution(object):
    def subsets(self, nums):
        res = [[]]
        for i in nums:
            res += [item + [i] for item in res]
        return res
    
if __name__ == '__main__':
    print(Solution().subsets([1,2,3]))