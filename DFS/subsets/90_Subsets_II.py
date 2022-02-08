# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 20:07:45 2022

@author: Fan Luo
"""
"""
90. Subsets II

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        res = [[]]
        
        for i in nums:
            res += [item + [i] for item in res]
            
        # remove duplicate
        res2 = []
        for i in res:
            i = sorted(i)
            if i not in res2:
                res2.append(i)
        
        return res2
    
if __name__ == "__main__":
    print(Solution().subsetsWithDup([1,4,4,4]))